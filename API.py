import os, sys, json, requests, configparser

url = 'https://app.asana.com/api/1.0/tasks?project=1146674956832113&completed_since=now'
key = ''
config = configparser.ConfigParser()

if not os.path.isfile('config.txt'):
    configFile = open('config.txt', 'w+')
    configFile.write('[Default]\nkey = ')
    configFile.close()
    print('A new config.txt file has been created. Please enter your API key into this file')
    sys.exit()

config.read('config.txt')

if 'Default' in config and 'key' in config['Default']:
    key = config['Default']['key']
else:
    print('config.txt is not properly formatted')
    sys.exit()

if key == '':
    print('API key is missing from config.txt')
    sys.exit()

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + key
    }

print(json.dumps(json.loads(requests.get(url, headers=headers).text), indent=4, sort_keys=True))