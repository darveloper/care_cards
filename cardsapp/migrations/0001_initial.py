# Generated by Django 3.0.8 on 2020-07-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(max_length=300)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(default=None, max_length=200)),
                ('state', models.CharField(default=None, max_length=3)),
                ('zip_code', models.CharField(max_length=12)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
