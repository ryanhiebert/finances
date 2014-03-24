# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0004_allotment_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='allotment',
            name='category',
            field=models.ForeignKey(to='finances.Category', to_field='id'),
            preserve_default=True,
        ),
    ]
