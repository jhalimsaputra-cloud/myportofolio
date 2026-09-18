from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Mahasiswa, Skill, Project
from main.forms import ProjectForm, SkillForm


def show_main(request):
    context = {
        "name": "Justin Evan Halim Saputra",
        "npm": "2506549386",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student navigating life between clean code and endless debugging. Fueled by good tea, billiard, and continuous learning. Just building cool things one commit at a time."
        ),
        "mahasiswa_list": Mahasiswa.objects.all()
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Justin Evan Halim Saputra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Justin Evan Halim Saputra"
    }
    return render(request, "education.html", context)

def create_skill(request):
    form = SkillForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skills")

    context = {
        "name": "Justin Evan Halim Saputra",
        "form": form,
    }

    return render(request, "skills_form.html", context)

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")

    return redirect("main:show_skills")

def update_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    form = SkillForm(
        request.POST or None,
        instance=skill
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill berhasil diperbarui!")
        return redirect("main:show_skills")

    context = {
        "name": "Justin Evan Halim Saputra",
        "form": form,
        "skill": skill,
    }

    return render(request, "skills_form.html", context)

def get_skills_json(request):
    name_query = request.GET.get("name", "").strip()

    skills = Skill.objects.all()

    if name_query:
        skills = skills.filter(name__icontains=name_query)

    skills_json = serializers.serialize("json", skills)

    return HttpResponse(
        skills_json,
        content_type="application/json"
    )


def show_skills(request):
    json_response = get_skills_json(request)

    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    skills = [
        skill.object
        for skill in skills
    ]

    software_skills = [
        skill
        for skill in skills
        if skill.skill_type == "Software"
    ]

    systems_skills = [
        skill
        for skill in skills
        if skill.skill_type == "Systems"
    ]

    name_query = request.GET.get("name", "").strip()

    context = {
        "name": "Justin Evan Halim Saputra",
        "software_skills": software_skills,
        "systems_skills": systems_skills,
        "name_query": name_query,
    }

    return render(request, "skill.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Justin Evan Halim Saputra",
        "form": form,
    }
    return render(request, "projects_form.html", context)

...
def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Justin Evan Halim Saputra",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

