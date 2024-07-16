# Generated by Django 4.1.4 on 2024-07-16 08:19

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(blank=True, max_length=500)),
                ('review', tinymce.models.HTMLField(blank=True)),
                ('rating', models.FloatField(default=5)),
            ],
        ),
        migrations.AlterModelOptions(
            name='destination',
            options={'ordering': ('order', 'name')},
        ),
        migrations.AddField(
            model_name='activity',
            name='additional_info',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='altitude_chart',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='activity',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='activity',
            name='trek_map',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='activityregion',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='activityregion',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='destination',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='destination',
            name='order',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='tour_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='tour_excludes',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='tour_highlights',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='tour_includes',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='activityfaq',
            name='answer',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='activityfaq',
            name='question',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='destination_detail',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='itineraryactivity',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='itineraryactivity',
            name='highest_altitude',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='itineraryactivity',
            name='meals',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='itineraryactivity',
            name='trek_distance',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='itineraryactivity',
            name='trek_duration',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='ActivityTestimonialImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('activity_testimonial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='activity.activitytestimonial')),
            ],
        ),
        migrations.AddField(
            model_name='activitytestimonial',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='activity.activity'),
        ),
        migrations.CreateModel(
            name='ActivityEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=400)),
                ('phone', models.CharField(blank=True, default=' ', max_length=400)),
                ('message', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enquiries', to='activity.activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=400)),
                ('phone', models.CharField(blank=True, max_length=400)),
                ('message', models.TextField(blank=True)),
                ('no_of_guests', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('is_private', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('booking_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField(null=True)),
                ('departure_date', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('emergency_contact_name', models.CharField(blank=True, max_length=400)),
                ('emergency_address', models.CharField(blank=True, max_length=400)),
                ('emergency_phone', models.CharField(blank=True, max_length=400)),
                ('emergency_email', models.CharField(blank=True, max_length=400)),
                ('emergency_relationship', models.CharField(blank=True, max_length=400)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='activity.activity')),
            ],
        ),
    ]
