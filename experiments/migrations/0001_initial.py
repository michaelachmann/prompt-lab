# Generated by Django 5.0.4 on 2024-06-13 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datasets', '0002_dataset_delete_datasets'),
        ('ml_models', '0001_initial'),
        ('prompts', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('f1_score_macro', models.FloatField(blank=True, null=True)),
                ('f1_score_micro', models.FloatField(blank=True, null=True)),
                ('f1_score_weighted', models.FloatField(blank=True, null=True)),
                ('precision', models.FloatField(blank=True, null=True)),
                ('recall', models.FloatField(blank=True, null=True)),
                ('accuracy', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_experiments', to=settings.AUTH_USER_MODEL)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.dataset')),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_experiments', to=settings.AUTH_USER_MODEL)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ml_models.mlmodel')),
                ('prompt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prompts.prompt')),
            ],
        ),
    ]
