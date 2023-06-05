# Generated by Django 4.2.1 on 2023-06-05 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('backups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]