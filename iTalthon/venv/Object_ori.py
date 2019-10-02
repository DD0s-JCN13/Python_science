class MainContainer(object):
    def __init__(self, name):
        self.name = name
    def printer(self):
        print("Tester name: " + str(self.name))
tester = MainContainer("JCN")
tester.printer()