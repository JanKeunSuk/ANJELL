from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
    , Permission)
from django.conf import settings




class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an user name')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,
            password=password,
            email=self.normalize_email(email)
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
     
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
    )
    username=models.CharField(max_length=40,unique=True)
    user_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    direccion=models.CharField(max_length=255)
    
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return self.user_name+self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.user_name

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
    
    
    
class rol(models.Model):

    #aca va a habr problemas para relacionar con permisos
    #le puse many to many porque en realidad el foreign key tiene que estar en la otra tabla
    ROL_CHOICES = (
        ("SIS", 'Sistema'),
        ('PRO', 'Proyecto'),
    )
    
    rol_id = models.AutoField(primary_key=True)
    permisos= models.ManyToManyField(Permission)
    nombre_rol_id = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 200)
    tipo = models.CharField(max_length = 3, choices = ROL_CHOICES)
    
    
class proyecto(models.Model):
    ESTADO_CHOICES = (
        ('PEN', 'Pendiente'),
        ('ACT', 'Activo'),
        ('ANU', 'Anulado'),
        ('FIN', 'Finalizado'),
    )
    
    proyecto_id = models.AutoField(primary_key=True)
    nombre_corto = models.CharField(max_length = 200)
    nombre_largo = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 200)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length = 3, choices = ESTADO_CHOICES)
    
class Sprint(models.Model):
    
    ESTADO_CHOICES = (
        ('CAN', 'Cancelado'),
        ('ACT', 'Activo'),
        ('CON', 'Consulta'),
    )
     
    Sprint_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 200)
    #HU se referencia desde el modelo HU
    fecha_inicio = models.DateTimeField()
    duracion = models.FloatField()
    estado = models.CharField(max_length = 3, choices = ESTADO_CHOICES)
    

    
    
class Flujo(models.Model):
    
    ESTADO_CHOICES = (
        ('CAN', 'Cancelado'),
        ('ACT', 'Activo'),
    )
     
    Flujo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 200)
    estado = models.CharField(max_length = 3, choices = ESTADO_CHOICES)




class HU(models.Model):
    VALORES100_CHOICES = zip( range(1,100), range(1,100) )
    VALORES10_CHOICES = zip( range(1,10), range(1,100) )

    ESTADO_CHOICES = (
        ('CAN', 'Cancelado'),
        ('ACT', 'Activo'),
    )
     
    HU_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length = 200)
    valor_negocio = models.IntegerField(choices = VALORES10_CHOICES)
    valor_tecnico = models.IntegerField(choices = VALORES10_CHOICES)
    prioridad = models.IntegerField(choices = VALORES100_CHOICES)
    duracion = models.FloatField()
    acumulador_horas = models.FloatField()
    estado = models.CharField(max_length = 3, choices = ESTADO_CHOICES)
    kanban=models.ForeignKey(Flujo)
    sprint=models.ForeignKey(Sprint)
    proyecto=models.ForeignKey(proyecto)
    
    
class Actividad(models.Model):
    Actividad_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 200)
    #cada Actividad referancia a su respectivo FLujo
    flujo=models.ForeignKey(Flujo)
    #pendiente
    #en_progreso
    #finalizado
    
class asignacion(models.Model):
    asignation_id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(settings.AUTH_USER_MODEL)
    rol=models.ForeignKey(rol)
    proyecto=models.ForeignKey(proyecto)
    HU=models.ForeignKey(HU)
    
    
    

    
    
    
    