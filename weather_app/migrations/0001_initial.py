# Generated by Django 3.2.7 on 2023-11-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('lon', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('lat', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
            ],
        ),
    ]
