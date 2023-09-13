import sys

from st2common.runners.base_action import Action


class SimpleScriptAction(Action):
    def run(self):
        self.logger.info(f"This is my simple script! Cool!")
        self.action_service
        return True, "Success!"

