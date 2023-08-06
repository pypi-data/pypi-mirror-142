from django.test import TestCase  # noqa
from django.utils import timezone

from .models import Profile, Tool

# Create your tests here.


class toolTest(TestCase):
    def test_create_tool(self):
        author = Profile.objects.get(id=1)

        seaf = Tool.objects.create(
            name="name",
            connector="SeafileConnector",
            author=author,
            date_created=timezone.now(),
        )
        self.assertIs(seaf.get_connector(), "seafile")
