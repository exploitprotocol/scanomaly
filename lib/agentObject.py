#This class can be used to modify user-agents
from lib.fileOp import FileOp
import random

class UserAgent:

    #Initialize our object with list of requests to make
    def __init__(self, reqList, cwd):
        self.agents = FileOp(cwd+'/lists/user-agents.txt').reader()
        self.reqList = reqList.copy()

    #Change all requests to a single agent
    def agentlist(self):
        someAgent = self.randomAgent()
        for i in self.reqList:
            new_h = i.headers.copy()
            new_h['User-Agent'] = someAgent
            i.headers = new_h.copy()
        return self.reqList

    #Change all requests to a random agent
    def agentran(self):
        for i in self.reqList:
            new_h = i.headers.copy()
            new_h['User-Agent'] = self.randomAgent()
            i.headers = new_h.copy()
        return self.reqList

    #Return a random user agent
    def randomAgent(self):
        return random.choice(self.agents)
