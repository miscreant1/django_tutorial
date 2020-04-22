# Generated by Django 3.0.5 on 2020-04-22 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='multitableinheritance.Place')),
                ('serves_hot_dogs', models.BooleanField(default=False)),
                ('serves_pizza', models.BooleanField(default=False)),
            ],
            bases=('multitableinheritance.place',),
        ),
    ]
