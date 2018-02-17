from django.shortcuts import render, get_object_or_404
from .models import Classe, Students
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
	class_list=Classe.objects.order_by('pk')
	context={'class_list':class_list}
	return render(request,'app1/index.html',context)


def class_info(request,classe_id):
	classe=get_object_or_404(Classe,pk=classe_id)
	subj_list=classe.subj_list.split(',')
	context={'classe':classe,'subj_list':subj_list}
	return render(request,'app1/class_info.html',context)
	
	
def registration(request,classe_id):
	salle=get_object_or_404(Classe,pk=classe_id)
	context={'salle':salle}
	return render(request,'app1/registration.html',context)

def save_registration(request,classe_id):
	salle=get_object_or_404(Classe,pk=classe_id)	#classe où enregistrer
	stud=Students(stud_mat=gen_mat(salle.c_name),stud_name=request.POST['nom'],stud_surname=request.POST['prenom'],stud_dob=request.POST['dob'],stud_class=salle)
	stud.save()
	#increments the number of students in the corresponding class
	salle.num_of_students+=1
	salle.save()
	context={'salle':salle}
	return render(request,'app1/registration.html',context)
	#HttpResponseRedirect(reverse('app1:registration',args=(classe_id,)))


def insert_marks(request,classe_id,subj):
	classe=get_object_or_404(Classe,pk=classe_id)
	context={'classe':classe,'subject':subj}
	return render(request,'app1/insert_marks.html',context)
	

~#def save_marks(request,+o)	
"""here are the funtions needed for the manipulation of the data"""
def gen_mat(classe):
	#this generates and returns the matricule of a student 
	stud_list=Students.objects.order_by('pk')
	numb=0
	for stud in stud_list:
		if stud.stud_mat[:2].upper()==classe[:2].upper():
			numb+=1
	return(classe[:2].upper()+str(numb+1))

