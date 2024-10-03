from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method == "POST":
        uname = request.POST['name']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect('home')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('home')

def add_new_bug(request):
    if request.method == "POST":
        name = request.POST['name']
        project = request.POST['project']
        tester_code = request.POST['tester_code']
        bug_date = request.POST['bug_date']
        bug_level = request.POST['bug_level']
        bug_priority = request.POST['bug_priority']
        bug_type = request.POST['bug_type']
        status_name = request.POST['status_name']
        description = request.POST['description']
        proj_obj = Project.objects.get(id=project)
        creator = UserProfile.objects.get(user=request.user)
        bug = Bug.objects.create(title=name, description=description, project=proj_obj, creator=creator, status=status_name, bug_type=bug_type, created=bug_date, priority=bug_priority, bug_level=bug_level, tester_code=tester_code)
        messages.success(request, "Added Successfully")
        return redirect('bug_report')
    project = Project.objects.all()
    return render(request, 'add_new_bug.html', {'project': project, 'bug_type': BUGTYPE, 'bug_status': BUGSTATUS})

def add_new_project(request):
    if request.method == "POST":
        project_name = request.POST['project_name']
        project_duration = request.POST['project_duration']
        submission_date = request.POST['submission_date']
        client_name = request.POST['client_name']
        client_address = request.POST['client_address']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        department_name = request.POST['department_name']
        project_lead = request.POST['project_lead']
        description = request.POST['description']
        proj_lead = UserProfile.objects.get(id=project_lead)
        bug = Project.objects.create(name=project_name, description=description, submission_date=submission_date, duration=project_duration, client_name=client_name, client_address=client_address, phone_number=phone_number, email_id=email, department_name=department_name, project_lead=proj_lead)
        messages.success(request, "Added Successfully")
        return redirect('project_report')
    project = Project.objects.all()
    user = UserProfile.objects.all()
    return render(request, 'add_new_project.html', {'project': project, 'user': user})

def add_new_user(request):
    if request.method == "POST":
        userrole = request.POST['userrole']
        user_name = request.POST['user_name']
        # confirm = request.POST['confirm']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        file = request.FILES['file']
        address = request.POST['address']
        dob = request.POST['dob']
        user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, password=password, email=email)
        bug = UserProfile.objects.create(user=user, userrole=userrole, contact=phone_number, gender=gender, file=file, address=address, dob=dob)
        messages.success(request, "Added Successfully")
        return redirect('user_report')
    return render(request, 'add_new_user.html', {'userrole': USERROLE})

def bug_report(request):
    bug = Bug.objects.all()
    return render(request, 'bug_report.html', {'bug': bug})

def project_report(request):
    project = Project.objects.all()
    return render(request, 'project_report.html', {'project': project})


def user_report(request):
    user = UserProfile.objects.all()
    return render(request, 'user_report.html', {'user': user})

@login_required(login_url="login")
def Change_Password(request):
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Changed Successfully")
            logout(request)
            return redirect('home')
        else:
            messages.success(request, "Password not matching")
    return render(request, 'change_password.html')

def profile(request):
    data = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        userrole = request.POST['userrole']
        user_name = request.POST['user_name']
        # confirm = request.POST['confirm']
        # password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        address = request.POST['address']
        dob = request.POST['dob']
        user = User.objects.filter(username=user_name).update(first_name=first_name, last_name=last_name, email=email)
        bug = UserProfile.objects.filter(user=user).update(userrole=userrole, contact=phone_number, gender=gender, address=address, dob=dob)
        try:
            file = request.FILES['file']
            UserProfile.objects.filter(user=user).update(file=file)
        except:
            pass
        messages.success(request, "Updated Successfully")
        return redirect('profile')
    return render(request, 'profile.html', {'data': data, 'userrole': USERROLE})

def edit_user(request,pid):
    data = UserProfile.objects.get(id=pid)
    if request.method == "POST":
        userrole = request.POST['userrole']
        user_name = request.POST['user_name']
        # confirm = request.POST['confirm']
        # password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        address = request.POST['address']
        dob = request.POST['dob']
        user = User.objects.filter(username=user_name).update(first_name=first_name, last_name=last_name, email=email)
        bug = UserProfile.objects.filter(user=user).update(userrole=userrole, contact=phone_number, gender=gender, address=address, dob=dob)
        try:
            file = request.FILES['file']
            UserProfile.objects.filter(user=user).update(file=file)
        except:
            pass
        messages.success(request, "Updated Successfully")
        return redirect('user_report')
    return render(request, 'edit_user.html', {'data': data, 'userrole': USERROLE})

def delete_user(request, pid):
    data = UserProfile.objects.get(id=pid)
    data.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('user_report')

def edit_project(request,pid):
    data = Project.objects.get(id=pid)
    if request.method == "POST":
        project_name = request.POST['project_name']
        project_duration = request.POST['project_duration']
        submission_date = request.POST['submission_date']
        client_name = request.POST['client_name']
        client_address = request.POST['client_address']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        department_name = request.POST['department_name']
        project_lead = request.POST['project_lead']
        description = request.POST['description']

        proj_lead = UserProfile.objects.get(id=project_lead)
        bug = Project.objects.filter(id=pid).update(name=project_name, description=description, submission_date=submission_date,
                                     duration=project_duration, client_name=client_name, client_address=client_address,
                                     phone_number=phone_number, email_id=email, department_name=department_name,
                                     project_lead=proj_lead)
        messages.success(request, "Updated Successfully")
        return redirect('project_report')
    user = UserProfile.objects.all()
    return render(request, 'edit_project.html', {'data': data, 'user': user})

def delete_project(request, pid):
    data = Project.objects.get(id=pid)
    data.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('project_report')

def edit_bug(request,pid):
    data = Bug.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        project = request.POST['project']
        tester_code = request.POST['tester_code']
        bug_date = request.POST['bug_date']
        bug_level = request.POST['bug_level']
        bug_priority = request.POST['bug_priority']
        bug_type = request.POST['bug_type']
        status_name = request.POST['status_name']
        description = request.POST['description']
        proj_obj = Project.objects.get(id=project)
        creator = UserProfile.objects.get(user=request.user)
        bug = Bug.objects.filter(id=pid).update(title=name, description=description, project=proj_obj, creator=creator,
                                 status=status_name, bug_type=bug_type, created=bug_date, priority=bug_priority,
                                 bug_level=bug_level, tester_code=tester_code)

        messages.success(request, "Updated Successfully")
        return redirect('bug_report')
    project = Project.objects.all()
    return render(request, 'edit_bug.html', {'data': data, 'project': project, 'bug_type': BUGTYPE, 'bug_status': BUGSTATUS})

def delete_bug(request, pid):
    data = Bug.objects.get(id=pid)
    data.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('bug_report')

def bug_detail(request, pid):
    data = Bug.objects.get(id=pid)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        comment = Comment.objects.create(user=UserProfile.objects.get(user=request.user), title=title, message=description, bug=data)
        messages.success(request, "Comment Successfully")
        return redirect('bug_report')
    comment2 = Comment.objects.filter(bug=data)
    return render(request, 'bug_detail.html', {'data': data, 'comment': comment2})