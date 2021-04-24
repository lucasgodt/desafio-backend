# Generated by Django 3.2 on 2021-04-24 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_uf', models.SmallIntegerField()),
                ('uf', models.CharField(max_length=2)),
                ('nome', models.CharField(max_length=20)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8)),
            ],
            options={
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ibge', models.CharField(max_length=8)),
                ('nome', models.CharField(max_length=40)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('capital', models.BooleanField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='cidades.state')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
