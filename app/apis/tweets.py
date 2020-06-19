# app/apis/tweets.py
from flask_restx import Namespace, Resource, fields
from flask import abort
from app.db import repository
from app.models import Tweet

api = Namespace('tweets')

json_tweet = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime
})

json_new_tweet = api.model('New tweet', {
    'text': fields.String(required=True)
})


@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'Tweet id')
@api.param('text', 'Tweet text')
@api.param('created_at', 'Tweet creation date')
class TweetResource(Resource):
    @api.marshal_with(json_tweet)
    def get(self, id):
        tweet = repository.get(id)
        if tweet is None:
            api.abort(404, "Tweet {} doesn't exist".format(id))
        else:
            return tweet
    @api.marshal_with(json_tweet, code=201)
    @api.expect(json_new_tweet, validate=True)
    def post(self):
        text = api.payload["text"]
        if len(text) > 0:
            tweet = Tweet(text)
            repository.add(tweet)
            return tweet, 201
        else:
            return abort(422, "Tweet text can't be empty")
    @api.marshal_with(tweet)
    def delete(self, id):
        tweet = repository.get(id)
        if tweet is None:
            api.abort(404, "Tweet {} doesn't exist".format(id))
        else:
            repository.remove(id)
            return None
    @api.marshal_with(json_tweet, code=200)
    @api.expect(json_new_tweet, validate=True)
    def patch(self, id):
        tweet = repository.get(id)
        if tweet is None:
            api.abort(404, "Tweet {} doesn't exist".format(id))
        else:
            tweet.text = api.payload["text"]
            return tweet
