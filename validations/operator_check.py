from controller.base import IValidation
import regex

class OperatorErrorChecker(IValidation):


    def check_error(self,expression):



        operators_pattern = r'([\d\.]+)((?:[(+-][*^/])|(?:[+-][*^/)]))'
        matches = regex.findall(operators_pattern,expression)

        if  matches:
            for match in matches:
                self.error_handler.set_error('Syntax Error : Invalid Operators '+match[0]+match[1])


        operators_pattern = r'[\d\d.]+(?:[\s)]+[\d\.])+'
        matches = regex.findall(operators_pattern,expression)

        if  matches:
            for match in matches:
                self.error_handler.set_error('Syntax Error : Invalid Operators '+match.replace(' ','?'))

        operators_pattern = '(log)?(\d+(?:\.\d+)?)\((\d+(?:\.\d+)?)'

        matches = regex.findall(operators_pattern,expression)

        if matches:
            for match in matches:
                if match[0] == 'log':
                    pass
                else:
                    self.error_handler.set_error('Syntax Error : Missing Operator '+match[1]+'?('+match[2])
        operators_pattern = r'(\([*\/^])'

        matches = regex.findall(operators_pattern,expression)

        if matches:
            for match in matches:
                self.error_handler.set_error('Syntax Error : Invalid Operator '+match)




        return self.successor.check_error(expression)



    def set_successor(self,successor):

        self.successor  = successor

    def set_error_handler(self,handler):
        self.error_handler = handler