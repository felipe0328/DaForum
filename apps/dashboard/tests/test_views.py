from django.test import TestCase
from django.urls import reverse_lazy

class DashboardViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('dashboard'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse_lazy('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

class LoginViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/login.html')

class LogoutViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('logout'))
        self.assertEqual(response.status_code, 302)

class SignupViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('signup'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse_lazy('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/register.html')