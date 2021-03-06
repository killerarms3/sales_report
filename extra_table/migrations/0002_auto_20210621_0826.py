# Generated by Django 2.2 on 2021-06-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store_house',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.CharField(blank=True, max_length=256, null=True)),
                ('subtype', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='sku',
            name='status',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='stores',
            name='category',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='stores',
            name='code',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='stores',
            name='subtype',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
