# Generated by Django 4.0.2 on 2022-02-14 18:50

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to=main_page.models.Photo.get_file_name)),
            ],
        ),
    ]
