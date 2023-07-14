from django.test import TestCase
from apps.forum.models import Category, Subcategory

class CategoryModelTest(TestCase):
    def test_category_model(self):
        category_name = "cat_name"
        category_needs_auth = False

        category = Category.objects.create(
            name = category_name,
            need_auth = category_needs_auth,
        )

        self.assertTrue(isinstance(category, Category))
        self.assertIsNotNone(category.pk)
        self.assertEqual(category_name, category.name)
        self.assertEqual(category_needs_auth, category.need_auth)

class SubcategoryModelTest(TestCase):
    def test_subcategory_model(self):
        category_name = "cat_name"
        category_needs_auth = False

        category = Category.objects.create(
            name = category_name,
            need_auth = category_needs_auth,
        )

        subcategory_name = "sub_name"
        subcategory = Subcategory.objects.create(
            name = subcategory_name,
            category = category            
        )

        self.assertTrue(isinstance(subcategory, Subcategory))
        self.assertIsNotNone(subcategory.pk)
        self.assertEqual(subcategory_name, subcategory.name)
        self.assertEqual(category, subcategory.category)

