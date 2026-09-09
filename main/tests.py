from django.test import TestCase
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
 
    def test_url_and_template_correct(self):
        """1. URL dapat diakses dan menggunakan template yang tepat."""
        # Mengakses URL berdasarkan named route yang kamu buat di HTML
        response = self.client.get(reverse('main:show_skills'))
 
        # Memastikan status respons 200 (OK/Berhasil diakses)
        self.assertEqual(response.status_code, 200)
        # Memastikan template yang digunakan sesuai
        self.assertTemplateUsed(response, 'skill.html') 
 
    def test_model_data_appears_in_html_when_data_exists(self):
        """2. Data model muncul di halaman HTML ketika ada data."""
        # Setup: Buat data uji coba di database testing
        Skill.objects.create(
            name="Python",
            skill_type="Software",
            description="Building backend logic, data processing.",
            image_filename="python-logo.png"
        )
        Skill.objects.create(
            name="MIPS Assembly",
            skill_type="Systems",
            description="Understanding low-level computer architecture.",
            image_filename="mips-logo.png"
        )
 
        # Action: Akses halamannya
        response = self.client.get(reverse('main:show_skills'))
 
        # Assert: Pastikan data yang dibuat tadi ikut ter-render di dalam HTML
        self.assertContains(response, "Python")
        self.assertContains(response, "Building backend logic, data processing.")
        self.assertContains(response, "MIPS Assembly")
 
        # Assert tambahan: karena kedua tipe sudah terisi, pesan "belum ada skill"
        # untuk keduanya seharusnya TIDAK muncul sama sekali
        self.assertNotContains(response, "Belum ada skill Software Development yang ditambahkan.")
        self.assertNotContains(response, "Belum ada skill Systems &amp; Architecture yang ditambahkan.")
 
    def test_empty_state_message_when_no_data(self):
        """3. Halaman HTML menampilkan pesan kondisi kosong ketika belum ada data."""
        # Setup: Kita biarkan database testing kosong tanpa membuat objek Skill
 
        # Action: Akses halamannya
        response = self.client.get(reverse('main:show_skills'))
 
        # Assert: Pastikan pesan dari blok {% empty %} di HTML kamu muncul
        self.assertContains(response, "Belum ada skill Software Development yang ditambahkan.")
        self.assertContains(response, "Belum ada skill Systems &amp; Architecture yang ditambahkan.")
 
    def test_empty_state_shown_only_for_type_without_data(self):
        """Bonus: kalau cuma salah satu tipe yang punya data, pesan kosong hanya
        muncul untuk tipe yang memang belum punya skill, bukan keduanya."""
        Skill.objects.create(
            name="Java",
            skill_type="Software",
            description="Core Java and OOP principles.",
            image_filename="java-logo.png"
        )
 
        response = self.client.get(reverse('main:show_skills'))
 
        # Software sudah ada isinya -> pesan kosong Software tidak boleh muncul
        self.assertContains(response, "Java")
        self.assertNotContains(response, "Belum ada skill Software Development yang ditambahkan.")
 
        # Systems masih kosong -> pesan kosongnya harus tetap muncul
        self.assertContains(response, "Belum ada skill Systems &amp; Architecture yang ditambahkan.")
 
    def test_skills_are_grouped_under_correct_type_in_context(self):
        """Bonus: memastikan pemisahan skill per tipe benar di level context,
        bukan cuma kebetulan sama-sama muncul di HTML."""
        software_skill = Skill.objects.create(
            name="Django",
            skill_type="Software",
            description="Full-stack web framework.",
            image_filename="django-logo.png"
        )
        systems_skill = Skill.objects.create(
            name="AVR Assembly",
            skill_type="Systems",
            description="Low-level microcontroller programming.",
            image_filename="avr-logo.png"
        )
 
        response = self.client.get(reverse('main:show_skills'))
 
        software_skills = list(response.context['software_skills'])
        systems_skills = list(response.context['systems_skills'])
 
        self.assertIn(software_skill, software_skills)
        self.assertNotIn(systems_skill, software_skills)
 
        self.assertIn(systems_skill, systems_skills)
        self.assertNotIn(software_skill, systems_skills)
 