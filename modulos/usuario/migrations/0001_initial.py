# Generated by Django 3.2.4 on 2021-06-20 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(editable=False)),
                ('fecha_actualizacion', models.DateTimeField(editable=False)),
                ('identificacion', models.PositiveBigIntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
