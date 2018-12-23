
# coding:UTF-8
from wsgiref import simple_server

import random
from IdiomPair import Idiom, IdiomPair


class IdiomGameServer():
    def __init__(self):
        self.commonHeader = [('Content-Type', 'text/html')]
        self.RESP_CODE_OK = "200 OK"

    def getRoundData(self, environ, start_response):
        with open("terminalVer/goodIdiomPair.txt", "r", encoding="utf-8") as fp:
            try:
                n = int(environ['QUERY_STRING'].split('=')[1])
            except ValueError:
                start_response(self.RESP_CODE_OK, self.commonHeader)
                return ["Parameter Error".encode("UTF-8")]
            line1 = line2 = ""
            while n > 0:
                line1 = fp.readline()
                line2 = fp.readline()
                n -= 1
        start_response(self.RESP_CODE_OK, self.commonHeader)
        line1 = line1.strip("\n"); line2 = line2.strip("\n")
        # line1 = line1.encode("utf-8"); line2 = line2.encode("utf-8")
        bs = (line1 + "\n" + line2).encode("utf-8")
        return [bs]

    def getUserRound(self, environ, start_response):
        start_response(self.RESP_CODE_OK, self.commonHeader)
        a = random.randint(1, 100)
        return [str(a).encode("utf-8")]

    def parseGetPara(self, environ, start_response):
        path = environ['PATH_INFO']
        if path == "/getRoundData":
            return self.getRoundData(environ, start_response)
        elif path == "/getUserRound":
            return self.getUserRound(environ, start_response)
        else:
            start_response("404 Not Found", [('Content-Type', "text/html")])
            return ["Path Not Found, Plaese Check.".encode("UTF-8")]

    def startServer(self):
        httpd = simple_server.make_server("", 8000, self.parseGetPara)
        print("Server start at 8000")
        httpd.serve_forever()
        pass


if __name__ == "__main__":
    IdiomGameServer().startServer()
