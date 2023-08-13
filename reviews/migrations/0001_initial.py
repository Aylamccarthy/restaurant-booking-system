# Generated by Django 3.2.19 on 2023-07-31 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rate", models.PositiveSmallIntegerField()),
                ("review_text", models.TextField()),
                (
                    "date_created_on",
                    models.DateTimeField(default="2023-07-31 18:26:59"),
                ),
                (
                    "date_updated_on",
                    models.DateTimeField(default="2023-07-31 18:26:59"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["date_updated_on"],
            },
        ),
    ]
