# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='parent',
            field=models.ForeignKey(blank=True, to_field='id', null=True, to='finances.Account'),
            preserve_default=True,
        ),
    ]
