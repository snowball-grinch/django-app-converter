from django.test import TestCase, Client
# Client class:  This is a testing browser that enables us to make http requests within Django tests.
from django.urls import reverse
# reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)
# viewname can be a URL pattern name or the callable view object
# ......
#  using the named URL:
# reverse('news-archive')

#  passing a callable object
#  (This is discouraged because you can't reverse namespaced views this way.)
# from news import views
# reverse(views.archive)"""
# The reverse function is imported in order to return a url when the url’s name is passed in as an argument.


class TestLengthConversion(TestCase):
    """
    This class contains tests that convert measurements from one
    unit of measurement to another.
    """
    def setUp(self):
        """
        This method runs before the execution of each test case.
        """
        self.client = Client()
        self.url = reverse("length:convert")

    def test_centimetre_to_metre_conversion(self):
        """
        Tests conversion of centimetre measurements to metre.
        """
        data = {
               "input_unit": "centimetre",
               "output_unit": "metre",
               "input_value": round(8096.894, 3)
           }
        response = self.client.get(self.url, data)
        self.assertContains(response, 80.969)
