# Generated by Django 5.1.1 on 2025-01-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acividades', '0003_alter_activitys_typecoffee'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitys',
            name='materials',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Materials of activity'),
        ),
    ]
