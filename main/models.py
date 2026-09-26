import uuid
from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
    ('internship', 'Internship'),
    ('research', 'Research'),
    ('volunteer', 'Volunteer'),
    ('part-time', 'Part-Time'),
    ('full-time', 'Full-Time'),
    ('freelance', 'Freelance'),
    ('committee', 'Committee')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=30)
    npm = models.CharField(max_length=10)

    def __str__(self):
        return self.nama

class Skill(models.Model):
    SKILL_TYPES = (
        ('Software', 'Software Development'),
        ('Systems', 'Systems & Architecture'),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES)
    description = models.TextField()
    image_filename = models.CharField(max_length=200, help_text="Contoh: 'img/java_logo.png' atau 'image_127101.png'")
    starred_by = models.ManyToManyField(User, related_name="starred_skills", blank = True)

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )

    def __str__(self):
        return self.title
