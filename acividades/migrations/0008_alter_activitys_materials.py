# Generated by Django 5.1.1 on 2025-01-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acividades', '0007_remove_activitys_typecoffee_activitys_typerice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitys',
            name='materials',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Materials of activity'),
        ),
    ]
