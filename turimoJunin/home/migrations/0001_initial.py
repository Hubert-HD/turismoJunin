# Generated by Django 3.2.4 on 2021-06-29 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('image_URL', models.URLField(blank=True)),
                ('subtitulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categoria')),
                ('distrito_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.distrito')),
            ],
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.provincia'),
        ),
        migrations.CreateModel(
            name='Coordenadas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('recurso_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.recurso')),
            ],
        ),
    ]
