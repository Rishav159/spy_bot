import subprocess
from bottle import run, post, request, response, get, route
from bottle import static_file
import serial,time
# arduino = serial.Serial('COM3',9600,timeout=.1)

@route('/',method='GET')
def index():
    return static_file('index.html',root='static/')

@route('/controller',method='GET')
def controller():
    return static_file('controller.html',root='static/')

@route('/static/<filename>',method='GET')
def serve_static(filename):
    return static_file(filename,root='static/')
@route('/senddata/<data>',method='GET')
def senddata(data):
    # arduino.write(data.encode())
    print(data)
run(host='localhost', port=8080, debug=True)
