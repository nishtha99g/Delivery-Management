# Generated by Django 2.2.8 on 2020-06-27 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
        ('users', '0002_auto_20200627_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='warehouse.Warehouse'),
        ),
    ]
