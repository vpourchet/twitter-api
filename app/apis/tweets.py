# app/apis/tweets.py
from flask_restx import Namespace, Resource, fields
from app.db import repository

api = Namespace('tweets')

tweet = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime
})

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'Tweet id')
@api.param('text', 'Tweet text')
@api.param('created_at', 'Tweet creation date')
class TweetResource(Resource):
    @api.marshal_with(tweet)
    def get(self, id):
        tweet = repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet
    @api.marshal_with(tweet)
    def post(self, tweet):
        if tweet is None:
            api.abort(404)
        else:
            repository.post(tweet)
            return repository.get(tweet.id)
    @api.marshal_with(tweet)
    def delete(self, tweet):
        if tweet is None:
            api.abort(404)
        else:
            repository.delete(tweet)
            return 200
    @api.marshal_with(tweet)
    def patch(self, tweet):
        if tweet is None:
            api.abort(404)
        else:
            for tweet in repository.tweets:
                if tweet == tweet:
                    repository.tweets[tweet.id] = tweet
            return 200

