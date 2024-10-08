# Generated by Django 5.1.1 on 2024-09-14 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_forummodel_description_forummodel_title'),
        ('sujet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sujetmodel',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sujetmodel',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sujetmodel',
            name='forum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forum_sujet_id', to='forum.forummodel'),
        ),
    ]
