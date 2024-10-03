from django.db import models
from django.contrib.auth.models import User

# Create your models here.
USERROLE = ((1, "Manager"), (2, "Tester"), (3, "Developer"), (4, 'Admin'))

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    userrole = models.IntegerField(choices=USERROLE, null=True, blank=True, default=0)
    contact = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    submission_date = models.DateTimeField(null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    client_name = models.CharField(max_length=200, null=True, blank=True)
    client_address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    email_id = models.CharField(max_length=200, null=True, blank=True)
    department_name = models.CharField(max_length=200, null=True, blank=True)
    project_lead = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='project_lead')
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

BUGSTATUS = ((1, 'Open'), (2, 'Close'), (3, 'In Progress'))
BUGTYPE = ((1, 'High Priority'), (2, 'Low Priority'), (3, 'Information'))
class Bug(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='project')
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='creator')
    assign_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='assign_by')
    assign_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='assign_to')
    title = models.CharField(max_length=200, null=True, blank=True)
    priority = models.CharField(max_length=200, null=True, blank=True)
    bug_level = models.CharField(max_length=200, null=True, blank=True)
    tester_code = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=BUGSTATUS, null=True, blank=True, default=0)
    bug_type = models.IntegerField(choices=BUGTYPE, null=True, blank=True, default=0)
    file = models.FileField(null=True, blank=True)
    created = models.DateTimeField(null=True, auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.bug.title