# Generated by Django 4.2.1 on 2024-01-27 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_exponant_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExponantComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('exponant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.exponant')),
            ],
        ),
    ]
