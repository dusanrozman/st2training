import sys

from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message):
        print(message)
        return (True, message)

#        if "deviceIP" in message:  # == 'working':
#            return (True, message)
#        return (False, message)
