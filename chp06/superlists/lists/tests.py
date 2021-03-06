from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from lists.models import ListItem,List
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('lists/home.html')
        self.assertEqual(response.content.decode(), expected_html)

    # def test_home_page_displays_all_list_items(self):
    #     ListItem.objects.create(text='itemey 1')
    #     ListItem.objects.create(text='itemey 2')
    #
    #     request = HttpRequest()
    #     response = home_page(request)
    #
    #     self.assertIn('itemey 1', response.content.decode())
    #     self.assertIn('itemey 2', response.content.decode())

    # def test_home_page_can_save_a_POST_request(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = home_page(request)
    #
    #     self.assertEqual(ListItem.objects.count(), 1)
    #     new_item = ListItem.objects.first()
    #     self.assertEqual(new_item.text, 'A new list item')
    # def test_home_page_redirects_after_POST(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = home_page(request)
    #
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    # def test_home_page_only_saves_items_when_necessary(self):
    #     request = HttpRequest()
    #     home_page(request)
    #     self.assertEqual(ListItem.objects.count(), 0)



class ListAndItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_=List()
        list_.save()

        first_item = ListItem()
        first_item.text = 'The first (ever) list item'
        first_item.list=list_
        first_item.save()

        second_item = ListItem()
        second_item.text = 'Item the second'
        second_item.list=list_
        second_item.save()

        saved_list=List.objects.first()
        self.assertEqual(saved_list,list_)

        saved_items = ListItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list,list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list,list_)

class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
        '/lists/new',
        data={'item_text': 'A new list item'}
        )
        self.assertEqual(ListItem.objects.count(), 1)
        new_item = ListItem.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response=self.client.post(
        '/lists/new',
        data={'item_text':'A new list item'})
        new_list=List.objects.first()
        self.assertRedirects(response,'lists/%d/'%(new_list.id,))

    def test_can_save_a_post_request_to_an_existing_list(self):
        other_list=List.objects.create()
        correct_list=List.objects.create()

        self.client.post(
        '/lists/%d/add_item'%(correct_list.id,),
        data={'item_text':'A new item for an existing list'})
        self.assertEqual(ListItem.objects.count(),1)
        new_item=ListItem.objects.first()
        self.assertEqual(new_item.text,'A new item for an existing list')
        self.assertEqual(new_item.list,correct_list)

    def test_redirects_to_list_view(self):
        other_list=List.objects.create()
        correct_list=List.objects.create()
        response=self.client.post(
        '/lists/%d/add_item'%(correct_list.id,),
        data={'item_text':'A new item for an existing list'})
        self.assertRedirects(response,'/lists/%d/'%(correct_list.id,))



class ListViewTest(TestCase):
    def test_uses_list_template(self):
        list_=List.objects.create()
        response = self.client.get('/lists/%d/'%(list_.id))
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        ListItem.objects.create(text='itemey 1', list=correct_list)
        ListItem.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        ListItem.objects.create(text='other list item 1', list=other_list)
        ListItem.objects.create(text='other list item 2', list=other_list)
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')

    def test_passes_correct_list_to_template(self):
        other_list=List.objects.create()
        correct_list=List.objects.create()
        response=self.client.get('/lists/%d/'%(correct_list.id,))
        self.assertEqual(response.context['list'],correct_list)
    # def test_displays_all_items(self):
    #     list_ = List.objects.create()
    #     ListItem.objects.create(text='itemey 1', list=list_)
    #     ListItem.objects.create(text='itemey 2', list=list_)
    #     response = self.client.get('/lists/the-only-list-in-the-world/') #
    #     self.assertContains(response, 'itemey 1')
    #     self.assertContains(response, 'itemey 2')
