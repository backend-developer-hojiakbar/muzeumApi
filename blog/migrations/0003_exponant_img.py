# Generated by Django 4.2.1 on 2024-01-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_exponant_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='exponant',
            name='img',
            field=models.ImageField(default=1, upload_to='exponant/'),
            preserve_default=False,
        ),
    ]
