from django.forms import ModelForm, TextInput, Textarea, URLInput, Select

from main.models import Project, Skill

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Skill


class SkillForm(ModelForm):
    class Meta:
        model = Skill

        fields = [
            "name",
            "skill_type",
            "description",
            "image_filename",
        ]

        labels = {
            "name": "Nama Skill",
            "skill_type": "Tipe Skill",
            "description": "Deskripsi Skill",
            "image_filename": "Nama File Gambar",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Java",
                    "maxlength": 100,
                }
            ),

            "skill_type": Select(),

            "description": Textarea(
                attrs={
                    "placeholder": "Jelaskan kemampuan atau pengalamanmu menggunakan skill ini",
                    "rows": 3,
                }
            ),

            "image_filename": TextInput(
                attrs={
                    "placeholder": "java.png",
                    "maxlength": 200,
                }
            ),
        }