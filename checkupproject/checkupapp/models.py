from django.db import models


class UserDetail(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)
    height = models.IntegerField(default=1)
    tel = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    userimage = models.ImageField(upload_to='image', null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class CheckUp(models.Model):
    userdetail = models.ForeignKey(UserDetail,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True)
    HT = models.BooleanField(default=False, null=True, blank=True)
    DM = models.BooleanField(default=False, null=True, blank=True)
    DLP = models.BooleanField(default=False, null=True, blank=True)
    hepatitis = models.BooleanField(default=False, null=True, blank=True)
    chronic_hepatitis = models.BooleanField(default=False,
                                            null=True,
                                            blank=True)
    osteoporosis = models.BooleanField(default=False, null=True, blank=True)
    allergy = models.BooleanField(default=False, null=True, blank=True)
    CVS = models.BooleanField(default=False, null=True, blank=True)
    renal_stone = models.BooleanField(default=False, null=True, blank=True)
    cancer = models.BooleanField(default=False, null=True, blank=True)
    CA_breast = models.BooleanField(default=False, null=True, blank=True)
    CA_ovary = models.BooleanField(default=False, null=True, blank=True)
    CA_cervix = models.BooleanField(default=False, null=True, blank=True)
    CA_GI = models.BooleanField(default=False, null=True, blank=True)
    CA_liver = models.BooleanField(default=False, null=True, blank=True)
    CA_pancreas = models.BooleanField(default=False, null=True, blank=True)
    CA_others = models.BooleanField(default=False, null=True, blank=True)
    CA_prostate = models.BooleanField(default=False, null=True, blank=True)
