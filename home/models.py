# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Area(models.Model):

    #__Area_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    alias = models.CharField(max_length=255, null=True, blank=True)
    observacion = models.CharField(max_length=255, null=True, blank=True)

    #__Area_FIELDS__END

    class Meta:
        verbose_name        = _("Area")
        verbose_name_plural = _("Area")


class Mesa_Ayuda(models.Model):

    #__Mesa_Ayuda_FIELDS__
    nombre_mesa = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

    #__Mesa_Ayuda_FIELDS__END

    class Meta:
        verbose_name        = _("Mesa_Ayuda")
        verbose_name_plural = _("Mesa_Ayuda")


class Servicio(models.Model):

    #__Servicio_FIELDS__
    nombre_servicio = models.CharField(max_length=255, null=True, blank=True)

    #__Servicio_FIELDS__END

    class Meta:
        verbose_name        = _("Servicio")
        verbose_name_plural = _("Servicio")


class Atencion(models.Model):

    #__Atencion_FIELDS__
    estado_atencion = models.CharField(max_length=255, null=True, blank=True)
    estado_llamado = models.CharField(max_length=255, null=True, blank=True)

    #__Atencion_FIELDS__END

    class Meta:
        verbose_name        = _("Atencion")
        verbose_name_plural = _("Atencion")


class Ticket(models.Model):

    #__Ticket_FIELDS__
    serie = models.CharField(max_length=255, null=True, blank=True)

    #__Ticket_FIELDS__END

    class Meta:
        verbose_name        = _("Ticket")
        verbose_name_plural = _("Ticket")


class Cliente(models.Model):

    #__Cliente_FIELDS__
    documento = models.CharField(max_length=255, null=True, blank=True)
    es_titular = models.CharField(max_length=255, null=True, blank=True)

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")


class Sucursal(models.Model):

    #__Sucursal_FIELDS__
    nombre_sucursal = models.CharField(max_length=255, null=True, blank=True)

    #__Sucursal_FIELDS__END

    class Meta:
        verbose_name        = _("Sucursal")
        verbose_name_plural = _("Sucursal")


class Usuario(models.Model):

    #__Usuario_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellido = models.CharField(max_length=255, null=True, blank=True)
    correo = models.CharField(max_length=255, null=True, blank=True)

    #__Usuario_FIELDS__END

    class Meta:
        verbose_name        = _("Usuario")
        verbose_name_plural = _("Usuario")



#__MODELS__END
