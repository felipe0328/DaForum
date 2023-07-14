from django.test import TestCase
from apps.forum.models import Category,Subcategory, Thread
from django.urls import reverse_lazy

class FormViewTest(TestCase):
    def create_subcategory(self)->str:
        category_name = "cat_name"
        subcategory_name = "sub_name"

        category = Category.objects.create(name=category_name, need_auth=False)
        Subcategory(name=subcategory_name, category=category).save()
        return subcategory_name

    def test_url_exists(self):
        subcategory_name = self.create_subcategory()
        response = self.client.get(f'/forum/{subcategory_name}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        subcategory_name = self.create_subcategory()
        response = self.client.get(reverse_lazy('forum.subcategory', kwargs={'name': subcategory_name}))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        subcategory_name = self.create_subcategory()
        response = self.client.get(reverse_lazy('forum.subcategory', kwargs={'name': subcategory_name}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/subcategory_detail.html')

class NewFormViewTest(TestCase):
    def create_subcategory(self)->str:
        category_name = "cat_name"
        subcategory_name = "sub_name"

        category = Category.objects.create(name=category_name, need_auth=False)
        Subcategory(name=subcategory_name, category=category).save()
        return subcategory_name

    def test_url_exists(self):
        subcategory_name = self.create_subcategory()
        response = self.client.get(f'/forum/{subcategory_name}/new')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        subcategory_name = self.create_subcategory()
        response = self.client.get(reverse_lazy('forum.createThread', kwargs={'name': subcategory_name}))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        subcategory_name = self.create_subcategory()
        response = self.client.get(reverse_lazy('forum.createThread', kwargs={'name': subcategory_name}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/thread_form.html')

class ThreadViewTest(TestCase):
    def create_subcategory(self)->Subcategory:
        category_name = "cat_name"
        subcategory_name = "sub_name"

        category = Category.objects.create(name=category_name, need_auth=False)
        subcategory = Subcategory.objects.create(name=subcategory_name, category=category)
        return subcategory
    
    def create_newthread(self, subcategory:Subcategory)->Thread:
        thread = Thread.objects.create(subcategory= subcategory,
                                       subject = "some_subject",
                                       name = "name",
                                       email = "email@gma.com", 
                                       message = "some message")
        
        return thread

    def test_url_exists(self):
        subcategory = self.create_subcategory()
        thread = self.create_newthread(subcategory)
        response = self.client.get(f'/forum/{subcategory.name}/thread/{thread.pk}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        subcategory = self.create_subcategory()
        thread = self.create_newthread(subcategory)
        response = self.client.get(reverse_lazy('forum.threadView', kwargs={'name': subcategory.name, 'pk':thread.pk}))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        subcategory = self.create_subcategory()
        thread = self.create_newthread(subcategory)
        response = self.client.get(reverse_lazy('forum.threadView', kwargs={'name': subcategory.name, 'pk':thread.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/thread_detail.html')


class NewThreadViewTest(TestCase):
    def create_subcategory(self)->Subcategory:
        category_name = "cat_name"
        subcategory_name = "sub_name"

        category = Category.objects.create(name=category_name, need_auth=False)
        subcategory = Subcategory.objects.create(name=subcategory_name, category=category)
        return subcategory
    
    def create_newthread(self, subcategory:Subcategory)->Thread:
        thread = Thread.objects.create(subcategory= subcategory,
                                       subject = "some_subject",
                                       name = "name",
                                       email = "email@gma.com", 
                                       message = "some message")
        
        return thread

    def test_url_exists(self):
        subcategory = self.create_subcategory()
        thread = self.create_newthread(subcategory)
        response = self.client.get(f'/forum/{subcategory.name}/thread/{thread.pk}/new')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        subcategory = self.create_subcategory()
        thread = self.create_newthread(subcategory)
        response = self.client.get(reverse_lazy('forum.createThreadResponse', kwargs={'name': subcategory.name, 'pk':thread.pk}))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        subcategory = self.create_subcategory()
        thread = self.create_newthread(subcategory)
        response = self.client.get(reverse_lazy('forum.createThreadResponse', kwargs={'name': subcategory.name, 'pk':thread.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/threadresponse_form.html')