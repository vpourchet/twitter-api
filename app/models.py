from datetime import datetime
from app import db
from sqlalchemy.schema import ForeignKey

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = db.relationship("User", back_populates="tweets")

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

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(200))
    api_key = db.Column(db.String(80))
    tweets = db.relationship('Tweet', back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"
