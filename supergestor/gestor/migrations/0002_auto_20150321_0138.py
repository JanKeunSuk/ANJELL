# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('Actividad_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='asignacion',
            fields=[
                ('asignation_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Flujo',
            fields=[
                ('Flujo_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=3, choices=[(b'CAN', b'Cancelado'), (b'ACT', b'Activo')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HU',
            fields=[
                ('HU_id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('valor_negocio', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('valor_tecnico', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('prioridad', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99)])),
                ('duracion', models.FloatField()),
                ('acumulador_horas', models.FloatField()),
                ('estado', models.CharField(max_length=3, choices=[(b'CAN', b'Cancelado'), (b'ACT', b'Activo')])),
                ('kanban', models.ForeignKey(to='gestor.Flujo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('proyecto_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_corto', models.CharField(max_length=200)),
                ('nombre_largo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('estado', models.CharField(max_length=3, choices=[(b'PEN', b'Pendiente'), (b'ACT', b'Activo'), (b'ANU', b'Anulado'), (b'FIN', b'Finalizado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('rol_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_rol_id', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=3, choices=[(b'SIS', b'Sistema'), (b'PRO', b'Proyecto')])),
                ('permisos', models.ManyToManyField(to='auth.Permission')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('Sprint_id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateTimeField()),
                ('duracion', models.FloatField()),
                ('estado', models.CharField(max_length=3, choices=[(b'CAN', b'Cancelado'), (b'ACT', b'Activo'), (b'CON', b'Consulta')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hu',
            name='proyecto',
            field=models.ForeignKey(to='gestor.proyecto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hu',
            name='sprint',
            field=models.ForeignKey(to='gestor.Sprint'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asignacion',
            name='HU',
            field=models.ForeignKey(to='gestor.HU'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asignacion',
            name='proyecto',
            field=models.ForeignKey(to='gestor.proyecto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asignacion',
            name='rol',
            field=models.ForeignKey(to='gestor.rol'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asignacion',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actividad',
            name='flujo',
            field=models.ForeignKey(to='gestor.Flujo'),
            preserve_default=True,
        ),
    ]
