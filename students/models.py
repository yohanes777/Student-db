# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Student(models.Model):

    class Meta(object):
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Ім'я")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Прізвище")

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name="По-батькові",
        default='')

    birthday = models.DateField(
        blank=False,
        verbose_name="Дата народження",
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name="Фото",
        null=True)

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Білет")


    notes = models.TextField(
        blank=True,
        verbose_name="Додатково")

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)



