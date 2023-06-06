from controller.base import IValidation
import regex

class Op3(IValidation):


    def check_error(self,expression):



        operators_pattern = r'(\([*\/^%])'

        matches = regex.findall(operators_pattern,expression)

        if matches:
            for match in matches:
                self.error_handler.set_error('Syntax Error : Invalid Operator '+match)
        return self.successor.check_error(expression)



    def set_successor(self,successor):

        self.successor  = successor

    def set_error_handler(self,handler):
        self.error_handler = handler