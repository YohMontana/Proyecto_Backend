from rest_framework import serializers
from .models import Productos, Categorias, UsuarioModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'




class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productos
        fields = '__all__'
     

class MostrarProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields= '__all__'
       
class CrearProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields= '__all__'
        


class CategoriaConProductosSerializer(serializers.ModelSerializer):
    # source > sirve para indicar que atributo del modelo tengo que utilizar para hacer que funcione, sin embargo si utilizamos el atributo original no es necesario colocar el source (porque dara un error de redundancia)
    producto = CrearProductoSerializer(many=True, source='productos')
    class Meta:
        model = Categorias
        fields = '__all__'
        
        
class EliminarProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields= '__all__'


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UsuarioModel
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }
