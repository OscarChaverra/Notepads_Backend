# Generated by Django 5.1.1 on 2025-02-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plaga', '0002_plaga_sintomas_plague'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plaga',
            name='name_plague',
            field=models.CharField(max_length=100, verbose_name='name of the plague'),
        ),
        migrations.AlterField(
            model_name='plaga',
            name='sintomas_plague',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='sintomas of plague'),
        ),
    ]
