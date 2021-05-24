from django.db import models

# Create your models here.


class Master_Table(models.Model):
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    OTP = models.IntegerField()
    Role = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_updated = models.DateTimeField(auto_now_add=True)
    is_created = models.DateTimeField(auto_now_add=True)


class Employer(models.Model):
    m_id = models.ForeignKey(Master_Table, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contact = models.BigIntegerField(default="123")
    DOB = models.DateField(default="2020-12-01")
    Gender = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    profile_pic = models.ImageField(
        upload_to="img/",  default='/img/default-user.jpg')
    ver_doc = models.FileField(
        upload_to="ver_doc/",  default='/ver_doc/default.pdf')


class Candidate(models.Model):
    m_id = models.ForeignKey(Master_Table, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contact = models.BigIntegerField(default="123")
    DOB = models.DateField(default="2020-12-01")
    Gender = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    profile_pic = models.ImageField(
        upload_to="img/", default='/img/default-user.jpg')


class Company(models.Model):
    emp_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    Company_name = models.CharField(max_length=50)
    Company_address = models.CharField(max_length=50)
    Company_state = models.CharField(max_length=50)
    Founded = models.IntegerField(default="2001")
    Company_city = models.CharField(max_length=50)
    Company_contact = models.BigIntegerField(default="123")
    Company_Email = models.EmailField(max_length=50)
    Company_link = models.CharField(max_length=50)
    Company_desp = models.TextField(max_length=150)
    open_job = models.IntegerField(default="5")
    # job_name = models.CharField(max_length=50)
    Company_logo = models.ImageField(
        upload_to="img/", default='/img/default-user.jpg')


class Job(models.Model):
    comp_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    Job_title = models.CharField(max_length=50)
    Job_desp = models.TextField(max_length=500)
    Job_type = models.CharField(max_length=50)
    Job_category = models.CharField(max_length=50)
    Job_respon = models.TextField(max_length=500)
    Job_edu_exp = models.TextField(max_length=500)
    Job_benefit = models.TextField(max_length=500)
    Vacancy = models.IntegerField(default="5")
    Education = models.CharField(max_length=50)
    Experience = models.CharField(max_length=50)
    Job_loc = models.CharField(max_length=50)
    start_salary = models.CharField(max_length=50, default="5k")
    end_salary = models.CharField(max_length=50, default="8k")
    Gender = models.CharField(max_length=50, default="Any")
    App_deadline = models.DateField(default="2020-12-01")
    Published = models.DateField(auto_now_add=True)
