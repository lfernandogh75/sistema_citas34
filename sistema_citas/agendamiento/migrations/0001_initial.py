# Generated by Django 5.0.7 on 2024-08-02 00:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=20)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamiento.especialidad')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('motivo', models.TextField()),
                ('estado', models.CharField(choices=[('programada', 'Programada'), ('completada', 'Completada'), ('cancelada', 'Cancelada')], default='programada', max_length=20)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas_paciente', to=settings.AUTH_USER_MODEL)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamiento.medico')),
            ],
        ),
    ]
