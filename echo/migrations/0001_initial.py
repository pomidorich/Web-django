# Generated by Django 4.1.3 on 2022-11-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'Books',
                'managed': False,
            },
        ),
    ]
