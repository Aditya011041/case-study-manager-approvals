# Generated by Django 5.0.2 on 2024-03-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management', '0030_leaveapplication_final_rejection_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapplication',
            name='effective_status',
            field=models.CharField(default='PENDING', max_length=20),
        ),
    ]
