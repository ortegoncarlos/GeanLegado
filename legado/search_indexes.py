import datetime
from haystack import indexes
from legado.models import Perfil


class PerfilIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/perfil_text.txt")
    author = indexes.CharField(model_attr='nombre')
    content_auto = indexes.EdgeNgramField(model_attr='slug')

    def get_model(self):
        return Perfil

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()