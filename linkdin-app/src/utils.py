import json

def save_file(file_path, text):
    with open(file_path, 'w') as f:
        f.write(str(text))
        
def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)