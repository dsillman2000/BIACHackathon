import json
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.tone_analyzer_v3 import ToneInput

service = ToneAnalyzerV3(
	version='2017-09-21',
    iam_apikey='1EGdwW8r7x06l1P4NqAWUYGgMuKrBnyHzGmYxW7AVOoJ',
    url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api'
)

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