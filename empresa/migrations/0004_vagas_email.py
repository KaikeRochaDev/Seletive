# Generated by Django 4.1.5 on 2023-01-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_alter_vagas_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagas',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]