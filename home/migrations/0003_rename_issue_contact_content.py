# Generated by Django 4.0.1 on 2022-04-29 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='issue',
            new_name='content',
        ),
    ]
