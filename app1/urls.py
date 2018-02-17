from django.urls import path, include
from . import views
app_name='app1'
urlpatterns=[
	path('',views.index,name='index'),	
	path('<int:classe_id>/registration/',views.registration,name='registration'),
	path('<int:classe_id>/save_registration/',views.save_registration,name='save'),
	path('<int:classe_id>/class_info/',views.class_info,name='class_info'),
	path('<int:classe_id>,<str:subj>/insert_marks/',views.insert_marks,name='marks'),
]
