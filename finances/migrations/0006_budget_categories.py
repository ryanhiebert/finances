# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_allotment_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='categories',
            field=models.ManyToManyField(through='finances.Allotment', to='finances.Category'),
            preserve_default=True,
        ),
    ]
