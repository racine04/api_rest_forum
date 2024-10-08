# Generated by Django 5.1.1 on 2024-09-16 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_remove_forummodel_title_forummodel_name_and_more'),
        ('sujet', '0003_alter_sujetmodel_forum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sujetmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='sujetmodel',
            name='name',
            field=models.CharField(default='', max_length=180),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sujetmodel',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sujetmodel',
            name='forum',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='forum.forummodel'),
            preserve_default=False,
        ),
    ]
