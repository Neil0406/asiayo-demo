from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta

class MemberAccountManager(BaseUserManager):
    """ Manager for user profiles """
    def new_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        return user
        
    def create_user(self, email, name, password, permission=None):
        """ Create a new user profile """
        user = self.new_user(email, name, password)
        user.save(using=self._db)
        
    def create_superuser(self, email, name, password):
        """ Create a new superuser profile """
        user = self.new_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def update_user(self, id_, email=None, name=None, password=None):
        """ Update user profile """
        email = self.normalize_email(email)
        user = MemberAccount.objects.get(id=id_)
        if password != None and password.strip() != '':
            user.password = password
            user.set_password(user.password)
        if email:
            user.email = email
        if name:
            user.name = name
        user.updated_at = datetime.now()
        user.save()
        
    def delete_user(self, user_id):
        user = MemberAccount.objects.get(id=user_id)
        if user.is_superuser != True:
            user.delete()
            
    def update_password(self, _id, password=None):
        user = MemberAccount.objects.get(id=_id)
        if password != None and password.strip() != "":
            user.password = password
            user.set_password(user.password)
            user.updated_at = datetime.now()
            user.save()
        return user.id
    
    
class MemberAccount(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True, verbose_name='帳號(Email)')
    name = models.CharField(max_length=255, verbose_name='姓名')
    is_staff = models.BooleanField(default=False, verbose_name='管理員')
    is_active = models.BooleanField(default=True, verbose_name='啟用帳號')
    is_superuser = models.BooleanField(default=False,  verbose_name='超級使用者')
    is_delete = models.BooleanField(default=False, verbose_name='軟刪除')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='建立日期')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    objects = MemberAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def __str__(self):
        """ Return string representation of our user """
        return self.email
    
