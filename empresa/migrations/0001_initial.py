# Generated by Django 4.1.5 on 2023-01-29 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecnologia', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='logo_empresa')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('cidade', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=30)),
                ('caracteristica_empresa', models.TextField()),
                ('nicho_mercado', models.CharField(choices=[('M', 'Marketing'), ('N', 'Nutrição'), ('D', 'Design'), ('T', 'Tecnologia')], max_length=4)),
                ('tecnologias', models.ManyToManyField(to='empresa.tecnologias')),
            ],
        ),
    ]