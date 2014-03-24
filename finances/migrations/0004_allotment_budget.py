# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_account_journals'),
    ]

    operations = [
        migrations.AddField(
            model_name='allotment',
            name='budget',
            field=models.ForeignKey(to='finances.Budget', to_field='id'),
            preserve_default=True,
        ),
    ]
