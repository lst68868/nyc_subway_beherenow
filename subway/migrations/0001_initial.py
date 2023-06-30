# Generated by Django 4.2.2 on 2023-06-30 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('hex_color', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('cbtc_enabled', models.BooleanField()),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trains', to='subway.line')),
            ],
        ),
        migrations.AddField(
            model_name='line',
            name='stations',
            field=models.ManyToManyField(to='subway.station'),
        ),
    ]