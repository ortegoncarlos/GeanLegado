from django import forms
from django.forms import CheckboxInput
from haystack.forms import SearchForm
from .models import Perfil
from django import forms
from sanjose_project.settings import PALABRAS_INAPROPIADAS,EXPRESION_REGULAR_URL,MENSAJE_URLS
import re
from django.core.mail import send_mail
from django.forms.fields import FileField
from audiofield.widgets import CustomerAudioFileWidget

class PerfilSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()


class PerfilForm(forms.ModelForm):
    audio_file = forms.FileField(widget=CustomerAudioFileWidget)
    class Meta:
        model = Perfil
        fields = ['nombre','fecha_nacimiento','lugar_nacimiento','imagen','profesion','biografia','origen_apellido','slug','audio_file','listo']

        widgets = {
            'listo': CheckboxInput(attrs={'hidden': 'hidden'})
            }

    def clean_biografia(self):
            biografia = self.cleaned_data['biografia']
            texto =str(biografia)
            urls = re.findall(EXPRESION_REGULAR_URL, texto)
            if urls.__len__() > 0:

                send_mail('Aqui va el asunto',MENSAJE_URLS, 'rmazahares@uci.cu',
                 ['rmazahares@uci.cu'], fail_silently=False)

                raise forms.ValidationError("Existe una url")
            for palabra in PALABRAS_INAPROPIADAS:
                if texto.find(palabra) > 0:
                    raise forms.ValidationError('Hay una mala palabra')

            return biografia
