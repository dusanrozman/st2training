import sys

from st2common.runners.base_action import Action


class AddNumbersAction(Action):
    def run(self, num1: int, num2):
        self.logger.info(f"num1: {num1} and num2:{num2}")
        self.logger.info(f"Config: {self.config}")
        if num1 and num2:
            return True, f"{num1 + num2}"
        return False, "no numbers given"
