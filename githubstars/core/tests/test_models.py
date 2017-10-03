import unittest
from core.models import Repository


class RepositoryTestCase(unittest.TestCase):
    """ Test using correct data """
    def testCreateProject(self):
        Repository.objects.create(repository_id=123456,
                                  name='Testde de Projeto',
                                  url='https://github.com/brainnco/challenge-for-developers',
                                  language='Python')

    def testSelectProject(self):
        Repository.objects.get(repository_id=123456)

    def testUpdateProject(self):
        project = Repository.objects.get(repository_id=123456)
        project.tags = 'js,css,html'
        project.save()
