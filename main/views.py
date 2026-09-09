from django.shortcuts import render

from main.models import Experience, Mahasiswa, Skill


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

def show_skills(request):
    context = {
        'name': 'Justin Evan Halim Saputra',
        'software_skills': Skill.objects.filter(skill_type='Software'),
        'systems_skills': Skill.objects.filter(skill_type='Systems'),
    }
    return render(request, 'skill.html', context)