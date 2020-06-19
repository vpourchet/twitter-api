from datetime import datetime
from app import db

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Tweet #{self.id}>"

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
