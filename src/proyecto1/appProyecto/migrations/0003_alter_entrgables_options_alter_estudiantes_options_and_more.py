# Generated by Django 5.0 on 2023-12-29 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appProyecto', '0002_curso_entrgables_estudiantes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrgables',
            options={'verbose_name_plural': 'Entregables'},
        ),
        migrations.AlterModelOptions(
            name='estudiantes',
            options={'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'verbose_name_plural': 'Profesores'},
        ),
    ]
