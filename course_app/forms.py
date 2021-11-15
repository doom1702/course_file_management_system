from course_app.models import Dep_File, File, Ict_File, Qb_File, Rubrics_File, Sylab_File, Uni_Exam_File
from django import forms

class MyFileUploaded(forms.ModelForm):
    class Meta():
        model = File
        fields = ['file_name','file_link']

class Dep_File_Upload(forms.ModelForm):
    class Meta():
        model = Dep_File
        fields = ['file_name','file_link']

class Syllab_File_Upload(forms.ModelForm):
    class Meta():
        model = Sylab_File
        fields = ['file_name','file_link']

class Rubrics_File_Upload(forms.ModelForm):
    class Meta():
        model = Rubrics_File
        fields = ['file_name','file_link']

class Uni_Exam_File_Upload(forms.ModelForm):
    class Meta():
        model = Uni_Exam_File
        fields = ['file_name','file_link']

class ICT_File_Upload(forms.ModelForm):
    class Meta():
        model = Ict_File
        fields = ['file_name','file_link']

class Qb_File_Upload(forms.ModelForm):
    class Meta():
        model = Qb_File
        fields = ['file_name','file_link']
