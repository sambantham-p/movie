# Generated by Django 4.1.5 on 2023-01-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('movieImg', models.CharField(blank=True, db_column='movieImg', max_length=800, null=True)),
                ('movieName', models.CharField(blank=True, db_column='movieName', max_length=500, null=True)),
                ('movieOverview', models.CharField(blank=True, db_column='movieOverview', max_length=1000, null=True)),
                ('movieRating', models.IntegerField(blank=True, db_column='movieRating', null=True)),
            ],
            options={
                'db_table': 'movieOverview',
                'managed': False,
            },
        ),
    ]