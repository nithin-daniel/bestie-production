# Generated by Django 4.2.4 on 2023-09-24 17:10

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
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='activity')),
            ],
            options={
                'verbose_name_plural': 'Activity',
            },
        ),
        migrations.CreateModel(
            name='ClientTestimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='MainTestimonials')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Client Testimonials',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_description', models.TextField()),
                ('event_date', models.DateField()),
                ('event_payment', models.CharField(max_length=100)),
                ('event_specialities', models.CharField(max_length=100)),
                ('event_benefits', models.CharField(max_length=100)),
                ('event_quotes', models.CharField(max_length=100)),
                ('event_photo', models.ImageField(upload_to='Event_Images')),
                ('event_about_section', models.TextField()),
                ('event_no_of_participations', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GalleryPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(upload_to='gallery_photos')),
            ],
            options={
                'verbose_name_plural': 'Gallery Photos',
            },
        ),
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=100)),
                ('news_date', models.DateField()),
                ('news_description', models.TextField()),
                ('new_image', models.ImageField(upload_to='New Imges/')),
            ],
            options={
                'verbose_name_plural': 'Latest News',
            },
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=100)),
                ('package_description', models.TextField()),
                ('package_image', models.ImageField(upload_to='Packages/')),
                ('package_slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Package',
            },
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_name', models.CharField(max_length=100)),
                ('resort_description', models.TextField()),
                ('resort_service_1', models.CharField(max_length=100)),
                ('resort_service_2', models.CharField(max_length=100)),
                ('resort_service_3', models.CharField(blank=True, max_length=100)),
                ('resort_service_4', models.CharField(blank=True, max_length=100)),
                ('resort_service_5', models.CharField(blank=True, max_length=100)),
                ('resort_service_6', models.CharField(blank=True, max_length=100)),
                ('resort_service_7', models.CharField(blank=True, max_length=100)),
                ('resort_service_8', models.CharField(blank=True, max_length=100)),
                ('resort_aminities_1', models.CharField(max_length=100)),
                ('resort_aminities_2', models.CharField(max_length=100)),
                ('resort_aminities_3', models.CharField(blank=True, max_length=100)),
                ('resort_aminities_4', models.CharField(blank=True, max_length=100)),
                ('resort_aminities_5', models.CharField(blank=True, max_length=100)),
                ('resort_aminities_6', models.CharField(blank=True, max_length=100)),
                ('resort_aminities_7', models.CharField(blank=True, max_length=100)),
                ('resort_aminities_8', models.CharField(blank=True, max_length=100)),
                ('resort_amount', models.CharField(max_length=100)),
                ('resort_images', models.ImageField(upload_to='Resort_Image')),
                ('resort_slug', models.SlugField()),
                ('resort_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.packages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Resort',
            },
        ),
    ]
