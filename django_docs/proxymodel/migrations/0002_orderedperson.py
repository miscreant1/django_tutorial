# Generated by Django 3.0.5 on 2020-04-23 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxymodel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedPerson',
            fields=[
            ],
            options={
                'ordering': ['last_name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('proxymodel.person',),
        ),
    ]