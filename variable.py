from sk_calculator import Calculator
import regex
class VariableHandler:

    def __init__(self):

        self.calculator = Calculator()
        self.simple_variable = {}
        self.complex_variable = {}


    def declare(self,declarations):


        declarations = list(filter(None, regex.split(r'[;,]',declarations)))

        self.declaration_list = {}

        for declaration in declarations:
            declaration = list(filter(None, regex.split(r'(\$[^=]+)=',declaration.replace(' ',''))))
            variable =declaration[0]
            expression =declaration[1]

            if variable in self.declaration_list:
                print( f"Variable already exist : {variable}")
            else:

                self.declaration_list[variable] = expression

        print(self.declaration_list)



    def get_values(self):

        for variable,expression in self.declaration_list.items():

            if '$' not in expression:
                self.simple_variable[variable]=self.calculator.evaluate(expression)
            else:
                self.complex_variable[variable] = expression

        for v1,e1 in self.complex_variable.items():


            for v2,e2 in self.simple_variable.items():

                e1= e1.replace(str(v2),str(e2))
            self.declaration_list[v1]= e1


        for variable,expression in self.declaration_list.items():

            self.declaration_list[variable] = self.calculator.evaluate(expression)

        print(self.declaration_list)

    def generate_report(self,content):

        for variable,value in self.declaration_list.items():
            pattern = r'(\s|\b)'+regex.escape(variable)+r'(\s|\b)'
            content = regex.sub(pattern,f' {value} ',content)

        print(content)







variable = VariableHandler()

variable.declare('$x=1+2;$y=2+1;$var =12+223+(222+2); $var2=$x+$y; $xy=($var2+$x+$y)')

variable.get_values()
variable.generate_report('Rohim has $x taka and Korim has $y taka. They have $xy taka. The can get $var taka. They need $var2 taka')



