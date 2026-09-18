from django.urls import path

from main.views import show_main, show_experience, show_education, show_skills, create_project, show_projects, get_projects_json, delete_project, create_skill, update_skill, delete_skill, get_skills_json

app_name = "main"

urlpatterns = [
    # Main pages
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    # Skills
    path("skills/", show_skills, name="show_skills"),
    path("skills/add/", create_skill, name="create_skill"),
    path("skills/<uuid:skill_id>/update/", update_skill, name="update_skill",),
    path("skills/<uuid:skill_id>/delete/", delete_skill, name="delete_skill"),
    path("api/skills/", get_skills_json, name="get_skills_json"),
    # Projects
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project",),
    path("api/projects/", get_projects_json, name="get_projects_json"),
]