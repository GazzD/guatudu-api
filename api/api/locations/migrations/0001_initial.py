# Generated by Django 3.0.2 on 2020-01-20 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on witch the object was created', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on witch the object was last modified', verbose_name='modified_at')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cities/images')),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on witch the object was created', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on witch the object was last modified', verbose_name='modified_at')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='cities/images')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Country')),
            ],
            options={
                'db_table': 'cities',
            },
        ),
    ]
