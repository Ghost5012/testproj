from django.db import models

# Create your models here.
class Classe(models.Model):
    """creating the fields for the Classes table"""
    c_name=models.CharField(max_length=10)
    subj_list=models.CharField(max_length=50)
    num_of_students=models.IntegerField()

    def __str__(self):
        """returns informations about a class"""
        return '%s   has %s students'%(self.c_name,self.students)

class Students(models.Model):
    #creating the fields of the student tabble
    stud_mat=models.CharField(max_length=5)
    #stud_mat=models.ForeignKey(stud_mat,on_delete=models.CASCADE)
    stud_name=models.CharField(max_length=30)
    stud_surname=models.CharField(max_length=30)
    stud_dob=models.DateTimeField('birth date')
    stud_class=models.ForeignKey(Classe,on_delete=models.CASCADE)
    

    def __str__(self):
        """method called to display the informations of a student"""
        return '%s  %s  %s  %s'%(self.stud_mat,self.stud_name,self.stud_surname,self.stud_class)

class Marks(models.Model):
    stud=models.ForeignKey(Students,on_delete=models.CASCADE)
    subject=models.CharField(max_length=15)
    mark=models.FloatField()
