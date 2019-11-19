import os, sys, json, requests, configparser

devproj = '1150333541424865'
prodproj = '1146674956832113'

url = 'https://app.asana.com/api/1.0/tasks'
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
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + key
    }

data = {
    'data': {
        'name': 'Test Task',
        'projects': [
            devproj
        ]
    }
}
data = json.dumps(data)

subdata = {
    'data': {
        'name': 'Test Subtask'
    }
}
subdata = json.dumps(subdata)

parent = json.loads(requests.post(url, headers=headers, data=data).text)
requests.post(url + '/{}/subtasks'.format(parent['data']['gid']), headers=headers, data=subdata)