# Generated by Django 4.2.5 on 2023-12-04 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_event', models.DateField()),
                ('additional_notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name', 'phone_number'),
            },
        ),
    ]