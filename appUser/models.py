from django.db import models
from django.contrib.auth.models import User




class Userinfo(models.Model):
   user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   tel = models.CharField(("Telefon"), max_length=50, default="", blank=True) 
   
   def __str__(self) -> str:
      return self.user.username
   

class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   title = models.CharField(("Başlık"), max_length=50)
   image = models.ImageField(("Profile Resmi"), upload_to="profile", max_length=250)
   isview = models.BooleanField(("Görüntüle"), default=True)
   isnew = models.BooleanField(("Silinen Yeni Profil Mi"), default=False) # yeni profil olup olmadığını anlamızı sağlıcak
   islogin = models.BooleanField(("Girişli Profil"), default=False)
  
   def __str__(self) -> str:
      return self.title
   
class Emailmessage(models.Model):
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("Mesaj"))
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
   
   def __str__(self) -> str:
      return self.title
   
   
class Category(models.Model):
   title = models.CharField(("Kategori adı"), max_length=50)
   slug=models.SlugField(max_length=50,null=True,unique=True)
   
   def __str__(self) -> str:
      return self.title
      
class Video(models.Model):
   title = models.CharField(("Başlık"), max_length=50)
   image = models.ImageField(("Dizi Film Resim"), upload_to="Video", max_length=250)
   Category=models.ForeignKey(Category, on_delete=models.CASCADE)
   content = models.DateTimeField(auto_now_add=True)
   profilsec=models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True)


    
   def __str__(self) -> str:
      return self.title