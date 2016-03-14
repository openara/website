'''
Created on 19 nov. 2015

@author: biodigitals
'''
from apetizer.models import Item
from django.template.defaulttags import register

@register.inclusion_tag('openara/tags/list_acteurs.html', takes_context=True)
def list_acteurs(context):
    context['acteurs'] = Item.objects.get_at_url('/'+context['currentNode'].get_root().slug+'/les-acteurs/', exact=False).get_children().order_by('?')
    return context