# Generated by Django 4.0.1 on 2022-04-30 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_issue_contact_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Work title')),
                ('image', models.ImageField(upload_to='works')),
            ],
        ),
    ]
