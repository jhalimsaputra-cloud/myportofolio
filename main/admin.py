from django.contrib import admin
from .models import Mahasiswa, Skill, Experience, Project

admin.site.register(Mahasiswa)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)