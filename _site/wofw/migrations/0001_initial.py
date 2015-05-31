# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alderman',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alderlast', models.CharField(max_length=100)),
                ('alderfull', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billnumber', models.IntegerField(default=0)),
                ('billname', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote', models.CharField(max_length=10, choices=[(b'aye', b'aye'), (b'nay', b'nay'), (b'present', b'present'), (b'no vote', b'no vote')])),
                ('reading', models.CharField(max_length=20, choices=[(b'committee', b'committee'), (b'perfection', b'perfection'), (b'final', b'final')])),
                ('date', models.DateField()),
                ('alderlast', models.ForeignKey(to='wofw.alderman')),
                ('billnumber', models.ForeignKey(to='wofw.bill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wardnumber', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='alderman',
            name='ward',
            field=models.ForeignKey(to='wofw.ward'),
            preserve_default=True,
        ),
    ]
