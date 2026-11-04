from django.contrib.auth.models import Permission, User
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skill


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
