from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_backend():
    return 'Hello Backend, is on maintance 🙃  syncing with github. Testing 2'

@app.route('/webhook-handler', methods=['POST'])
def webhook_handler():
    data = request.json
    if data['ref'] == 'refs/heads/main':  # Adjust according to your branch
        pull_changes()
    return '', 200

def pull_changes():
    repo_path = '/home/ec2-user/sample/sample'
    os.chdir(repo_path)
    subprocess.run(['git', 'pull', 'origin', 'main'])  # Adjust according to your branch

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
