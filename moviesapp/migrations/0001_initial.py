# Generated by Django 4.2.4 on 2023-08-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=250)),
                ('image_url', models.URLField()),
                ('thumb_url', models.URLField()),
                ('imdb_url', models.CharField(max_length=150)),
                ('rating', models.FloatField()),
                ('year', models.IntegerField()),
                ('actors', models.ManyToManyField(to='moviesapp.actor')),
                ('directors', models.ManyToManyField(to='moviesapp.director')),
                ('genre', models.ManyToManyField(to='moviesapp.genre')),
            ],
        ),
    ]