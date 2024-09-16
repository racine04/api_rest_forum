# Generated by Django 5.1.1 on 2024-09-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_forummodel_description_forummodel_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forummodel',
            name='title',
        ),
        migrations.AddField(
            model_name='forummodel',
            name='name',
            field=models.CharField(default='', max_length=180),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forummodel',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
