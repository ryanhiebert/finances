# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0010_category_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='parent',
            field=models.ForeignKey(blank=True, to_field='id', null=True, to='finances.Journal'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='allotment',
            unique_together=set([('category', 'budget')]),
        ),
        migrations.AlterUniqueTogether(
            name='budget',
            unique_together=set([('journal', 'previous', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('journal', 'parent', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='journal',
            unique_together=set([('parent', 'name')]),
        ),
    ]
