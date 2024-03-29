# Generated by Django 4.2.5 on 2024-03-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('first_name', 'phone_number')},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='last name goes here', max_length=100),
            preserve_default=False,
        ),
    ]
