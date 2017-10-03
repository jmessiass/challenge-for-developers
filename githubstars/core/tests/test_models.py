import unittest
from core.models import Repositorie


class RepositorieTestCase(unittest.TestCase):
    def testInsert(self):
        self.insert = Repositorie.objects.create(repositorie_id=11, name='')
