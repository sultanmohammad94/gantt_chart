from django.db import models
class Task(models.Model):
    """This class represnts a DXHTML Task."""
    
    id = models.AutoField(primary_key = True, editable = False)
    text = models.CharField(blank = True, max_length = 150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = models.IntegerField()
    progress = models.FloatField()
    parent = models.CharField(max_length = 150)
    
    def __repr__(self) -> str:
        return self.text
    
    
    
class Link(models.Model):
    id = models.AutoField(primary_key = True, editable = False)
    source = models.CharField(max_length = 150)
    target = models.CharField(max_length = 150)
    type = models.CharField(max_length = 150)
    lag = models.IntegerField(blank = True, default = 0)
    
    def __repr__(self) -> str:
        return self.id
