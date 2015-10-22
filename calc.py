#Тэмдэгт төрөл
#
#EOF (end-of-file) энэ тэмдэгт нь Үгэн Судалгаа - д 
#оролцох нэмэлт тэмдэгт байхгүй гэдгийг илтгэнэ.
#Шууд орчуулга нь: файлын төгсгөл
#Үгэн Судалгаа: Lexical Analysis

#Тэмдэгтийн төрөлүүд:
#INTEGER: Бүхэл тоо
#PLUS: Нэмэх
#EOF: Файлын төгсгөл
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        #Тэмдэгт төрөл: INTEGER, PLUS, MINUS, or EOF
        self.type = type
        #Тэмдэгтийн авч болох утгууд: 0,1,2...8,9,'+','-', or None
        self.value = value

    def __str__(self):
##        Энэхүү ангийн /класс/ утсан /стринг/ илэрхийлэл.
##
##        Жишээ нь:
##            Token(INTEGER, 3)
##            Token(PLUS, '+')
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        #Хандагчийн оруулах утсан мэдээлэл: "3+5" гэх мэт
        self.text = text
        #self.pos нь self.text дахь байрлалын дугаар
        self.pos = 0
        #Одоо уншиж байгаа тэмдэгтийн үе
        self.current_token = None

    def error(self):
        raise Exception('Өгөгдөл дамжуулахад алдаа гарав.')

    def get_next_token(self):
##        Үгэн Судалагч(хайгч, тэмдэглэгч гэж бас нэрлэдэг)
##
##        Энэ арга нь гараас орж буй өгүүлбэрийг тус, тусын 
##        тэмдэгт болгоход ашиглагддаг. Нэг нэг тэмдэгтээр нь салгана.
        text = self.text

        #self.pos дугаар нь self.text ийн уртаас хэтэрвэл
        #EOF: Файлын төгсгөл тэмдэгтийг буцаана. Учир нь
        #үүнээс хойш тэмдэгт болгон хувиргах гарын өгөгдөл байхгүй болно.
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        #self.pos -д байрлах тэмдэгийг авч, энэхүү ганц тэмдэг дээр суурилан
        #ямар тэмдэгт үүсгэхээ шийдвэрлэнэ.
        current_char = text[self.pos]

        #if the character is a digit then convert it to
        #integer, create an INTEGER token, increment self.pos
        #index to point to the next character after the digit
        #and return the INTEGER token
        if current_char.isspace():
            self.pos += 1
            pass
        
        elif current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        elif current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        elif current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token
        
        self.error()

    def eat(self, token_type):
        #compare the current token type with the passed token
        #type and if the match then "eat" the current token
        #and assign the next token to the self.current_token,
        #otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        #expr -> INTEGER PLUS INTEGER
        #set current token to the first token taken from input
        self.current_token = self.get_next_token()
        beforeOP = True
        left = 0
        right = 0
        result = 0
        
        op = self.current_token

        while op.type != EOF:
            if op.type == INTEGER:
                if beforeOP == True:
                    left = int(left * 10 + int(op.value))
                else:
                    right = int(right * 10 + int(op.value))
                self.eat(INTEGER)
            elif op.type == PLUS:
                beforeOP = False
                self.eat(PLUS)
            elif op.type == MINUS:
                beforeOP = False
                self.eat(MINUS)
        
        #we expect the current token to be a single-digit integer
        #left = int(left * 10 + self.current_token.value)
        #self.eat(INTEGER)

        #we expect the current token to be a '+' token
        #op = self.current_token
        #if op.type == PLUS:
        #    self.eat(PLUS)
        #elif op.type == MINUS:
        #    self.eat(MINUS)

        #we expect the current token to be a single digit integer
        #right = int(right * 10 + self.current_token.value)
        #self.eat(INTEGER)

        #after the above call the self.current_token is set to
        #EOF token

        #at this point INTGER PLUS INTEGER sequence of tokens
        #has been successfully found and the method can just
        #return the result of adding two integers, thus
        #effectively interpreting client input
        if op.type == PLUS:
            result = left + right
        elif op.type == MINUS:
            result = left - right
            
        return result

def main():
    while True:
        try:
            #To run under Python3 replace 'raw_input' call
            #with 'input'
            text = input('Унана >>>')
        except EOFerror:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
        
















            
    
                
