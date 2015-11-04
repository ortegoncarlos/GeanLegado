from django import template
from django.shortcuts import render_to_response , get_object_or_404
from django.template import RequestContext
from blog.models import Post,Hero, Circles, Featured,Sedes, Schedule


register = template.Library()


@register.filter(name='eventfilt')
def eventfilt(value,id):
		return value.filter(schedule=id)

@register.filter(name='hex_to_rgb')
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    if lv == 0:
        pass
    else:
        return tuple(int(value[i:i + lv // 3 ], 16 ) for i in range(0, lv, lv // 3))+(0.4,)

@register.filter(name='rgb_to_hex')
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb