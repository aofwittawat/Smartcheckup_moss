from django.db import models


class UserDetail(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)
    height = models.IntegerField(default=1)
    tel = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True, unique=True)
    userimage = models.ImageField(upload_to='image', null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class CheckUp(models.Model):
    userdetail = models.ForeignKey(
        UserDetail, on_delete=models.CASCADE, null=True, blank=True)
    HT = models.BooleanField(default=False)
    DM = models.BooleanField(default=False)
    DLP = models.BooleanField(default=False)
    hepatitis = models.BooleanField(default=False)
    chronic_hepatitis = models.BooleanField(default=False)
    osteoporosis = models.BooleanField(default=False)
    allergy = models.BooleanField(default=False)
    CVS = models.BooleanField(default=False)
    renal_stone = models.BooleanField(default=False)
    cancer = models.BooleanField(default=False)
    CA_breast = models.BooleanField(default=False)
    CA_ovary = models.BooleanField(default=False)
    CA_cervix = models.BooleanField(default=False)
    CA_GI = models.BooleanField(default=False)
    CA_liver = models.BooleanField(default=False)
    CA_pancreas = models.BooleanField(default=False)
    CA_others = models.BooleanField(default=False)
    CA_prostate = models.BooleanField(default=False)

    def __str__(self):
        return self.userdetail
