from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=222)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class University(models.Model):
    name = models.CharField(max_length=111)
    rektor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=222)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=111)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=111)
    mudir = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()
    kafedra = models.ForeignKey(Kafedra, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    name = models.CharField(max_length=33)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    name = models.CharField(max_length=111)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
