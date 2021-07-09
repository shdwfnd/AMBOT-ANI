import math

sin, cos, tan = math.sin, math.cos, math.tan
sqrt = math.sqrt
power = math.pow
π = math.pi
abs = math.fabs
log = math.log10
ln = math.log
e = math.exp


class Calculator:
    def __init__(self):
        self.total_expression = ""
        self.current_expression = ""
        self.prev_ans = ""
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""

    def add_to_expression(self, value):
        self.current_expression += str(value)

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""    

    def delete(self):
        self.current_expression = str(self.current_expression[:-1])
        

    def answer(self):
        self.current_expression = self.current_expression + "Ans"
    
    # other functions
    def evaluate(self):
        self.total_expression += self.current_expression
        x = self.total_expression
        
        try:
            if '²' in x or '³' in x or 'E' in x or 'P' in x or 'C' in x or 'Ans' in x or 'e' in x or 'π' in x:
                x = x.replace('²', '**2').replace('³', '**3').replace('E','*10**').replace('Ans',f'{self.prev_ans}').replace('e', 'math.exp').replace('π', 'math.pi')
                pc = []
                operands = ['+', '-', '*', '/']
                for i in range(len(x)):
                    if x[i] == 'P' or x[i] == 'C':
                        term = ''
                        y = z = i
                        while y > -1 and x[y] not in operands:
                            term = x[y] + term
                            y -= 1
                        while (z+1) < len(x) and x[z+1] not in operands:
                            term += x[z+1]
                            z += 1
                        pc.append(term)
                for term in pc:
                    if 'P' in term:
                        n,r = term.split('P')
                        n,r = int(n), int(r)
                        if 0 <= r <= n: 
                            x = x.replace(term, f'math.factorial({n})' + '//' + f'math.factorial({n}-{r})')
                    elif 'C' in term:
                        n,r = term.split('C')
                        n,r = int(n), int(r)
                        if 0 <= r <= n:
                            x = x.replace(term, f'math.factorial({n})' + '//' + f'math.factorial({r})' + '//' + f'math.factorial({n}-{r})' )
            self.current_expression = str(eval(x))
            
        except Exception:
            self.current_expression = "Error"   
        
        self.prev_ans = self.current_expression[:]
        self.total_expression = ""
        self.current_expression = self.current_expression[:13]
        return self.current_expression

    def exit(self):
        exit()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
