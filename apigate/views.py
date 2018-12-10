from django.shortcuts import render
from rest_framework import generics
from edit_bot.models import Flow
from .serializers import FlowSerializers,BotSerializers,FlowEndFlagSerializers
from dashboard.models import Bot
from rest_framework.response import Response


class BotFlowViewList(generics.ListCreateAPIView):
    
    
    serializer_class = FlowSerializers
    

    def get_queryset(self):
        print(Bot.objects.get(id=self.botId))
        return Flow.objects.filter(bot=Bot.objects.get(id=self.botId))
    
    
    def list(self, request,bot_id):
        self.botId=bot_id
        queryset=self.get_queryset()
        print(queryset)
        serializer = self.serializer_class(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)


class Botlist(generics.ListCreateAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializers

class FlowViewList(generics.ListCreateAPIView):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializers
