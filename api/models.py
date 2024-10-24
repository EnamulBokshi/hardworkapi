from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField
import shortuuid

#User Table
class User(AbstractUser):
    username = models.CharField(unique=True,max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def save(self,*args,**kwargs):
        email_sername,mobile = self.email.split("@")
        
        if self.full_name == '' or self.full_name == None:
            self.full_name = email_sername
        if self.username == '' or self.username == None:
            self.username = email_sername
        super(User,self).save(*args,**kwargs)
#User Profile Table
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.FileField(upload_to="image",default='default/user.png',null=True,blank=True)
    full_name = models.CharField(max_length=100,null=True,blank=True)
    bio = models.CharField(max_length = 100,null=True,blank=True)
    about = models.CharField(max_length = 100,null=True,blank=True)
    author = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    def save(self,*args,**kwargs):
        if self.full_name == '' or self.full_name == None:
            self.full_name = self.user.full_name
        super(Profile,self).save(*args,**kwargs)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)

def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)


# Post Table
class Post(models.Model):
    STATUS = (
        ('Active','Active'),
        ('Draft','Draft'),
        ('Disabled','Disabled'),
        ('Featured','Featured')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    tags = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='image/post',null=True,blank=True)
    status = models.CharField(choices=STATUS,max_length=100,default='Active')
    slug = models.SlugField(unique=True, null=True, blank=True)
    view = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Post'
    
    def save(self,*args, **kwargs):
        if self.slug == '' or self.slug == None:
            self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)

# class Candidates(models.Model):

class Gallery(models.Model):
    STATUS = (
        ('Active','Active'),
        ('Deactive','Deactive')
    )
    image = models.FileField(upload_to='Gallery',null=False,blank=False)
    status = models.CharField(choices=STATUS,default="Active",max_length=100)
    title = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.status
    
    def save(self,*args, **kwargs):
        if self.title == '' or self.title == None:
            self.title = 'Gallery_Item'
        if self.image:
            super(Gallery,self).save(*args, **kwargs)

class Quote(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,blank = True, null=True)
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return  self.name
    def save(self,*args, **kwargs):
        super(Quote,self).save(*args, **kwargs)
