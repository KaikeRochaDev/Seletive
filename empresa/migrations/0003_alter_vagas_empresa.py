# Generated by Django 4.1.5 on 2023-01-29 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_vagas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresa.empresa'),
        ),
    ]
