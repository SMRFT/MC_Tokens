from mct.mct import *
import os, json

def read_data(full_path: str) -> dict:
    with open(full_path, 'r') as f:
        return json.load(f)

def generate_token(data) -> str:
    if 'expiry-days' in data:
        expDays = int(data['expiry-days'])
    else:
        expDays = 30
        data.set('expiry-days', 30)
    return createJwt(data, expDays)

def print_token(data, token):
    print()
    print(f"Token for {data.get('aud')} with expiry {data.get('expiry-days')} days:")
    print(token)
    print()


for entry_name in os.listdir('data'):
    if entry_name.endswith('.json'):
        try:
            full_path = os.path.join('data', entry_name)
            data = read_data(full_path)
            token =  generate_token(data)
            print_token(data, token)
        except Exception as e:
            print(f"Token generation failed for {entry_name}: {e}")


