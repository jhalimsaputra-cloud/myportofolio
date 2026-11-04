import uuid

from django.contrib.auth.models import AnonymousUser, Group, User
from django.test import RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Project, Skill
from main.serializers import SkillSerializer


class SkillSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="skill-reader", password="test-password",
            email="private@example.com",
        )
        self.payload = {
            "name": "Python", "skill_type": "Software",
            "description": "Backend development", "image_filename": "python.png",
        }
        self.skill = Skill.objects.create(**self.payload)

    def serialize_for(self, user):
        request = RequestFactory().get("/api/v1/skills/")
        request.user = user
        return SkillSerializer(self.skill, context={"request": request}).data

    def test_representation_exposes_only_public_fields(self):
        self.skill.starred_by.add(self.user)
        data = self.serialize_for(self.user)
        self.assertEqual(set(data), {
            "id", "name", "skill_type", "description", "image_filename",
            "star_count", "is_starred",
        })
        self.assertEqual(data["id"], str(self.skill.pk))
        self.assertEqual(data["star_count"], 1)
        self.assertTrue(data["is_starred"])
        self.assertNotIn(self.user.email, str(data))
        self.assertNotIn(self.user.password, str(data))
        self.assertFalse(self.serialize_for(AnonymousUser())["is_starred"])
        self.assertFalse(SkillSerializer(self.skill).data["is_starred"])

    def test_star_status_is_specific_to_current_user(self):
        other = User.objects.create_user(username="other-reader")
        self.skill.starred_by.add(other)
        data = self.serialize_for(self.user)
        self.assertEqual(data["star_count"], 1)
        self.assertFalse(data["is_starred"])

    def test_create_sanitizes_text_and_preserves_category(self):
        serializer = SkillSerializer(data={
            "name": "  <b>Python</b>  ", "skill_type": "Systems",
            "description": " <p>Backend development</p> ",
            "image_filename": " <b>python.png</b> ",
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        skill = serializer.save()
        self.assertEqual(skill.name, "Python")
        self.assertEqual(skill.description, "Backend development")
        self.assertEqual(skill.image_filename, "python.png")
        self.assertEqual(skill.skill_type, "Systems")

    def test_invalid_input_does_not_create_records(self):
        cases = [
            ("name", ""), ("name", "   "), ("name", "<b></b>"),
            ("name", "x" * 101),
            ("description", ""), ("description", " <p> </p> "),
            ("image_filename", ""), ("image_filename", "<img src='x'>"),
            ("image_filename", "x" * 201),
            ("skill_type", "Unknown"), ("skill_type", "<b>Software</b>"),
        ]
        for field, value in cases:
            with self.subTest(field=field, value=value):
                serializer = SkillSerializer(data={**self.payload, field: value})
                self.assertFalse(serializer.is_valid())
                self.assertIn(field, serializer.errors)
        self.assertEqual(Skill.objects.count(), 1)

    def test_identity_and_star_fields_cannot_be_written(self):
        forged_id = uuid.uuid4()
        serializer = SkillSerializer(data={
            **self.payload, "id": str(forged_id), "star_count": 99,
            "is_starred": True, "starred_by": [self.user.pk],
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        created = serializer.save()
        self.assertNotEqual(created.pk, forged_id)
        self.assertEqual(created.starred_by.count(), 0)
        self.assertEqual(serializer.data["star_count"], 0)
        self.assertFalse(serializer.data["is_starred"])
        self.assertTrue(all(serializer.fields[name].read_only for name in (
            "id", "star_count", "is_starred",
        )))

    def test_partial_update_preserves_unspecified_fields(self):
        serializer = SkillSerializer(
            self.skill, data={"name": " <b>Django</b> "}, partial=True,
        )
        self.assertTrue(serializer.is_valid(), serializer.errors)
        serializer.save()
        self.skill.refresh_from_db()
        self.assertEqual(self.skill.name, "Django")
        self.assertEqual(self.skill.description, self.payload["description"])
        self.assertEqual(self.skill.skill_type, self.payload["skill_type"])

    def test_full_update_requires_all_required_fields(self):
        serializer = SkillSerializer(self.skill, data={"name": "Changed"})
        self.assertFalse(serializer.is_valid())
        for field in ("skill_type", "description", "image_filename"):
            self.assertIn(field, serializer.errors)
        self.skill.refresh_from_db()
        self.assertEqual(self.skill.name, self.payload["name"])

    def test_invalid_partial_update_preserves_database(self):
        serializer = SkillSerializer(
            self.skill, data={"description": "<p></p>"}, partial=True,
        )
        self.assertFalse(serializer.is_valid())
        self.skill.refresh_from_db()
        self.assertEqual(self.skill.description, self.payload["description"])


class ProjectAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner",
            password="test-password",
            email="owner@example.com",
        )
        self.visitor = User.objects.create_user(
            username="visitor",
            password="test-password",
        )
        self.project = Project.objects.create(
            title="Portfolio",
            description="My website",
            tech_stack="Django",
        )

        self.list_url = reverse("api:project-list")
        self.detail_url = reverse(
            "api:project-detail",
            args=[self.project.id],
        )
        self.star_url = reverse(
            "api:project-star",
            args=[self.project.id],
        )

        self.payload = {
            "title": "New project",
            "description": "A useful app",
            "tech_stack": "Python",
            "project_url": "https://example.com/",
            "project_image_url": "",
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], str(self.project.id))
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("fields", response.data[0])
        self.assertEqual(
            self.client.get(self.detail_url).status_code,
            status.HTTP_200_OK,
        )

    def test_search_and_empty_results(self):
        response = self.client.get(self.list_url, {"title": "PORT"})
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            self.list_url,
            {"title": "not-found"},
        )
        self.assertEqual(response.data, [])

    def test_missing_project(self):
        url = reverse("api:project-detail", args=[uuid.uuid4()])

        self.assertEqual(
            self.client.get(url).status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)

            self.assertEqual(
                self.client.post(
                    self.list_url,
                    self.payload,
                    format="json",
                ).status_code,
                status.HTTP_403_FORBIDDEN,
            )
            self.assertEqual(
                self.client.patch(
                    self.detail_url,
                    {"title": "Changed"},
                    format="json",
                ).status_code,
                status.HTTP_403_FORBIDDEN,
            )
            self.assertEqual(
                self.client.delete(self.detail_url).status_code,
                status.HTTP_403_FORBIDDEN,
            )

        self.assertEqual(Project.objects.count(), 1)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "Portfolio")

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Project.objects.filter(pk=response.data["id"]).exists()
        )

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)

        for changes, field in [
            ({"title": "   "}, "title"),
            (
                {"title": '<img src="x" onerror="alert(1)">'},
                "title",
            ),
            (
                {"project_url": "javascript:alert(1)"},
                "project_url",
            ),
        ]:
            response = self.client.post(
                self.list_url,
                {**self.payload, **changes},
                format="json",
            )

            self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST,
            )
            self.assertIn(field, response.data)

        self.assertEqual(Project.objects.count(), 1)

    def test_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.patch(
            self.detail_url,
            {"title": "Changed"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.project.refresh_from_db()
        self.assertEqual(self.project.description, "My website")

        response = self.client.put(
            self.detail_url,
            {"title": "Incomplete"},
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        response = self.client.put(
            self.detail_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(self.detail_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(response.content, b"")
        self.assertFalse(
            Project.objects.filter(pk=self.project.id).exists()
        )

    def test_star_requires_login_and_toggles(self):
        self.assertEqual(
            self.client.post(self.star_url).status_code,
            status.HTTP_403_FORBIDDEN,
        )

        self.client.force_authenticate(user=self.visitor)

        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)

        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            {
                **self.payload,
                "star_count": 99,
                "is_starred": True,
                "starred_by_names": "forged",
                "starred_by": [self.visitor.id],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_staff_and_editor_cannot_manage_tutorial_projects(self):
        self.visitor.is_staff = True
        self.visitor.save()
        self.visitor.groups.add(Group.objects.create(name="Editor"))

        self.client.force_authenticate(user=self.visitor)

        response = self.client.patch(
            self.detail_url,
            {"title": "Changed"},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)

        self.assertEqual(
            self.client.delete(self.list_url).status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)

        self.assertTrue(
            client.login(
                username="owner",
                password="test-password",
            )
        )

        response = client.post(
            self.list_url,
            self.payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )
        self.assertEqual(Project.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        client.login(
            username="owner",
            password="test-password",
        )

        page = client.get(
            self.list_url,
            HTTP_ACCEPT="text/html",
        )
        self.assertEqual(page.status_code, status.HTTP_200_OK)

        token = client.cookies["csrftoken"].value

        response = client.post(
            self.list_url,
            self.payload,
            format="json",
            HTTP_X_CSRFTOKEN=token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
