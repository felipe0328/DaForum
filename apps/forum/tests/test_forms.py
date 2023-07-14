from django.test import TestCase
from apps.forum.forms import ThreadForm, ThreadResponseForm

class ThreadFormTests(TestCase):
    def test_create_form(self):
        form = ThreadForm()
        self.assertIsNotNone(form.fields['subject'])
        self.assertIsNotNone(form.fields['name'])
        self.assertIsNotNone(form.fields['email'])
        self.assertIsNotNone(form.fields['message'])
        self.assertIsNotNone(form.fields['image'])
        self.assertIsNone(form.fields.get('pk'))
        self.assertIsNone(form.fields.get('subcategory'))
        self.assertIsNone(form.fields.get('created'))

class ThreadResponseFormTests(TestCase):
    def test_create_form(self):
        form = ThreadResponseForm()
        self.assertIsNotNone(form.fields['user'])
        self.assertIsNotNone(form.fields['response'])
        self.assertIsNone(form.fields.get('pk'))
        self.assertIsNone(form.fields.get('thread'))
        self.assertIsNone(form.fields.get('created'))
