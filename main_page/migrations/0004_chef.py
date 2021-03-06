# Generated by Django 4.0.2 on 2022-02-13 13:11

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_advantage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('second_name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('position', models.CharField(db_index=True, max_length=50, unique=True)),
                ('photo', models.ImageField(upload_to=main_page.models.Chef.get_file_name)),
                ('instagram_link', models.CharField(db_index=True, max_length=150, unique=True)),
                ('facebook_link', models.CharField(db_index=True, max_length=150, unique=True)),
                ('twitter_link', models.CharField(db_index=True, max_length=150, unique=True)),
                ('linkedin_link', models.CharField(db_index=True, max_length=150, unique=True)),
            ],
        ),
    ]
