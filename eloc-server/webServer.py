
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import simplejson
import random
import MySQLdb
from dbHandler import *

# Open database connection
db = MySQLdb.connect("localhost","root","root","elocate" )

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print "in get method"
        self._set_headers()
        f = open("index.html", "r")
        self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        data=self.data_string.split('&')
        dict={}
        for i in data:
            dt=i.split('=')
            dict[dt[0]]=dt[1]
            #print 'key: ',dt[0],'  value: ',dt[1]
        print dict

        if 'getLocations' in dict:
            data2=getColomn(db,'location')
            #print data2
            self.wfile.write(simplejson.dumps(data2))
        elif 'getTimestamps' in dict:
            data2=getColomnWhere(db,'time_stamp',dict['getTimestamps'])
            print simplejson.dumps(data2)
            self.wfile.write(simplejson.dumps(data2))
        elif 'getData' in dict:
            print "------------ in getting data------------"
            data2=getData(db, dict['location'], dict['timestamp'])
            self.wfile.write(simplejson.dumps(data2))
        return


def run(server_class=HTTPServer, handler_class=S, port=8002):
    server_address = ('127.0.0.1', port) #10.22.196.21
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()