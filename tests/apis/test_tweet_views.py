# tests/apis/test_tweet_views.py
from flask_testing import TestCase
from app import create_app
from app.models import Tweet
from app.db import repository

class TestTweetViews(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def setUp(self):
        repository.clear()

    def test_tweet_show(self):
        tweet1 = Tweet("First tweet")
        repository.add(tweet1)
        response = self.client.get("/tweets/1")
        response_tweet = response.json
        print(response_tweet)
        self.assertEqual(response_tweet["id"], 1)
        self.assertEqual(response_tweet["text"], "First tweet")
        self.assertIsNotNone(response_tweet["created_at"])
