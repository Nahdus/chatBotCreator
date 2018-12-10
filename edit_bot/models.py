from django.db import models
from dashboard.models import Bot
import tagulous.models
from django.utils.translation import gettext as _



class Flow(models.Model):
    FlowName=models.CharField(_("Flow Name"), max_length=50)
    Question=models.TextField()
    Answers=models.TextField()
    bot=models.ForeignKey(Bot,on_delete=models.CASCADE)
    order=models.PositiveIntegerField()
    words=tagulous.models.TagField(max_count=50)
    
    class Meta:
        unique_together = (("bot", "FlowName"),)  

    def __str__(self):
        return(str(self.pk)+" "+self.Question)



class FlowEndFlag(models.Model):
    end=models.BooleanField()
    flow=models.ForeignKey(Flow,on_delete=models.CASCADE)

    def __str__(self):
        return(str(self.pk)+" "+self.flow.Question)
