# Generated by Django 4.1.7 on 2023-03-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0003_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=20)),
                ('proyecto', models.CharField(max_length=60)),
                ('hora', models.TimeField()),
            ],
        ),
    ]
