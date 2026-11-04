import os
import runpy
from unittest.mock import patch

from django.contrib.auth.models import Permission, User
from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skill


class EnvironmentSettingsTest(SimpleTestCase):
    def load_settings(self, production):
        with patch.dict(os.environ, {"PRODUCTION": production}), patch("dotenv.load_dotenv"):
            settings_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "portofolio", "settings.py")
            return runpy.run_path(settings_path, run_name="_settings_check_")

    def test_production_disables_debug(self):
        for value in ("True", "true", "TRUE"):
            with self.subTest(value=value):
                config = self.load_settings(value)
                self.assertTrue(config["PRODUCTION"])
                self.assertFalse(config["DEBUG"])

    def test_local_development_enables_debug(self):
        config = self.load_settings("False")
        self.assertFalse(config["PRODUCTION"])
        self.assertTrue(config["DEBUG"])


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

class SkillViewTest(TestCase):
    def create_skill(self, name="Python", skill_type="Software"):
        return Skill.objects.create(
            name=name,
            skill_type=skill_type,
            description="Building backend logic.",
            image_filename="python-logo.png",
        )

    def get_skills(self, **params):
        response = self.client.get(reverse("api:skill-list"), params)
        self.assertEqual(response.status_code, 200)
        return response.json()

    def test_url_and_template_correct(self):
        """Halaman menyediakan wadah untuk kartu yang dimuat melalui AJAX."""
        response = self.client.get(reverse("main:show_skills"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertContains(response, 'id="software-grid"')
        self.assertContains(response, 'id="systems-grid"')
        self.assertContains(response, reverse("api:skill-list"))
        self.assertNotContains(response, reverse("main:get_skills_json"))

    def test_skill_data_available_through_json(self):
        """Endpoint menyediakan identitas dan isi kartu untuk frontend."""
        skill = self.create_skill()
        data = self.get_skills()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], str(skill.id))
        fields = data[0]
        self.assertEqual(fields["name"], skill.name)
        self.assertEqual(fields["description"], skill.description)
        self.assertEqual(fields["image_filename"], skill.image_filename)
        self.assertEqual(fields["star_count"], 0)
        self.assertFalse(fields["is_starred"])

    def test_empty_data_and_empty_state_placeholder(self):
        """API mengirim daftar kosong; HTML menyediakan pesan untuk frontend."""
        self.assertEqual(self.get_skills(), [])
        response = self.client.get(reverse("main:show_skills"))
        self.assertContains(response, 'id="empty"')
        self.assertContains(
            response,
            "Belum ada skill yang ditambahkan maupun ditemukan.",
        )

    def test_single_category_data(self):
        """Data satu kategori tidak menghasilkan entri kategori lainnya."""
        skill = self.create_skill(name="Java")
        data = self.get_skills()
        self.assertEqual(
            [(item["id"], item["skill_type"]) for item in data],
            [(str(skill.id), "Software")],
        )

    def test_category_values_preserved_in_json(self):
        """API mempertahankan kategori yang diperlukan frontend untuk pengelompokan."""
        software = self.create_skill(name="Django")
        systems = self.create_skill(name="AVR Assembly", skill_type="Systems")
        categories = {
            item["id"]: item["skill_type"]
            for item in self.get_skills()
        }
        self.assertEqual(categories, {
            str(software.id): "Software",
            str(systems.id): "Systems",
        })

    def test_search_is_case_insensitive_and_can_return_empty(self):
        skill = self.create_skill()
        self.create_skill(name="Java")
        data = self.get_skills(name="  PYTH  ")
        self.assertEqual([item["id"] for item in data], [str(skill.id)])
        self.assertEqual(self.get_skills(name="not-found"), [])

    def test_legacy_json_endpoint_remains_available(self):
        """Migrating the page must not break consumers of the previous endpoint."""
        skill = self.create_skill()
        response = self.client.get(reverse("main:get_skills_json"), {"name": "PYTH"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["pk"], str(skill.pk))
        self.assertEqual(response.json()[0]["fields"]["name"], skill.name)

    def test_management_form_and_csrf_cookie_follow_roles(self):
        user = User.objects.create_user(username="page-reader")
        editor = User.objects.create_user(username="page-editor")
        editor.user_permissions.add(Permission.objects.get(
            content_type__app_label="main", codename="change_skill",
        ))
        owner = User.objects.create_superuser(username="page-owner")
        for account, can_edit, can_create in (
            (None, False, False), (user, False, False),
            (editor, True, False), (owner, True, True),
        ):
            with self.subTest(account=account):
                client = Client(enforce_csrf_checks=True)
                if account is not None:
                    client.force_login(account)
                response = client.get(reverse("main:show_skills"))
                self.assertEqual(response.status_code, 200)
                self.assertIn("csrftoken", response.cookies)
                self.assertContains(response, 'name="csrfmiddlewaretoken"')
                if can_edit:
                    self.assertContains(response, 'id="skill-form"')
                    self.assertContains(response, f'action="{reverse("api:skill-list")}"')
                else:
                    self.assertNotContains(response, 'id="skill-form"')
                if can_create:
                    self.assertContains(response, 'id="add-skill-button"')
                else:
                    self.assertNotContains(response, 'id="add-skill-button"')


class WebsiteRegressionTest(TestCase):
    def test_logout_requires_post_and_valid_csrf(self):
        user = User.objects.create_user(username="logout-check", password="test-password")
        client = Client(enforce_csrf_checks=True)
        self.assertTrue(client.login(username=user.username, password="test-password"))
        logout_url = reverse("main:logout")
        response = client.get(logout_url)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(client.session["_auth_user_id"], str(user.pk))
        self.assertEqual(client.post(logout_url).status_code, 403)
        self.assertEqual(client.session["_auth_user_id"], str(user.pk))
        page = client.get(reverse("main:show_main"))
        self.assertContains(page, f'action="{logout_url}"')
        token = client.cookies["csrftoken"].value
        response = client.post(logout_url, HTTP_X_CSRFTOKEN=token)
        self.assertRedirects(response, reverse("main:show_main"))
        self.assertNotIn("_auth_user_id", client.session)

    def test_pages_have_exactly_one_title(self):
        for name, title in (
            ("show_main", "Justin Evan Halim Saputra - Portfolio"),
            ("show_experience", "Justin Evan Halim Saputra - Portfolio"),
            ("show_education", "Justin Evan Halim Saputra - Portfolio"),
            ("show_skills", "Skills - Justin Evan Halim Saputra"),
            ("show_projects", "Projects - Justin Evan Halim Saputra"),
            ("login", "Login - Justin Evan Halim Saputra"),
            ("register", "Register - Justin Evan Halim Saputra"),
            ("show_test", "Website Feedback - Justin Evan Halim Saputra"),
        ):
            with self.subTest(page=name):
                response = self.client.get(reverse(f"main:{name}"))
                self.assertContains(response, "<title>", count=1)
                self.assertContains(response, "</title>", count=1)
                self.assertContains(response, title)

    def test_legacy_skill_success_messages_survive_redirect_once(self):
        owner = User.objects.create_superuser(username="legacy-owner")
        self.client.force_login(owner)
        payload = {
            "name": "Legacy Skill", "skill_type": "Software",
            "description": "Valid description", "image_filename": "python.png",
        }
        response = self.client.post(reverse("main:create_skill"), payload, follow=True)
        self.assertContains(response, "Skill baru berhasil ditambahkan!")
        skill = Skill.objects.get(name="Legacy Skill")
        response = self.client.get(reverse("main:show_skills"))
        self.assertNotContains(response, "Skill baru berhasil ditambahkan!")
        response = self.client.post(reverse("main:update_skill", args=[skill.pk]), {
            **payload, "name": "Updated legacy skill",
        }, follow=True)
        self.assertContains(response, "Skill berhasil diperbarui!")
        skill.refresh_from_db()
        self.assertEqual(skill.name, "Updated legacy skill")
        response = self.client.post(reverse("main:delete_skill", args=[skill.pk]), follow=True)
        self.assertContains(response, "Skill berhasil dihapus!")
        self.assertFalse(Skill.objects.filter(pk=skill.pk).exists())

    def test_feedback_accepts_valid_post_and_redirects(self):
        url = reverse("main:show_test")
        response = self.client.post(url, {"fname": "Example Reader", "lname": "reader@example.com"})
        self.assertRedirects(response, url)
        page = self.client.get(url)
        self.assertNotContains(page, "reader@example.com")
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(Skill.objects.count(), 0)

    def test_feedback_shows_confirmation_after_valid_post(self):
        response = self.client.post(reverse("main:show_test"), {
            "fname": "Example Reader", "lname": "reader@example.com",
        }, follow=True)
        self.assertContains(response, "Data formulir valid.")
        self.assertContains(response, "tidak menyimpan atau mengirim data.")

    def test_feedback_rejects_invalid_input(self):
        for payload, field in (
            ({"fname": "<b></b>", "lname": "reader@example.com"}, "fname"),
            ({"fname": "Reader", "lname": "invalid-email"}, "lname"),
            ({}, "fname"),
        ):
            with self.subTest(payload=payload):
                response = self.client.post(reverse("main:show_test"), payload)
                self.assertEqual(response.status_code, 200)
                self.assertIn(field, response.context["form"].errors)
        self.assertEqual(self.client.put(reverse("main:show_test")).status_code, 405)

    def test_feedback_requires_csrf(self):
        client = Client(enforce_csrf_checks=True)
        url = reverse("main:show_test")
        payload = {"fname": "Example Reader", "lname": "reader@example.com"}
        self.assertEqual(client.post(url, payload).status_code, 403)
        page = client.get(url)
        self.assertEqual(page.status_code, 200)
        token = client.cookies["csrftoken"].value
        self.assertEqual(client.post(url, payload, HTTP_X_CSRFTOKEN=token).status_code, 302)
