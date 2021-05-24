from django.urls import path, include
from . import views

urlpatterns = [
    # Page URLS
    path("", views.IndexPage, name="index"),
    path("employerindex/", views.EmployerIndex, name="employerindex"),
    path("faq/", views.FaqPage, name="FAQ"),
    path("profilepage/<int:pk>", views.ProfilePage, name="profilepage"),
    path("addcompanypage/<int:pk>", views.AddCompanyPage, name='addcompanypage'),
    path("companylist/", views.CompanyList, name='companylist'),
    path("empcompanylist/", views.EmpCompanyList, name='empcompanylist'),
    path("postjobpage/", views.PostJobPage, name='postjobpage'),
    path("joblistpage/", views.JobListPage, name='joblistpage'),
    path("empjoblistpage/", views.EmpJobListPage, name='empjoblistpage'),
    path("empmyjoblist/", views.EmpMyJobList, name='empmyjoblist'),
    path("admin-login/", views.AdminLogin, name="admin-login"),






    # Functionality URLS
    path('registeruser/', views.RegisterUser, name="register"),
    path('loginuser/', views.LoginUser, name="login"),
    path('updateprofile/<int:pk>', views.UpdateProfile, name="updateprofile"),
    path("addcompanydata/<int:pk>", views.AddCompanyData, name='addcompanydata'),
    path("companysingle/<int:pk>", views.CompanySingle, name='companysingle'),
    path("empcompanysingle/<int:pk>",
         views.EmpCompanySingle, name='empcompanysingle'),
    path("postjobdata/<int:pk>", views.PostJobData, name="postjobdata"),
    path("jobsingle/<int:pk>", views.JobSingle, name="jobsingle"),
    path("empjobsingle/<int:pk>", views.EmpJobSingle, name="empjobsingle"),
    path('admin-login-check/', views.AdminLoginCheck, name="admin-login-check"),
    path("cand-logout/", views.Cand_Logout, name="cand-logout"),
    path("emp-logout/", views.Emp_Logout, name="emp-logout"),
    path("admin-logout/", views.Admin_Logout, name="admin-logout"),
    path("admin-emp-list/", views.Admin_Emp_List, name="admin-emp-list"),
    path('emp-checkpage/<int:pk>', views.Emp_CheckPage, name="emp-checkpage"),
    path("emp-check/<int:pk>", views.Emp_Check, name="emp-check"),
    path("emp-delete/<int:pk>", views.EmpDelete, name="emp-delete"),




]
