# Generated by Django 5.0.2 on 2024-03-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_management', '0012_leaveapplication_manager_response_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaveapplication',
            name='manager_response',
        ),
        migrations.AddField(
            model_name='leaveapplication',
            name='admin_response',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=10, null=True),
        ),
    ]
