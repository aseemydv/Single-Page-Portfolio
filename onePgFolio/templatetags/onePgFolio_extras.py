from django import template
register = template.Library()

@register.filter(name='ccat')
def string_concat(a1,a2):
    ''' concatenates arguments a1 and a2 '''
    return str(a1) + str(a2)

@register.filter(name='stringify')
def stringify(content):
    ''' returns the passed argument as string '''
    return str(content)

        
    