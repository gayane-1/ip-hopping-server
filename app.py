import subprocess
from flask import Flask, request

app = Flask(__name__)

def change_ip(new_ip):
    subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'address', 'name="Ethernet"', 'static', new_ip, '255.255.255.0'])

@app.route('/change_ip', methods=['POST'])
def change_ip_route():
    new_ip = request.form['new_ip']
    change_ip(new_ip)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
