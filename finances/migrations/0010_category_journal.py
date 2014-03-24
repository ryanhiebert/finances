# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0009_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='journal',
            field=models.ForeignKey(to='finances.Journal', to_field='id'),
            preserve_default=True,
        ),
    ]
