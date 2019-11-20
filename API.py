import os, sys, json, requests, configparser

devproj = '1150333541424865'
prodproj = '1146674956832113'
project = devproj

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

def MobileTask(name, device, dtx = 'no', case = 'none'):
    data = {
        'data': {
            'name': name,
            'projects': [
                project
            ]
        }
    }
    data = json.dumps(data)

    parent = json.loads(requests.post(url, headers=headers, data=data).text)
    SubTask(parent['data']['gid'], device, dtx, case, 'Replacement Ordered', 'Inventory Updated')

def SubTask(parent, *subs):
    sublist = []
    
    for sub in subs:
        if sub != 'no' and sub != 'none':
            sublist.append(sub)
    sublist.reverse()
    
    for sub in sublist:
        data = {
            'data': {
                'name': sub
            }
        }
        data = json.dumps(data)

        requests.post(url + '/{}/subtasks'.format(parent), headers=headers, data=data)

MobileTask('Michael Rice', 'iPhone Plus', 'Data Transfer', 'Case: Defender')