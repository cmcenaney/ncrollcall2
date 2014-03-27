from django.db import models
from django.core.exceptions import MultipleObjectsReturned

# Create your models here.
class gadb_action(models.Model):
    action_id = models.IntegerField(unique=False, max_length=4, primary_key=True)
    bill_id = models.IntegerField(unique=False, max_length=12)
    datetime = models.CharField(unique=False, max_length=50)
    chamber = models.CharField(unique=False, max_length=50)
    motion = models.CharField(unique=False, max_length=50)
    rcs_num = models.IntegerField(unique=False, max_length=12)
    aye = models.CharField(unique=False, max_length=50)
    no = models.CharField(unique=False, max_length=50)
    not_voting = models.IntegerField(unique=False, max_length=12)
    exc_abs = models.IntegerField(unique=False, max_length=12)
    exc_vote = models.IntegerField(unique=False, max_length=12)
    total_votes = models.IntegerField(unique=False, max_length=12)
    result = models.CharField(unique=False, max_length=50)
    
    class Meta(object):
        verbose_name_plural = "Action"
        #ordering = ('-date', 'name',)
        
    def __unicode__(self):
        return U'%s' %(self.action_id)

class gadb_bill(models.Model):
    bill_id = models.IntegerField(unique=False, max_length=4, primary_key=True)
    chamber = models.CharField(unique=False, max_length=50)
    subject = models.CharField(unique=False, max_length=50)
    doc_id = models.CharField(unique=False, max_length=50)
    doc_url = models.CharField(unique=False, max_length=50)
    is_featured = models.IntegerField(unique=False, max_length=12)
    description = models.CharField(unique=False, max_length=50)
    status = models.CharField(unique=False, max_length=50)
    last_action = models.CharField(unique=False, max_length=50)

    class Meta(object):
        verbose_name_plural = "Bill"
        #ordering = ('-date', 'name',)
        
    def __unicode__(self):
        return U'%s' %(self.chamber + "B " + str(self.bill_id) + " " + self.subject)

class gadb_vote(models.Model):
    vote_id = models.IntegerField(unique=False, max_length=11,primary_key=True)
    legislator_id = models.IntegerField(unique=False, max_length=11)
    action_id = models.IntegerField(unique=False, max_length=11)
    vote = models.CharField(unique=False, max_length=3)
    with_party = models.IntegerField(unique=False, max_length=4)

    class Meta(object):
        verbose_name_plural = "Vote"
    #     #ordering = ('-date', 'name',)
        
    def __unicode__(self):
        return U'%s' %(self.action_id)


class gadb_legislator(models.Model):
    legislator_id = models.IntegerField(unique=False, max_length=11, primary_key=True)
    ncga_id = models.IntegerField(unique=False, max_length=11)
    first_name = models.TextField(unique=False, max_length=50)
    last_name = models.TextField(unique=False, max_length=50) 
    chamber = models.CharField(unique=False, max_length=50)
    district = models.IntegerField(unique=False, max_length=5)
    party = models.CharField(unique=False, max_length=50)
    office_addr = models.CharField(unique=False, max_length=50)
    office_phone = models.CharField(unique=False, max_length=50)
    email = models.CharField(unique=False, max_length=50)
    legislative_addr = models.CharField(unique=False, max_length=80)
    terms = models.CharField(unique=False, max_length=50)
    counties = models.CharField(unique=False, max_length=50)
    occupation = models.CharField(unique=False, max_length=50)
    home_address = models.CharField(unique=False, max_length=50)
    total_votes = models.IntegerField(unique=False, max_length=11)
    eligible_votes = models.IntegerField(unique=False, max_length=11)
    actual_votes = models.IntegerField(unique=False, max_length=11)
    with_majority = models.IntegerField(unique=False, max_length=11)
    against_majority = models.IntegerField(unique=False, max_length=11)
    photo = models.CharField(unique=False, max_length=50)
    votelist = models.ManyToManyField(gadb_vote)

    class Meta(object):
        verbose_name_plural = "Legislator"
        #ordering = ('-date', 'name',)
        
    def __unicode__(self):
        return U'%s' %(self.last_name + ", " + self.first_name)

class gadb_stats(models.Model):
    stat_id = models.IntegerField(unique=False, max_length=11, primary_key=True)
    stat_name = models.CharField(unique=False, max_length=50)
    value = models.CharField(unique=False, max_length=50)

    class Meta(object):
        verbose_name_plural = "Stats"
        #ordering = ('-date', 'name',)
        
    def __unicode__(self):
        return U'%s' %(self.stat_id)

