from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/images/category", null=True, blank=True)
    
    def __str__(self):
        return self.name

class User(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to="static/images/user", null=True, blank=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.fullname

class Region(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/images/region", null=True, blank=True)
    
    def __str__(self):
        return self.name

class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images/work", null=True, blank=True)
    video = models.FileField(upload_to="static/videos/work", max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class Application(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    price = models.IntegerField()
    duration = models.CharField(max_length=50)
    STATUS = (
        ("HIRED", "hired"),
        ("REJECTED", "rejected"),
        ("IN PROCESS", "in process")
    )
    status = models.CharField(choices=STATUS, max_length=50)
    created_on = models.DateTimeField(auto_now=True)
