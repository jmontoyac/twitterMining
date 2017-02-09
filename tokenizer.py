import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
import re
import json

#nltk.download('punkt')

tknzr = TweetTokenizer()

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tknzr.tokenize(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 

#tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
#tweet = '{"created_at":"Wed Feb 08 17:13:46 +0000 2017","id":829377694538178560,"id_str":"829377694538178560","text":"Hikari Ichihara applejump tokyo \n#Jazz #singer @ Apple Jump https:\/\/t.co\/UlrcFcVoTf","source":"\u003ca href=\"http:\/\/instagram.com\" rel=\"nofollow\"\u003eInstagram\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":142192183,"id_str":"142192183","name":"seki","screen_name":"applejump2009","location":"\u6771\u4eac\u90fd\u8c4a\u5cf6\u533a\u897f\u6c60\u888b\/Tokyo,Japan","url":"http:\/\/applejump.net\/","description":"Live cafe & bar Apple Jump\u306e\u30de\u30b9\u30bf\u30fc\u3067\u3059\u3002\n\u7acb\u6559\u5927\u5b66\u6c60\u888b\u30ad\u30e3\u30f3\u30d1\u30b9\u96a3\u308a\u3002Small Jazz Club & Acoustic Live Spot w\/YAMAHA GRAND PIANO","protected":false,"verified":false,"followers_count":1077,"friends_count":537,"listed_count":67,"favourites_count":267,"statuses_count":3532,"created_at":"Mon May 10 06:34:42 +0000 2010","utc_offset":32400,"time_zone":"Tokyo","geo_enabled":true,"lang":"ja","contributors_enabled":false,"is_translator":false,"profile_background_color":"BF1238","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme20\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme20\/bg.png","profile_background_tile":false,"profile_link_color":"BF1238","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"EFEFEF","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/440129600799010817\/kN326SCa_normal.png","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/440129600799010817\/kN326SCa_normal.png","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/142192183\/1393770870","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":{"type":"Point","coordinates":[35.73104737,139.70505172]},"coordinates":{"type":"Point","coordinates":[139.70505172,35.73104737]},"place":{"id":"7efb0fd5276fdda5","url":"https:\/\/api.twitter.com\/1.1\/geo\/id\/7efb0fd5276fdda5.json","place_type":"city","name":"\u8c4a\u5cf6\u533a","full_name":"\u6771\u4eac \u8c4a\u5cf6\u533a","country_code":"JP","country":"\u65e5\u672c","bounding_box":{"type":"Polygon","coordinates":[[[139.677525,35.712228],[139.677525,35.745989],[139.752663,35.745989],[139.752663,35.712228]]]},"attributes":{}},"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[{"text":"Jazz","indices":[33,38]},{"text":"singer","indices":[39,46]}],"urls":[{"url":"https:\/\/t.co\/UlrcFcVoTf","expanded_url":"https:\/\/www.instagram.com\/p\/BQQjLDhBdY8\/","display_url":"instagram.com\/p\/BQQjLDhBdY8\/","indices":[60,83]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"in","timestamp_ms":"1486574026127"}'
#print(word_tokenize(tweet))
#tweet_json = json.loads(tweet)
#print(preprocess(tweet_json['text']))

#with open('data/stream_apple.json', 'r') as f:
#    for line in f:
#        tweet = json.loads(line)
#        print(preprocess(tweet['text']))
