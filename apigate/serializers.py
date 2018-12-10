from rest_framework import serializers
from edit_bot.models import Flow,Bot,FlowEndFlag

class FlowSerializers(serializers.ModelSerializer):
    words = serializers.StringRelatedField(many=True)
    bot = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Flow
        fields = ('FlowName','bot','order','Question','Answers','words')

class FlowEndFlagSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = FlowEndFlag
        fields = ('end','flow')

class BotSerializers(serializers.ModelSerializer):
    # bot = serializers.StringRelatedField(many=False)
    class Meta:
        model = Bot
        fields = ('Name','id')