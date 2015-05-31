# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wofw', '0003_auto_20150531_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alderman',
            name='ward',
            field=models.ForeignKey(to='wofw.Ward'),
            preserve_default=True,
        ),
    ]
