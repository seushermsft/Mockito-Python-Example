import urllib.request

# To run, run 'python3 main.py'
class Testing(object):
    def doSomething(self, target):
        contents = urllib.request.urlopen("http://google.com").read()
        return contents

class Tester(object):
    def run(self, testingInstance, target):
        return testingInstance.doSomething(target)

if __name__ == "__main__":
    content = Tester().run(Testing(), "target1")
    print(content)