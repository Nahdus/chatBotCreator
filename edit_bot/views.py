from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View
from .models import Flow,FlowEndFlag
from dashboard.models import Bot
from .forms import createFlow,markEnd
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib import messages





class createFlow_form(View):
    model_flow = Flow
    model_bot=Bot
    model_flowend=FlowEndFlag
    QAform_class=createFlow
    QAend_class=markEnd
    
    
    template_name='edit_bot/set_flow.html'
    template_success='edit_bot/set_flow.html'
    
    
    def reorder():
        pass



    # displays blank form
    def get(self,request,bot_id,flow_id=None):
        QAform=self.QAform_class()
        QAend=self.QAend_class()
        # print(flow_id)
        
        def addFlow():
            flows= self.model_flow.objects.filter(bot=Bot.objects.get(id=bot_id)).order_by('order')
            #################################
            
            end_T_F=set()
            for each in flows:
                flowend=self.model_flowend.objects.get(flow=each)
                end_T_F.add(flowend)
                
            #end_T_F=self.model_flowend.objects.all()
                
            Flows_and_ends=zip(flows,end_T_F)
            
            order=len(flows)
            QAform.fields['order'].initial=order
            return render(request,
            self.template_name,
            {'form':QAform,
            'endfield':QAend,
            'Flows_and_ends':Flows_and_ends,
            "botid":bot_id,
            'form_media': QAform.media,})

        def modifyFlow(flow_id):
            flows= self.model_flow.objects.filter(bot=Bot.objects.get(id=bot_id)).order_by('order')
            flowToBeModified=self.model_flow.objects.get(id=flow_id)
            #################################
            
            end_T_F=set()
            for each in flows:
                flowend=self.model_flowend.objects.get(flow=each)
                end_T_F.add(flowend)
                
            #end_T_F=self.model_flowend.objects.all()
                
            Flows_and_ends=zip(flows,end_T_F)
            
            order=len(flows)

            QAform.fields['Question'].initial=flowToBeModified.Question
            QAform.fields['Answers'].initial=flowToBeModified.Answers
            # QAform.fields['bot'].initial=flowToBeModified.bot
            QAform.fields['order'].initial=flowToBeModified.order
            QAform.fields['words'].initial=flowToBeModified.words.tags

            return render(request,
            self.template_name,
            {'form':QAform,
            'endfield':QAend,
            'Flows_and_ends':Flows_and_ends,
            "botid":bot_id})
            # form = MyForm(initial={'charfield1': 'foo', 'charfield2': 'bar'})
           

        if not(flow_id):
            return addFlow()
        elif (flow_id):
            return modifyFlow(flow_id)




    def post(self, request,bot_id,flow_id=None):

        QAform=self.QAform_class(request.POST)
        QAend=self.QAend_class(request.POST)
        

        # print(QAform)
        if QAform.is_valid() and QAend.is_valid():

            FlowFromForm=QAform.save(commit=False)
            FlowEndFlagFromForm=QAend.save(commit=False)
            if (flow_id):#if flow is being modified
                flowX = self.model_flow.objects.get(id=flow_id)
                flowend=self.model_flowend.objects.get(flow=flowX)
            else:#else create a new flow
                flowX = FlowFromForm   
                flowend=FlowEndFlagFromForm         
            # flowend=FlowEndFlag

            #clean normalized data
            flowX.Question=QAform.cleaned_data['Question']
            flowX.Answers=QAform.cleaned_data['Answers']
            flowX.order=QAform.cleaned_data['order']
            flowX.words=QAform.cleaned_data['words']

            #clean normalized data
            flowend.end=QAend.cleaned_data['end']

            #clean normalized data


            flowX.bot=self.model_bot.objects.get(id=bot_id)
            try:
                flowX.save()
            except IntegrityError:
                print(IntegrityError.args)
                messages.add_message(request, messages.INFO, "Flow name should be unique")
                return redirect("dashboard:edit_bot:createflow",bot_id=bot_id)


            flowend.flow=self.model_flow.objects.get(id=flowX.pk)
            flowend.save()


            # return self.get(request,bot_id)
            return redirect("dashboard:edit_bot:createflow", bot_id=bot_id)
            # return render(request,self.template_name,{'form':form,'flows':flows })
        else:
           
            return render(request,self.template_name,
            {'form':QAform,            
            'error':QAform.errors,
            'form_media': QAform.media,})



def delete_flow(request,bot_id,flow_id):
    # print(bot_id)
    # print(flow_id)
    flow=Flow.objects.get(id=flow_id)
    flow.delete()
    return redirect("dashboard:edit_bot:createflow", bot_id=bot_id)
    



