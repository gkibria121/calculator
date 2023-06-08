from sk_calculator import Calculator
import regex
class VariableHandler:

    def __init__(self):

        self.calculator = Calculator()


    def declare(self,declarations):


        declarations = list(filter(None, regex.split(r'[;,]',declarations)))


        self.declaration_list = {}

        for declaration in declarations:
            declaration = list(filter(None, regex.split(r'\$?([^=]+)=',declaration)))
            variable =declaration[0]
            expression =declaration[1]

            if variable in self.declaration_list:
                print( f"Variable already exist : {variable}")
            else:

                self.declaration_list[variable] = expression

        print(self.declaration_list)



    def get_values(self):

        for variable,expression in self.declaration_list.items():

            self.declaration_list[variable]=self.calculator.evaluate(expression)
        print(self.declaration_list)










variable = VariableHandler()

variable.declare('$x=1+2; $y=2+1; $var =12+223+(222+2); $var2= $x + $y+$var3 = ($var2+$x+$y)')





