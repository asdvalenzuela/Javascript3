from HTMLParser import HTMLParser

class myHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = ""

    def handle_starttag(self, tag, attrs):
        print tag
    def handle_endtag(self, tag):
        print tag
    def handle_data(self, data):
        print data

parser = myHTMLParser()
print(parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>'))