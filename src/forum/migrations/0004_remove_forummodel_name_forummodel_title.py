# Generated by Django 5.1.1 on 2024-09-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_remove_forummodel_title_forummodel_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forummodel',
            name='name',
        ),
        migrations.AddField(
            model_name='forummodel',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
