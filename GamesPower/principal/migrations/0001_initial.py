# Generated by Django 4.0.5 on 2022-08-26 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Usuario')),
                ('producto', models.CharField(max_length=50, verbose_name='Producto')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('creacion', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Comunidad',
                'ordering': ['-creacion'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Llave')),
                ('nombre', models.CharField(max_length=50, verbose_name='Productos')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria')),
                ('existencia', models.CharField(max_length=50, verbose_name='Existencia')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Proveedor')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['-creacion'],
            },
        ),
    ]
