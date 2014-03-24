# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0006_budget_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='previous',
            field=models.OneToOneField(to_field='id', to='finances.Budget'),
            preserve_default=True,
        ),
    ]
