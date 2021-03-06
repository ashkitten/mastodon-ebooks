import markovify
import json
from mastodon import Mastodon

api_base_url = "https://botsin.space"

client = Mastodon(
        client_id="clientcred.secret", 
        access_token="usercred.secret", 
        api_base_url=api_base_url)

with open("corpus.txt") as fp:
    model = markovify.NewlineText(fp.read())

print("Running...")
while True:
    print("tooting")
    # This is not the best long term fix tbh
    sentance = None
    while sentence is None:
        sentence = model.make_sentence()
    client.toot(sentence.replace(chr(31), "\n"))
    print("sleeping")
    time.sleep(60*60*3)
