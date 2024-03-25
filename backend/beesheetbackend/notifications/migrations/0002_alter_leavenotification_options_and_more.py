# Generated by Django 5.0.1 on 2024-03-05 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('leave_management', '0002_alter_leavetype_options'),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leavenotification',
            options={},
        ),
        migrations.AlterField(
            model_name='leavenotification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='leavenotification',
            name='leave_application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave_management.leaveapplication'),
        ),
        migrations.AlterField(
            model_name='leavenotification',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='leavenotification',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
    ]