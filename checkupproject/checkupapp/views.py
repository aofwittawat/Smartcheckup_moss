from django.shortcuts import render,redirect
from checkupapp.models import UserDetail, CheckUp


def Home(request):
    return render(request, 'home.html')

def checkformUser(request):
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        age = data.get('age')
        weight = data.get('weight')
        height = data.get('height')
        tel = data.get('tel')

        new = UserDetail()
        new.username = username
        new.firstname = firstname
        new.lastname = lastname
        new.age = age
        new.weight = weight
        new.height = height
        new.tel = tel
        new.save()
        return redirect('checkform')
    return render(request, 'checkform_user.html')



def Form(request):
    if request.method == 'POST':
        data = request.POST.copy()
        HT = data.get('HT')
        DM = data.get('DM')
        DLP = data.get('DLP')
        hepatitis = data.get('hepatitis')
        chronic_hepatitis = data.get('chronic_hepatitis')
        osteoporosis = data.get('osteoporosis')
        allergy = data.get('allergy')
        CVS = data.get('CVS')
        cancer = data.get('cancer')
        CA_breast = data.get('CA_breast')
        CA_ovary = data.get('CA_ovary')
        CA_cervix = data.get('CA_cervix')
        CA_GI = data.get('CA_GI')
        CA_liver = data.get('CA_liver')
        CA_pancreas = data.get('CA_pancreas')
        CA_prostate = data.get('CA_prostate')
        
        
        new = CheckUp()
        new.HT = HT
        new.DM = DM
        new.DLP = DLP
        new.hepatitis = hepatitis
        new.chronic_hepatitis = chronic_hepatitis
        new.osteoporosis = osteoporosis
        new.allergy  = allergy 
        new.CVS = CVS
        new.cancer = cancer
        new.CA_breast = CA_breast
        new.CA_ovary = CA_ovary
        new.CA_cervix = CA_cervix
        new.CA_GI = CA_GI
        new.CA_liver = CA_liver
        new.CA_pancreas = CA_pancreas
        new.CA_prostate = CA_prostate
        new.save()
        

    return render(request, 'checkform.html')
