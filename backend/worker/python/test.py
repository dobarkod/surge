import requests

def run():
    resp = requests.get('http://54.228.182.3/api/v1/rates/daily/', headers={
        'Host': 'hnbex.eu'
    })
    if resp.status_code != 200:
        raise Exception('Unexpected status code %d' % resp.status_code)

if __name__ == '__main__':
    run()
