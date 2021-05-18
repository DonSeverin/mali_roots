from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser, update_last_login )

class AccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address.')
        if not first_name:
            raise ValueError('Users must have an First_Name address.')
        if not last_name:
            raise ValueError('Users must have an Last_Name address.')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password=password,
        )
        user.is_admin     = True
        user.is_staff     = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
class Account(AbstractBaseUser):
    email        = models.EmailField(verbose_name='email', max_length=60, unique=True, primary_key=True)
    first_name   = models.CharField(max_length=60)
    last_name    = models.CharField(max_length=60)
    date_joined  = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login   = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_admin     = models.BooleanField(default=False) 
    is_staff     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    hide_email   = models.BooleanField(default=True)

    objects = AccountManager()

    ordering = ('email')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 'last_name',
    ]

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True    
    
class User(models.Model):
    account    = models.OneToOneField(Account, null=True, blank=True, on_delete=models.CASCADE) 
    
    name       = models.CharField(max_length=60, default='NULL')
    lastname   = models.CharField(max_length=60, default='NULL')
    phone      = models.IntegerField(default= 0)
    address    = models.CharField(max_length=150, default='NULL')
    birth_date = models.DateField(default='1994-05-14')

class Call(models.Model):
    User       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )
  
    phone      = models.IntegerField(default= 0)
    duration   = models.TimeField(default='08:00')
    dateTime   = models.DateField(default='1994-05-14')
    menuOption = models.CharField(max_length=256, default='NULL')
    latitude   = models.FloatField(default= 0)
    longditude = models.FloatField(default= 0)

class Menuoptions(models.Model):
    call                    = models.ForeignKey(Call, on_delete=models.SET_NULL, null=True, blank=True )

    treeSelection           = models.CharField(max_length=256, default='NULL')
    seedsConfirmation       = models.BooleanField(default=False, null=True, blank=True)
    contactingpermission    = models.BooleanField(default=False, null=True, blank=True)
    triangulationPermission = models.BooleanField(default=False, null=True, blank=True)    

class Seed(models.Model):
    name     = models.CharField(max_length=256, default='NULL')
    location = models.CharField(max_length=256, default='NULL')

class Tree(models.Model):
    tree       = models.ForeignKey(Seed, on_delete=models.SET_NULL, null=True, blank=True, default='NULL' )
    User       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default='NULL')

    name       = models.CharField(max_length=256, default='NULL')
    age        = models.CharField(max_length=256, default='NULL')
    endangered = models.BooleanField(default=False, null=True, blank=True)
    seeds      = models.BooleanField(default=False, null=True, blank=True)
