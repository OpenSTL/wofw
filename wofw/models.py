from django.db import models


# Create your models here.
class Ward(models.Model):
    wardnumber = models.IntegerField(default=0)
    
    def __unicode__(self):
        return unicode(self.wardnumber)

    # the total number of wards in st louis
    totalCount = 28

class Alderman(models.Model):
    ward = models.ForeignKey(Ward)
    alderlast = models.CharField(max_length=100)
    alderfull = models.CharField(max_length=200)
    
    def __unicode__(self):
        return unicode(self.alderlast)
  
class Bill(models.Model):
    billnumber = models.IntegerField(default=0)
    billname = models.CharField(max_length=200)
    
    def __unicode__(self):
        return unicode(self.billnumber)
        
class Vote(models.Model):
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
    alderlast = models.ForeignKey(Alderman)
    billnumber = models.ForeignKey(Bill)
    vote = models.CharField(max_length=10, choices=VOTE_CHOICES)
    reading = models.CharField(max_length=20, choices=READING_CHOICES)
    
    def __unicode__(self):
        return unicode(self.vote)
    
