import pytest
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.test import TestCase
from applications.emplois.models import Job

def create_poll(question, days):
    """
    Creates a poll with the given `question` published the given number of
    `days` offset to now (negative for polls published in the past,
    positive for polls that have yet to be published).
    """
    pass

class PollViewTests(TestCase):
    def test_index_view_with_no_polls(self):
        """
        If no polls exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('emplois:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

@pytest.mark.django_db
def test_about_views(client):
    response = client.get('/about')
    assert response.status_code == 200

