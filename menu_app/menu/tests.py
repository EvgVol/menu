from django.test import TestCase
from django.urls import reverse

from menu.models import MenuItem
from menu.templatetags.menu_tags import render_menu, draw_menu


class MenuTestCase(TestCase):
    def setUp(self):
        self.root_menu = MenuItem.objects.create(name='Root Menu',
                                                 url='/root/',
                                                 parent=None)
        self.child_menu = MenuItem.objects.create(name='Child Menu',
                                                  url='/child/',
                                                  parent=self.root_menu)
        self.grandchild_menu = MenuItem.objects.create(name='Grandchild Menu',
                                                       url='/grandchild/',
                                                       parent=self.child_menu)

    def test_render_menu(self):
        menu_html = render_menu([self.root_menu], '/root/')
        self.assertInHTML('<a href="/root/" class="active">Root Menu</a>', menu_html)
        self.assertInHTML('<a href="/child/" class="">Child Menu</a>', menu_html)
        self.assertInHTML('<a href="/grandchild/" class="">Grandchild Menu</a>', menu_html)

    def test_draw_menu_tag(self):
        menu_html = draw_menu('Root Menu', '/root/')
        self.assertInHTML('<a href="/root/" class="active">Root Menu</a>', menu_html)
        self.assertInHTML('<a href="/child/" class="">Child Menu</a>', menu_html)
        self.assertInHTML('<a href="/grandchild/" class="">Grandchild Menu</a>', menu_html)

    def test_get_absolute_url(self):
        self.assertEqual(self.root_menu.get_absolute_url(), '/root/')
        self.assertEqual(self.child_menu.get_absolute_url(), '/child/')
        self.assertEqual(self.grandchild_menu.get_absolute_url(), '/grandchild/')

    def test_menu_view(self):
        response = self.client.get(reverse('menu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')
