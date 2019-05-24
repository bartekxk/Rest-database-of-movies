from django.test import TestCase
from .models import Comments,Movies
from datetime import date

class ModelTestCase(TestCase):
    def setUp(self):
        self.comment=Comments()
        self.comment.Movie_ID=0
        self.comment.Context="test"
        self.comment.Date = date.today
    def test_create_comment(self):
        pass