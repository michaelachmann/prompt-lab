# Generated by Django 5.0.4 on 2024-06-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0004_alter_dataset_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="datasets/"),
        ),
    ]
