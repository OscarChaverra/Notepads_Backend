# Generated by Django 5.1.1 on 2025-02-17 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plaga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plaga',
            name='sintomas_plague',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='sintomas of plague'),
        ),
    ]
