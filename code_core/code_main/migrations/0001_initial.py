# Generated by Django 2.1.4 on 2018-12-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cipher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('direction', models.CharField(max_length=10)),
                ('translaction', models.IntegerField()),
                ('result', models.TextField()),
            ],
            options={
                'db_table': 'code_main',
            },
        ),
    ]
