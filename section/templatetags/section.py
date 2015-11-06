from django import template

register = template.Library()

@register.inclusion_tag('sections/sections.html')
def show_sections(sections):
    return {
        'sections': sections
    }
