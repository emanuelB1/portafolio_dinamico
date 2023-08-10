from django.db import models


class Profile(models.Model):
    # Campos para el perfil
    name = models.CharField(max_length=500)
    foto = models.ImageField(upload_to='profile_pictures/')
    descripcion = models.TextField()

    # Otros campos opcionales que podrían ser útiles
    age = models.PositiveIntegerField()
    email = models.EmailField()
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='proyectos/')
    enlace_pagina = models.URLField()
    enlace_github = models.URLField()

    def __str__(self):
        return self.nombre


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject
