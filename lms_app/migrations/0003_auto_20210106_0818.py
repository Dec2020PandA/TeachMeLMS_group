# Generated by Django 2.2 on 2021-01-06 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_playlist_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Quiz_Record',
            new_name='UserQuizRecord',
        ),
    ]
