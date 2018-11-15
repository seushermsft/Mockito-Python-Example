import urllib.request

# To run, run 'python3 main.py'
class Testing(object):
    def doSomething(self, target):
        contents = urllib.request.urlopen("http://google.com").read()
        return contents

if __name__ == "__main__":
    content = Testing().doSomething("target1")
    print(content)