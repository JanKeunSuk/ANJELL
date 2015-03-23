# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0003_auto_20150321_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hu',
            name='proyecto',
        ),
    ]
