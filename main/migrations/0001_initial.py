# Generated by Django 5.0.3 on 2024-03-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Unique word for this link')),
                ('link', models.CharField(max_length=250, verbose_name='Full link')),
            ],
        ),
    ]