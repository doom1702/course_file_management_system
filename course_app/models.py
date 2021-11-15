from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class File(models.Model):
    # When user is deleted The file too is deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_link = models.FileField(upload_to='vision/')

    def __str__(self):
        return self.file_name

    def delete(self, *args, **kwargs):
        self.file_link.delete()
        super().delete(*args, **kwargs)  
        


class Dep_File(models.Model):
    # When user is deleted The file too is deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_link = models.FileField(upload_to='department/')

    def __str__(self):
        return self.file_name
    
    def delete(self, *args, **kwargs):
        self.file_link.delete()
        super().delete(*args, **kwargs) 

class Sylab_File(models.Model):
    # When user is deleted The file too is deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_link = models.FileField(upload_to='syllabus/')

    def __str__(self):
        return self.file_name

    def delete(self, *args, **kwargs):
        self.file_link.delete()
        super().delete(*args, **kwargs) 

class Rubrics_File(models.Model):
    # When user is deleted The file too is deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_link = models.FileField(upload_to='rubrics/')

    def __str__(self):
        return self.file_name

    def delete(self, *args, **kwargs):
        self.file_link.delete()
        super().delete(*args, **kwargs) 

class Uni_Exam_File(models.Model):
    # When user is deleted The file too is deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_link = models.FileField(upload_to='uni_exam/')

    def __str__(self):
        return self.file_name

    def delete(self, *args, **kwargs):
        self.file_link.delete()
        super().delete(*args, **kwargs) 

class Ict_File(models.Model):
    # When user is deleted The file too is deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_link = models.FileField(upload_to='ict/')

    def __str__(self):
        return self.file_name

    def delete(self, *args, **kwargs):
        self.file_link.delete()
        super().delete(*args, **kwargs) 

class Qb_File(models.Model):
    # When user is deleted The file too is deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_link = models.FileField(upload_to='question_bank/')

    def __str__(self):
        return self.file_name

    def delete(self, *args, **kwargs):
        self.file_link.delete()
        super().delete(*args, **kwargs) 