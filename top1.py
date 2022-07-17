import requests
import urllib.parse
import sys

choices1 = ['Male', 'Female']
choices2 = ['difficulty5', 'difficulty4',
            'difficulty3', 'difficulty2', 'difficulty1']
choices3 = ['quality5', 'quality4',
            'quality3', 'quality2', 'quality1']
choices4 = [
    'Eyes or vision', 'Head or neck', 'Breathing', 'Heart or cardiovascular',
    'Abdominal or digestion', 'Genital or urinary',
    'Abnormal bleeding or bruising', 'Neurological', 'Joint or muscular',
    'Mental health', 'Skin or hair', 'Whole body']

def printId(c1, c2, c3, c4):
    url = ('https://www.crowdmed.com/cases?pick=&seed=&sort=random&filters='
           '{}|{}|{}|{}'.format(c1, c2, c3, urllib.parse.quote(c4)))
    print(url, file=sys.stderr)
    r = requests.get(url)
    json = r.json()
    for case in json['medcases']:
        print(case['id'])

for c1 in choices1:
    for c2 in choices2:
        for c3 in choices3:
            for c4 in choices4:
                printId(c1, c2, c3, c4)
