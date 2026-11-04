from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Project, Skill


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]
    def get_star_count(self, obj):
        return obj.starred_by.count()
    def get_is_starred(self, obj):
        request = self.context.get("request")

        if request is None or not request.user.is_authenticated:
            return False

        return request.user in obj.starred_by.all()
    def get_starred_by_names(self, obj):
        return ", ".join(
            user.username for user in obj.starred_by.all()
        )
    def validate_title(self, value):
        value = strip_tags(value).strip()

        if not value:
            raise serializers.ValidationError(
                "Title cannot be empty."
            )

        return value
    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Description cannot be empty after cleaning.")
        return value

    def validate_tech_stack(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Tech stack cannot be empty after cleaning.")
        return value


class SkillSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = [
            "id", "name", "skill_type", "description", "image_filename",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id", "star_count", "is_starred", "starred_by_names"]

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        # Iteration reuses prefetched users when the list view supplies them.
        return any(user.pk == request.user.pk for user in obj.starred_by.all())

    def get_starred_by_names(self, obj):
        return ", ".join(sorted(user.username for user in obj.starred_by.all()))

    def _clean_required_text(self, value):
        """Reject text that becomes empty after removing HTML and whitespace."""
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Teks tidak boleh kosong setelah dibersihkan.")
        return value

    def validate_name(self, value):
        return self._clean_required_text(value)

    def validate_description(self, value):
        return self._clean_required_text(value)

    def validate_image_filename(self, value):
        return self._clean_required_text(value)

    def validate_skill_type(self, value):
        # ChoiceField checks membership before this field-level validator runs.
        return strip_tags(value).strip()
