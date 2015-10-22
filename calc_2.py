INTEGER, PLUS, MINUS, MULTIPLE, DIVIDE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLE', 'DIVIDE', 'EOF'


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Toke({type}, {value})'.format(
            type = self.type,
            value = repr(self.value)
            )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Оролт хөрвүүлэхэд алдаа гарав.')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char  = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            if self.current_char == '*':
                self.advance()
                return Token(MULTIPLE, '*')
            if self.current_char == '/':
                self.advance()
                return Token(DIVIDE, '/')

            self.error()

        return Token (EOF, None)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        int_list = []
        op_list = []

        result = 0

        if self.current_token == INTEGER:
            int_list.append(self.current_token)
            self.eat(INTEGER)
        else:
            op_list.append(self.current_token)
            if self.current_token.type == PLUS:
                self.eat(PLUS)
            elif self.current_token.type == MINUS:
                self.eat(MINUS)

        result = int_list[0]

        for i in len(op_list):
            if op_list[i].type == PLUS:
                result += int_list[i+1]
            elif op_list[i].type == MINUS:
                result -= int_list[i+1]
            
            
        
##        left = self.current_token
##        self.eat(INTEGER)
##
##        op = self.current_token
##        if op.type == PLUS:
##            self.eat(PLUS)
##        elif op.type == MINUS:
##            self.eat(MINUS)
##        elif op.type == MULTIPLE:
##            self.eat(MULTIPLE)
##        elif op.type == DIVIDE:
##            self.eat(DIVIDE)
##
##        right = self.current_token
##        self.eat(INTEGER)
##
##        if op.type == PLUS:
##            result = left.value + right.value
##        elif op.type == MINUS:
##            result = left.value - right.value
##        elif op.type == MULTIPLE:
##            result = left.value * right.value
##        elif op.type == DIVIDE:
##            result = left.value / right.value

        return result

def main():
    text = ''
    while True:
        try:
            text = input('Unana >>> ')
        except EOFError:
            break
        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
        
