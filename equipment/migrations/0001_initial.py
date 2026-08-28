from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Equipment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("category", models.CharField(max_length=80)),
                ("is_available", models.BooleanField(default=True)),
                ("borrower_first_name", models.CharField(blank=True, max_length=80)),
                ("borrower_last_name", models.CharField(blank=True, max_length=80)),
                ("borrowed_at", models.DateTimeField(blank=True, null=True)),
                ("returned_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"ordering": ["category", "name"]},
        ),
    ]
