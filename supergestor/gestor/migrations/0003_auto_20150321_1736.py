# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0002_auto_20150321_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='delegacion',
            fields=[
                ('delegacion_id', models.AutoField(serialize=False, primary_key=True)),
                ('HU', models.ForeignKey(to='gestor.HU')),
                ('proyecto', models.ForeignKey(to='gestor.proyecto')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='asignacion',
            name='HU',
        ),
    ]
