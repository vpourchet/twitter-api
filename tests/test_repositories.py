# tests/test_repositories.py
from unittest import TestCase
from app.models import Repository, Tweet

class TestRepository(TestCase):
    def test_instance_variables(self):
        repository = Repository()
        self.assertEqual(len(repository.tweets), 0)
    def test_add(self):
        repository = Repository()
        tweet = Tweet("Coucou petite perruche.")
        repository.add(tweet)
        self.assertEqual(len(repository.tweets), 1)
    def test_increment_id(self):
        repository = Repository()
        tweet1 = Tweet("Ah que coucou.")
        repository.add(tweet1)
        self.assertEqual(tweet1.id, 1)
        tweet2 = Tweet("Tirelipimpon sur le Chihuahua.")
        repository.add(tweet2)
        self.assertEqual(tweet2.id, 2)

