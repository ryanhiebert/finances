# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0007_budget_previous'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='journal',
            field=models.ForeignKey(to='finances.Journal', to_field='id'),
            preserve_default=True,
        ),
    ]
