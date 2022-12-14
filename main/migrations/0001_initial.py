# Generated by Django 4.0.6 on 2022-07-19 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, max_length=256, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=256, unique=True, verbose_name='Slug')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('author_pen', models.CharField(max_length=100, verbose_name='Book Author')),
                ('location', models.CharField(choices=[('Andijon', 'Andijon'), ('Namangan', 'Namangan'), ('Samarqand', 'Samarqand'), ('Tashkent', 'Tashkent'), ('Jizzax', 'Jizzax'), ('Surxondaryo', 'Surxondaryo'), ('Navoiy', 'Navoiy'), ('Xorazm', 'Xorazm'), ('Qashqadaryo', 'Qashqadaryo'), ('Buxoro', 'Buxoro'), ('Sirdaryo', 'Sirdaryo'), ('Fargona', 'Fargona')], max_length=256, verbose_name='loacation')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('image', models.ImageField(upload_to='book_images', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('likes_count', models.PositiveIntegerField(default=0, verbose_name='Likes')),
                ('is_checked', models.BooleanField(default=False)),
                ('is_view', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='main.genre')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'db_table': 'book',
                'unique_together': {('slug',)},
            },
        ),
    ]
