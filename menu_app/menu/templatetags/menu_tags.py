from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name, current_path):
    menu_items = MenuItem.objects.filter(
        name=menu_name, parent__isnull=True
    ).prefetch_related('children')
    return render_menu(menu_items, current_path)


def render_menu(menu_items, current_path):
    menu_html = '<ul>'
    for item in menu_items:
        menu_html += '<li>'
        active_class = 'active' if current_path == item.get_absolute_url() else ''
        menu_html += f'<a href="{item.get_absolute_url()}" class="{active_class.strip()}">{item.name}</a>'
        child_menu_items = item.children.all()
        if child_menu_items:
            menu_html += render_menu(child_menu_items, current_path)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html