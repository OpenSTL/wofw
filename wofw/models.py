from django.db import models

# Create your models here.
class ward(models.Model):
    wardnumber = models.IntegerField(default=0)
    
class alderman(models.Model):
    ward = models.ForeignKey(ward)
    alderlast = models.CharField(max_length=100)
    alderfull = models.CharField(max_length=200)
  
class bill(models.Model):
    billnumber = models.IntegerField(default=0)
    billname = models.CharField(max_length=200)
    
class vote(models.Model):
    AYE = 'aye'
    NAY = 'nay'
    PRESENT = 'present'
    NOVOTE = 'no vote'
    VOTE_CHOICES = (
        (AYE, 'aye'),
        (NAY, 'nay'),
        (PRESENT, 'present'),
        (NOVOTE, 'no vote'),
    )
    COMMITTEE = 'committee'
    PERFECTION = 'perfection'
    FINAL = 'final'
    READING_CHOICES = (
        (COMMITTEE, 'committee'),
        (PERFECTION, 'perfection'),
        (FINAL, 'final'),
    )
    alderlast = models.ForeignKey(alderman)
    billnumber = models.ForeignKey(bill)
    vote = models.CharField(max_length=10, choices=VOTE_CHOICES)
    reading = models.CharField(max_length=20, choices=READING_CHOICES) 
    date = models.DateField()
    
    
