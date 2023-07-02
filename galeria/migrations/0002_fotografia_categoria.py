# Generated by Django 4.2.2 on 2023-07-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'nebulosa'), ('ESTRELA', 'estrela'), ('GALAXIA', 'galaxia'), ('PLANETA', 'planeta')], default='', max_length=50),
        ),
    ]
