# Generated by Django 2.2 on 2021-06-22 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extra_table', '0002_auto_20210621_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySalesBySKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('counts', models.PositiveIntegerField(blank=True, null=True)),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extra_table.SKU')),
                ('stores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extra_table.Stores')),
            ],
        ),
        migrations.CreateModel(
            name='DailyInventoryBySKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('counts', models.PositiveIntegerField(blank=True, null=True)),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extra_table.SKU')),
                ('stores_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extra_table.Store_house')),
            ],
        ),
    ]
