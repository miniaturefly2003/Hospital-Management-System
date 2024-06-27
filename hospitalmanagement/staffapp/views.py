from django.shortcuts import render,redirect
from staffapp.models import Doctor,Patient
# Create your views here.
def loginPageView(request):
    return render(request,'login.html',{})

def adminPageView(request):
    return render(request,'admin.html',{})

def doctorPageView(request):
    patients=Patient.objects.all()
    context={
            'allpatients':patients
            }
    return render(request=request,template_name='doctor.html',context=context)

def checkStaffView(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print("Name- ",username)
        print("Address- ",password)
        if username=="abhijith"and password=="1234":
            return render(request,'admin.html',{})
        else:
            doctor=Doctor.objects.filter(username=username,password=password)
            if doctor.count()>0:
                patients=Patient.objects.all()
                context={
                            'allpatients':patients
                        }
                return render(request=request,template_name='doctor.html',context=context)
            else:
                return render(request,'login.html',{})
        
        

def addDoctorView(request):
    return render(request,'addDoctor.html',{})    

def addPatientView(request):
    return render(request,'addPatient.html',{})      

def saveDoctorView(request):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        number=request.POST['number']
        email=request.POST['email']
        master=request.POST['master']
        username=request.POST['username']
        password=request.POST['password']

        print("Name- ",name)
        print("Address- ",address)
        print("Email- ",email)

        doctor=Doctor(name=name,address=address,number=number,email=email,master=master,username=username,password=password)
        doctor.save()
    return redirect('registerdoctor')

def savePatientView(request):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        number=request.POST['number']
        ailment=request.POST['ailment']
        email=request.POST['email']
        feedback=request.POST['feedback']

        print("Name- ",name)
        print("Address- ",address)
        print("Email- ",email)

        patient=Patient(name=name,address=address,number=number,ailment=ailment,email=email,feedback=feedback)
        patient.save()
    return redirect('registerpatient')

def getallDoctors(request):
    doctors=Doctor.objects.all()
    context={
        'alldoctors':doctors
    }
    return render(request=request,template_name='alldoctors.html',context=context)

def getallPatients(request):
    patients=Patient.objects.all()
    context={
        'allpatients':patients
    }
    return render(request=request,template_name='allpatients.html',context=context)

def deleteDoctorView(request,doctor_id):
    doctor=Doctor.objects.filter(pk=doctor_id)
    doctor.delete()
    return redirect('alldoctor')

def deletePatientView(request,patient_id):
    print(patient_id)
    patient=Patient.objects.filter(pk=patient_id)
    patient.delete()
    return redirect('allpatient')

def updateDoctorView(request,doctor_id):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        number=request.POST['number']
        email=request.POST['email']
        master=request.POST['master']
        username=request.POST['username']
        password=request.POST['password']

        print("Name- ",name)
        print("Address- ",address)
        print("Email- ",email)

        doctor=Doctor.objects.get(pk=doctor_id)
        doctor.name=name
        doctor.address=address
        doctor.number=number
        doctor.email=email
        doctor.master=master
        doctor.username=username
        doctor.password=password
        doctor.save()
    return redirect('alldoctor')

def updatePatientView(request,patient_id):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        number=request.POST['number']
        ailment=request.POST['ailment']
        email=request.POST['email']
        feedback=request.POST['feedback']

        print("Name- ",name)
        print("Address- ",address)
        print("Email- ",email)

        patient=Patient.objects.get(pk=patient_id)
        patient.name=name
        patient.address=address
        patient.number=number
        patient.ailment=ailment
        patient.email=email
        patient.feedback=feedback

        patient.save()
    return redirect('allpatient')

def singlePatientView(request,patient_id):
    patient=Patient.objects.get(pk=patient_id)
    context={
        'patient':patient
    }
    return render(request=request,template_name='singlepatient.html',context=context)

def updateSinglePatientView(request,patient_id):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        number=request.POST['number']
        ailment=request.POST['ailment']
        email=request.POST['email']
        feedback=request.POST['feedback']

        print("Name- ",name)
        print("Address- ",address)
        print("Email- ",email)

        patient=Patient.objects.get(pk=patient_id)
        patient.name=name
        patient.address=address
        patient.number=number
        patient.ailment=ailment
        patient.email=email
        patient.feedback=feedback

        patient.save()
        return redirect('doctor')

def deleteSinglePatientView(request,patient_id):
    print(patient_id)
    patient=Patient.objects.filter(pk=patient_id)
    patient.delete()
    return redirect('doctor')

def doctorSavePatientView(request):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        number=request.POST['number']
        ailment=request.POST['ailment']
        email=request.POST['email']
        feedback=request.POST['feedback']

        print("Name- ",name)
        print("Address- ",address)
        print("Email- ",email)

        patient=Patient(name=name,address=address,number=number,ailment=ailment,email=email,feedback=feedback)
        patient.save()
    return redirect('doctorregisterpatient')

def addDoctorPatientView(request):
    return render(request,'addDoctorPatient.html',{})    