from django.urls import path
from . import views

urlpatterns = [
    path(route= 'login', view= views.loginPageView, name='login'),
    path(route="check",view=views.checkStaffView,name='check'),
    path(route="adddoctor",view=views.addDoctorView,name='registerdoctor'),
    path(route="addpatient",view=views.addPatientView,name='registerpatient'),
    path(route="doctorsave",view=views.saveDoctorView,name='doctorsave'),
    path(route="patientsave",view=views.savePatientView,name='patientsave'),
    path(route="alldoctor",view=views.getallDoctors,name='alldoctor'),
    path(route="allpatient",view=views.getallPatients,name='allpatient'),
    path(route="deletedoc/<int:doctor_id>",view=views.deleteDoctorView,name='deletedoctor'),
    path(route="deletepa/<int:patient_id>",view=views.deletePatientView,name='deletepatient'),
    path(route="updatedoc/<int:doctor_id>",view=views.updateDoctorView,name='updatedoctor'),
    path(route="updatepa/<int:patient_id>",view=views.updatePatientView,name='updatepatient'),
    path(route= 'admin', view= views.adminPageView, name='admin'),
    path(route="<int:patient_id>",view=views.singlePatientView,name='getsinglepatient'),
    path(route="singleupdatepa/<int:patient_id>",view=views.updateSinglePatientView,name='updatesinglepatient'),
    path(route="singledeletepa/<int:patient_id>",view=views.deleteSinglePatientView,name='deletesinglepatient'),
    path(route= 'doctor', view= views.doctorPageView, name='doctor'),
    path(route="doctorpatientsave",view=views.doctorSavePatientView,name='doctorSavePatient'),
    path(route="adddoctorpatient",view=views.addDoctorPatientView,name='doctorregisterpatient'),
]