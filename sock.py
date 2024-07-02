#coding=utf-8
#author=MRY
#releasedtime=2024.7.2

#A local http server.
import socketserver
import http.server
import logging
import cgi
import os

conf=False
while not conf:
    targ=input('输入路径\n:')
    conf=bool(input(f'确认路径:{targ}\n y / n:'))
    if not os.path.exists(targ):
        print('路径不存在,',end='')
        continue
    if conf=='y' or conf=='Y':
        conf=True
os.chdir(targ)

PORT = 80

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

        with open("data.txt", "w") as file:
            for key in form.keys(): 
                file.write(str(form.getvalue(str(key))) + ",")

Handler = ServerHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()