from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password, username, **kwargs):
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have a name')
        user = self.model(
            email=email,
            username=username,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, password, **kwargs):
        user = self.create_user(
            email=email,
            full_name=full_name,
            password=password,
            **kwargs
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=False)
    age = models.IntegerField(null=True, blank=True)
    birth_year = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    public_visibility = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return True

class Books(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    book = models.FileField(upload_to='books', null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title
