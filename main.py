from sk_calculator import Calculator
import regex
class VariableHandler:

    def __init__(self):

        self.calculator = Calculator()
        self.constant_expression_list ={}
        self.variable_expression_list=[]


    def declare(self,declarations):


        declarations = list(filter(None, regex.split(r'[;,]',declarations)))

        self.declaration_list = {}

        for declaration in declarations:
            declaration = list(filter(None, regex.split(r'\s*(\$[^=]+)=',declaration)))
            variable =declaration[0].replace(' ','')
            expression =declaration[1]

            if variable in self.declaration_list:
                print( f"Variable already exist : {variable}")
            else:

                self.declaration_list[variable] = expression


    def get_constant_expression_list (self):


        for variable,expressin in self.declaration_list.items():
            if '$' not in expressin:
                self.constant_expression_list[variable] = str(self.calculator.evaluate(expressin))

        for variable,expressin in self.constant_expression_list.items():
            self.declaration_list[variable] = expressin

    def get_variable_expression_list(self):


        for variable,expressin in self.declaration_list.items():
            if '$' in expressin:
                self.variable_expression_list.append((variable,expressin))

    def solve_variable_expression_list(self):
        temp = {}
        for variable,expressin in self.variable_expression_list:
            temp_expression =expressin
            for key,value in self.constant_expression_list.items():
                pattern = regex.escape(key)+r'(\s|\b)'
                temp_expression = regex.sub(pattern,str(value),temp_expression)
            temp[variable] =temp_expression

        for variable,expression in temp.items():
            if '$' not in expression:
                self.constant_expression_list[variable]=str(self.calculator.evaluate(expression))
                for variable_e in self.variable_expression_list:
                    if variable_e[0] == variable:
                       self.variable_expression_list.remove(variable_e)

                self.declaration_list[variable]=str(self.calculator.evaluate(expression))
            else:
                self.variable_expression_list.append((variable,expression))
                self.declaration_list[variable]=expression

        for key,value in  self.variable_expression_list:
            if '$' in value:
                self.solve_variable_expression_list()


    def get_values(self):
        self.get_constant_expression_list()
        self.get_variable_expression_list()
        self.solve_variable_expression_list()



    def generate_report(self,content):

        for variable,value in self.declaration_list.items():
            pattern = r'(\s|\b)'+regex.escape(variable)+r'(\s|\b)'
            content = regex.sub(pattern,f' {value} ',content)

        print(content)







variable = VariableHandler()

variable.declare('$x=1+2;$y=2+1; $var =12+223+(222+2); $var2 =$x+$y; $xy = ( $var2 + $x +$y );$yx = $xy+$var2 ')

variable.get_values()
variable.generate_report('Rohim has "$x" taka and Korim has $y taka. They have $xy taka. The can get $var taka. They need $var2 taka and $yx')



