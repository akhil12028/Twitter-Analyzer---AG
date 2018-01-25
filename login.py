from user import User
from database import Database
from twitter_utils import get_request_token,get_verifier,get_access_token

Database.initialise(user='postgres',password='akhil',database='learning',host='localhost')

user_email = input('Enter Email: ')
user = User.load_from_db_by_email(user_email)

if not user:
    request_token = get_request_token()
    oauth_verifier = get_verifier(request_token)
    access_token = get_access_token(request_token,oauth_verifier)

    first_name = input('Enter First name: ')
    last_name = input('Enter Last Name: ')

    user = User(user_email,first_name,last_name,access_token['oauth_token'],access_token['oauth_token_secret'],None)
    user.save_to_db()

tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')

for tweet in tweets['statuses']:
    print(tweet['text'])