# Generated by Django 4.1.7 on 2023-03-01 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id']},
        ),
    ]
