# Generated by Django 5.0.8 on 2024-08-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_auth', '0008_alter_pictures_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='add_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
