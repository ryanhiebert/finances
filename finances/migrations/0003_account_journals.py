# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_account_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='journals',
            field=models.ManyToManyField(to='finances.Journal'),
            preserve_default=True,
        ),
    ]
