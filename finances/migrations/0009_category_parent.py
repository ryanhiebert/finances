# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0008_budget_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, to_field='id', null=True, to='finances.Category'),
            preserve_default=True,
        ),
    ]
