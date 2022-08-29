from django.db import models

# Create your models here.

class Producto(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="Llave")
    nombre= models.CharField(max_length=50, verbose_name="Productos")
    categoria= models.CharField(max_length=50, verbose_name="Categoria")
    existencia= models.CharField(max_length=50, verbose_name="Existencia")
    descripcion= models.TextField(verbose_name="Descripcion")
    imagen= models.ImageField(null= True, upload_to="fotos", verbose_name="Imagen")
    created= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "Producto"
        verbose_name_plural="Productos"
        ordering= ["-created"]

    def __str__(self):
        return self.nombre


class Proveedores(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    nombre= models.CharField(max_length=50, verbose_name="Proveedor")
    mensaje= models.TextField(verbose_name="Mensaje")
    archivo= models.FileField(upload_to="archivos", null=True, blank=True)
    creacion= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= "Proveedor"
        verbose_name_plural= "Proveedores"
        ordering= ["-creacion"]

    def __str__(self):
        return self.nombre


class Comunidad(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="ID")
    nombre= models.CharField(max_length=50, verbose_name="Usuario")
    producto= models.CharField(max_length=50, verbose_name="Producto")
    mensaje= models.TextField(verbose_name="Mensaje")
    creacion= models.DateField(auto_now_add=True)

    class Meta:
        verbose_name= "Comunidad"
        ordering= ["-creacion"]

    def __str__(self):
        return self.nombre
