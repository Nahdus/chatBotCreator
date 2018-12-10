from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.edit import CreateView
from django.views.generic import View
from .models import Bot
from .forms import createBot




def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


# class createbot(CreateView):
#     model = Bot
#     fields = ['Name']


class createBot_form(View):
    model = Bot
    form_class=createBot
    template_name='dashboard/dashboard.html'
    template_success='dashboard/dashboard.html'
    
    # displays blank form
    def get(self,request):
        form=self.form_class()
        bots= self.model.objects.all()
        
        
        return render(request,self.template_name,{'form':form,'bots':bots })
    
    
        

    #submits the filled form
    def post(self, request):
        form=self.form_class(request.POST)
        bots= self.model.objects.all()
        
        if form.is_valid():

            Bot=form.save(commit=False)
            bot = Bot
            #clean normalized data
            bot.Name=form.cleaned_data['Name']
            bot.save()
            
            return render(request, self.template_success, {'form':form,'bots':bots })
        else:
           
            return render(request, self.template_name, {'form':form,'bots':bots })

def botDetail(request,bot_id):
    bot=get_object_or_404(Bot, pk=bot_id)
    print(bot.Name)
    return render(request,'botDetail/botDetail.html',{'bot':bot})

def deleteBot(request,bot_id):
    Bot.objects.get(pk=bot_id).delete()
    
    #botToBeDeleted.delete()
    bot= Bot.objects.all()
    
    return redirect('dashboard:home')





