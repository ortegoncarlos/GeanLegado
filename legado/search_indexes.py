# import datetime
# from haystack import indexes
# from legado.models import Perfil


# class PerfilIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True, template_name="search/perfil_text.txt")
#     author = indexes.CharField(model_attr='nombre')
#     content_auto = indexes.EdgeNgramField(model_attr='slug')

#     def get_model(self):
#         return Perfil

#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.all()
from django.utils import timezone
from haystack import indexes

from .models import Perfil


class PerfilIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nombre = indexes.EdgeNgramField(model_attr='nombre')
    profesion = indexes.EdgeNgramField(model_attr='profesion')
    imagen = indexes.EdgeNgramField(model_attr='imagen')
    slug = indexes.EdgeNgramField(model_attr='slug')
    fecha_nacimiento = indexes.EdgeNgramField(model_attr='fecha_nacimiento')
    lugar_nacimiento = indexes.EdgeNgramField(model_attr='lugar_nacimiento')
    biografia = indexes.EdgeNgramField(model_attr='biografia')
    id = indexes.EdgeNgramField(model_attr='id')


    #content_auto = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Perfil

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(timestamp__lte=timezone.now())