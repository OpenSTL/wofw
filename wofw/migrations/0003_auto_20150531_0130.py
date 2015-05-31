# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wofw', '0002_remove_vote_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alderman',
            name='ward',
            field=models.ForeignKey(to='wofw.Ward'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='alderlast',
            field=models.ForeignKey(to='wofw.Alderman'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='billnumber',
            field=models.ForeignKey(to='wofw.Bill'),
            preserve_default=True,
        ),
    ]
