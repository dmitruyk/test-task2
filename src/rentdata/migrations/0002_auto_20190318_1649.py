# Generated by Django 2.1.7 on 2019-03-18 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='adLinkForJSONP_xlink_href',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='adLinkForXMLData_xlink_href',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='remove_id',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='remove_modification',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='remove_publishDate',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='xlink_href',
        ),
    ]
