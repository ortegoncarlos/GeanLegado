from rest_framework import serializers

from .models  import Perfil

class PerfilSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
 		model = Perfil
 		fields = ('id','nombre','fecha_nacimiento','lugar_nacimiento','imagen','profesion','biografia','origen_apellido','qrcode','slug',
 )
