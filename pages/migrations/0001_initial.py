# Generated by Django 2.2.9 on 2020-01-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('send_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-send_on'],
            },
        ),
    ]