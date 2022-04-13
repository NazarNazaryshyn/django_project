# Generated by Django 4.0.2 on 2022-02-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_category_is_visible_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=60, unique=True)),
                ('description', models.TextField(blank=True, max_length=700)),
            ],
        ),
    ]
