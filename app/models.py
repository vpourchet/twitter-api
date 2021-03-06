from datetime import datetime
class Tweet:
    def __init__(self, text):
        self.id = None
        self.text = text
        self.created_at = datetime.now()

class Repository:
    def __init__(self):
        self.clear()
    def add(self, tweet):
        self.tweets.append(tweet)
        tweet.id = self.next_id
        self.next_id += 1
    def get(self, id):
        for tweet in self.tweets:
          if tweet.id == id:
              return tweet
        return None
    def clear(self):
        self.tweets = []
        self.next_id = 1
    def remove(self, id):
        self.tweets = [tweet for tweet in self.tweets if tweet.id != id]
