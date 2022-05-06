# Generated by Django 4.0.3 on 2022-03-24 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_bookreview_stars_given'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.CreateModel(
            name='GenreBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.genre')),
            ],
        ),
        migrations.CreateModel(
            name='GenreAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.genre')),
            ],
        ),
    ]