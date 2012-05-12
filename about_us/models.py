# -*- coding: utf-8 -*-
from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["role_name"]
    
    def __unicode__(self):
        return "%s".strip() % self.role_name


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)
    roles = models.ManyToManyField(Role)
    
    class Meta:
        ordering = ["first_name"]
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        
    def __unicode__(self):
        return "%s %s".strip() % (self.first_name, self.last_name)