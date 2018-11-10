import json
import csv
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.tone_analyzer_v3 import ToneInput

service = ToneAnalyzerV3(
	version='2017-09-21',
    iam_apikey='1EGdwW8r7x06l1P4NqAWUYGgMuKrBnyHzGmYxW7AVOoJ',
    url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api'
)

tweetFile = open("data/tweets.csv")
tweets = {}
tones = {}
all_avgs = {}
for row in csv.reader(tweetFile):
	tweets[row[0]] = row[1:]
	tweetJsons = []
	for tweet in tweets[row[0]]:
		tweetJsons.append({'text':tweet})
	tones[row[0]] = service.tone_chat(tweetJsons).get_result()
	avgs = {}
	for utterance in tones[row[0]]['utterances_tone']:
		for i in range(len(utterance['tones'])):
			if utterance['tones'][i]['tone_id'] not in avgs:
				avgs[utterance['tones'][i]['tone_id']] = utterance['tones'][i]['score'] / len(tones[row[0]]['utterances_tone'])
			else:
				avgs[utterance['tones'][i]['tone_id']] += utterance['tones'][i]['score'] / len(tones[row[0]]['utterances_tone'])
	all_avgs[row[0]] = avgs
print(all_avgs)
maxes = {}
for player in all_avgs:
	maxes[player] = max(all_avgs[player].keys())
print(maxes)

'''
print("\ntone_chat() example 1:\n")
utterances = [{
    'text': 'I am very happy.',
    'user': 'glenn'
}, {
    'text': 'It is a good day.',
    'user': 'glenn'
}]
tone_chat = service.tone_chat(utterances).get_result()
print(json.dumps(tone_chat, indent=2))
'''
