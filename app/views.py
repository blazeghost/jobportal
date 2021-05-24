from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
# HttpResponseRedirect, reverse
from .models import *
from random import randint

# Create your views here.


def IndexPage(request):
    return render(request, "app/index.html")


def EmployerIndex(request):
    return render(request, "app/employer/index.html")


def FaqPage(request):
    return render(request, "app/faq.html")


def RegisterUser(request):
    if request.POST['role'] == "Employer":
        fname = request.POST['fname']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        cpass = request.POST['cpass']
        user = Master_Table.objects.filter(Email=email)
        if user:
            message = "User is already exist"
            return render(request, "app/base1.html", {'msg': message})

        else:
            if password == cpass:
                otp = randint(100000, 999999)
                masteruser = Master_Table.objects.create(
                    Email=email, Password=password, OTP=otp, Role=role)
                newemp = Employer.objects.create(
                    m_id=masteruser, Firstname=fname)
                return render(request, "app/index-2.html")

            else:
                message = "Password and CPassword doesnot match"
                return render(request, "app/base1.html", {'msg': message})

    else:

        if request.POST['role'] == "Candidate":
            fname = request.POST['fname']
            email = request.POST['email']
            password = request.POST['password']
            role = request.POST['role']
            cpass = request.POST['cpass']
            user = Master_Table.objects.filter(Email=email)
            if user:
                message = "User is already exist"
                return render(request, "app/base1.html", {'msg': message})

            else:
                if password == cpass:
                    otp = randint(100000, 999999)
                    masteruser = Master_Table.objects.create(
                        Email=email, Password=password, OTP=otp, Role=role)
                    newcand = Candidate.objects.create(
                        m_id=masteruser, Firstname=fname)
                    return render(request, "app/index-2.html")

                else:
                    message = "Password and CPassword doesnot match"
                    return render(request, "app/base1.html", {'msg': message})


def LoginUser(request):
    if request.POST['role'] == "Employer":
        email = request.POST['email']
        password = request.POST['password']

        user = Master_Table.objects.get(Email=email)

        if user:
            if user.Password == password and user.Role == "Employer":
                emp = Employer.objects.get(m_id=user)

                request.session['Role'] = user.Role
                request.session['id'] = user.id
                request.session['Firstname'] = emp.Firstname
                request.session['Email'] = user.Email

                return render(request, "app/employer/index.html")

            else:
                message = "User Password or Role Doesnot match"
                return render(request, "app/base1.html", {'msg': message})

        else:
            message = "User not Found"
            return render(request, "app/base1.html", {'msg': message})

    else:
        if request.POST['role'] == "Candidate":
            email = request.POST['email']
            password = request.POST['password']

            user = Master_Table.objects.get(Email=email)

            if user:
                if user.Password == password and user.Role == "Candidate":
                    cand = Candidate.objects.get(m_id=user)

                    request.session['Role'] = user.Role
                    request.session['id'] = user.id
                    request.session['Firstname'] = cand.Firstname
                    request.session['Email'] = user.Email

                    return render(request, "app/index-2.html")

                else:
                    message = "User Password or Role Doesnot match"
                    return render(request, "app/base1.html", {'msg': message})

            else:
                message = "User not Found"
                return render(request, "app/base1.html", {'msg': message})


def ProfilePage(request, pk):
    udata = Master_Table.objects.get(id=pk)
    if udata.Role == "Employer":
        emp = Employer.objects.get(m_id=udata)
        request.session['Email'] = udata.Email
        return render(request, "app/employer/emp_profile.html", {'key1': emp})
    else:
        if udata.Role == "Candidate":
            emp = Candidate.objects.get(m_id=udata)
            request.session['Email'] = udata.Email
            return render(request, "app/profile.html", {'key1': emp})


def UpdateProfile(request, pk):
    udata = Master_Table.objects.get(id=pk)

    if udata.Role == "Employer":
        emp = Employer.objects.get(m_id=udata)
        emp.Firstname = request.POST['fname']
        emp.Lastname = request.POST['lname']
        emp.City = request.POST['city']
        emp.State = request.POST['state']
        emp.Contact = request.POST['contact']
        # emp.DOB = request.POST['dob']
        emp.profile_pic = request.FILES['img']
        emp.Gender = request.POST['gender']
        emp.ver_doc = request.FILES['verdoc']
        print('Gender--------------->', emp.Gender)
        emp.save()
        url = f"/profilepage/{pk}"
        return redirect(url)
    else:
        if udata.Role == "Candidate":
            cand = Candidate.objects.get(m_id=udata)
            cand.Firstname = request.POST['fname']
            cand.Lastname = request.POST['lname']
            cand.City = request.POST['city']
            cand.State = request.POST['state']
            cand.Contact = request.POST['contact']
            cand.DOB = request.POST['dob']
            cand.profile_pic = request.FILES['img']
            cand.gender = request.POST['gender']
            cand.save()
            url = f"/profilepage/{pk}"
            return redirect(url)


def AddCompanyPage(request, pk):
    test = Company.objects.filter(emp_id=pk)
    if test:
        # If there is data(Company) in Database

        mdata = Master_Table.objects.get(id=pk)
        if mdata.Role == "Employer":
            e_id = Employer.objects.get(m_id=mdata)
            comp = Company.objects.get(emp_id=e_id)
            return render(request, "app/employer/addcompany.html", {'key1': comp})
    else:

        return render(request, "app/employer/addcompany.html")


def AddCompanyData(request, pk):
    mdata = Master_Table.objects.get(id=pk)
    test = Company.objects.filter(emp_id=pk)
    if test:
        # If there is data(Company) in Database

        mdata = Master_Table.objects.get(id=pk)
        if mdata.Role == "Employer":
            e_id = Employer.objects.get(m_id=mdata)
            comp = Company.objects.get(emp_id=e_id)
            comp.Company_name = request.POST['compname']
            comp.Company_address = request.POST['compaddress']
            comp.Company_Email = request.POST['compemail']
            comp.Company_contact = request.POST['compcontact']
            comp.Company_city = request.POST['compcity']
            comp.Company_state = request.POST['compstate']
            comp.Company_link = request.POST['weblink']
            comp.open_job = request.POST['openjob']
            comp.Founded = request.POST['founded']
            # comp.Company_logo = request.FILES['logo']
            comp.Company_desp = request.POST['description']
            comp.save()
            message = "Company Successfully Added"
            url = f"/addcompanypage/{pk}"
            return redirect(url)
    else:
        # print("--------------------> Fail")
        if mdata.Role == "Employer":
            e_id = Employer.objects.get(m_id=mdata)
            compname = request.POST['compname']
            compaddress = request.POST['compaddress']
            compemail = request.POST['compemail']
            compcontact = request.POST['compcontact']
            compcity = request.POST['compcity']
            compstate = request.POST['compstate']
            weblink = request.POST['weblink']
            openjob = request.POST['openjob']
            founded = request.POST['founded']
            logo = request.FILES['logo']
            description = request.POST['description']

            newcomp = Company.objects.create(emp_id=e_id,
                                             Company_name=compname, Company_address=compaddress, Company_Email=compemail, Company_contact=compcontact,
                                             Company_city=compcity, Company_state=compstate, Company_link=weblink,
                                             open_job=openjob, Founded=founded, Company_logo=logo, Company_desp=description)

            message = "Company Successfully Added"
            url = f"/addcompanypage/{pk}"
            return redirect(url)
            # return render(request, "app/employer/addcompany.html", {'msg': message})


def CompanyList(request):
    all_data = Company.objects.all()
    return render(request, "app/company-list.html", {'key1': all_data})


def EmpCompanyList(request):
    all_data = Company.objects.all()
    return render(request, "app/employer/company-list.html", {'key1': all_data})


def CompanySingle(request, pk):
    cdata = Company.objects.get(id=pk)
    return render(request, "app/company-single.html", {'key1': cdata})


def EmpCompanySingle(request, pk):
    cdata = Company.objects.get(id=pk)
    return render(request, "app/employer/company-single.html", {'key1': cdata})


def PostJobPage(request):
    return render(request, "app/employer/post-job.html")


def PostJobData(request, pk):
    mdata = Master_Table.objects.get(id=pk)
    if mdata.Role == "Employer":
        emp = Employer.objects.get(m_id=mdata)
        comp = Company.objects.get(emp_id=emp)
        # print("Company Id 1------------------->", comp)

        jobtitle = request.POST['jobtitle']
        appdeadline = request.POST['app_deadline']
        jobtype = request.POST['jobtype']
        jobcategory = request.POST['jobcategory']
        salarystart = request.POST['salarystart']
        salaryend = request.POST['salaryend']
        gender = request.POST['jobgender']
        experience = request.POST['experience']
        education = request.POST['education']
        joblocation = request.POST['joblocation']
        vacancy = request.POST['vacancy']
        jobdesp = request.POST['jobdesp']
        jobrespon = request.POST['jobrespon']
        jobeduexp = request.POST['jobeduexp']
        jobbenedits = request.POST['jobbenedits']

        newjob = Job.objects.create(comp_id=comp, Job_title=jobtitle, Job_desp=jobdesp,
                                    Job_type=jobtype, Job_category=jobcategory, Job_respon=jobrespon,
                                    Job_edu_exp=jobeduexp, Job_benefit=jobbenedits, Vacancy=vacancy,
                                    Education=education, Experience=experience, Job_loc=joblocation,
                                    start_salary=salarystart, end_salary=salaryend, Gender=gender,
                                    App_deadline=appdeadline)

        message = "Job Successfully Added"
        return render(request, "app/employer/post-job.html", {'msg': message})


def JobListPage(request):
    job_data = Job.objects.all()
    return render(request, "app/job-list.html", {"job_data": job_data})


def EmpJobListPage(request):
    job_data = Job.objects.all()
    return render(request, "app/employer/job-list.html", {"job_data": job_data})


def JobSingle(request, pk):
    job_data = Job.objects.get(id=pk)
    return render(request, "app/job-single.html", {"job_data": job_data})


def EmpJobSingle(request, pk):
    job_data = Job.objects.get(id=pk)
    return render(request, "app/employer/job-single.html", {"job_data": job_data})


def EmpMyJobList(request):
    job_data = Job.objects.all()
    return render(request, "app/employer/myjob-list.html", {"job_data": job_data})


def AdminLogin(request):
    return render(request, "app/admin/login.html")


def AdminLoginCheck(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":
        request.session['username'] = username
        request.session['password'] = password
        return render(request, "app/admin/index.html")
    else:
        message = "Username or Password doesnot match"
        return render(request, "app/admin/login.html", {'msg': message})


def Cand_Logout(request):
    # user = Master_Table.objects.get(id=pk)
    # cand = Candidate.objects.get(m_id=user)

    del request.session['Role']
    del request.session['id']
    del request.session['Firstname']
    del request.session['Email']

    return render(request, "app/index.html")


def Emp_Logout(request):
    # user = Master_Table.objects.get(id=pk)
    # emp = Employer.objects.get(m_id=user)

    del request.session['Role']
    del request.session['id']
    del request.session['Firstname']
    del request.session['Email']

    return render(request, "app/index.html")


def Admin_Logout(request):

    del request.session['username']
    del request.session['password']

    return render(request, "app/index.html")


def Admin_Emp_List(request):

    emp_data = Employer.objects.all()

    return render(request, "app/admin/employer-list.html", {'key_emp': emp_data})


def Emp_CheckPage(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    emp_data = Employer.objects.get(m_id=m_data)
    return render(request, "app/admin/emp-check.html", {'key_emp': emp_data})


def Emp_Check(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    # emp_data = Employer.objects.get(m_id=m_data)

    m_data.is_verified = request.POST['is_verified']
    m_data.is_active = request.POST['is_active']

    # print("----------->>>>", emp_data.m_id.is_verified)
    # print("----------->>>>", emp_data.m_id.is_active)
    # emp_data.save()
    m_data.save()

    url = f"/emp-checkpage/{pk}"
    return redirect(url)


def EmpDelete(request, pk):
    m_data = Master_Table.objects.get(id=pk)
    m_data.delete()
    return HttpResponseRedirect(reverse('admin-emp-list'))

# m_data = Master_Table.objects.all()
#         emp_data = Employer.objects.all()
#         cand_data = Candidate.objects.all()
#         comp_data = Company.objects.all()

# {'key_master': m_data, 'key_emp': emp_data, 'key_cand': cand_data, 'key_comp': comp_data}
