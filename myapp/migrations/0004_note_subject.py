# Generated by Django 3.2.8 on 2023-07-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_note_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='subject',
            field=models.CharField(choices=[('Maths', 'Maths'), ('English', 'English')], default='Maths', max_length=30),
            preserve_default=False,
        ),
    ]