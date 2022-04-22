
from ast import parse
from lib2to3.pgen2 import token


class Parser:

    ##### Parser header #####
    def __init__(self, scanner):
        self.next_token = scanner.next_token
        self.token = self.next_token()

    def take_token(self, token_type):
        if self.token.type != token_type:
            print(self.token.type ,token_type)
            self.error(f"Unexpected token:'{self.token.value}' in line {self.token.line} Expecteted token type: {token_type}")
        if token_type != 'EOF':
            self.token = self.next_token()
            print(self.token)

    def error(self, msg):
        print('error', self.token.type)
        raise RuntimeError('Parser Error: %s' % msg)

    ##### Parser body #####

    # Starting symbol
    def start(self):
        # start -> program EOF
        if self.token.type == 'begin':
            self.take_token('begin')
            self.deff()
            self.NLine()
            self.connection()
            self.take_token('end')
            self.take_token('EOF')
            print('\nSyntax correctly entered!\n')
        else:
            self.error("The begin keyword is missing.")
      

    #def -> ID EQ #keyw  def
    #def -> EMP
    def deff(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('EQ')
            self.keyw()
            self.deff()
        else: 
            pass
    
    #keyw -> VOLTAGESOURCE vector
    def keyw(self):
        if self.token.type == 'voltagesource':
            self.voltagesource()
        elif self.token.type == 'voltageprobe':
            self.voltageprobe()
        elif self.token.type == 'currentsource':
            self.currentsource()
        elif self.token.type == 'currentprobe':
            self.currentprobe() 
        elif self.token.type == 'resistor':
            self.resistor()
        elif self.token.type == 'capacitor':
            self.capacitor()
        elif self.token.type == 'inductor':
            self.inductor()
        elif self.token.type == 'diode':
            self.diode()
        else:
            pass

    def voltagesource(self):
        self.take_token('voltagesource')
        self.vector_emp()
    
    def voltageprobe(self):
        self.take_token('voltageprobe')
        self.vector_emp()

    def currentsource(self):
        self.take_token('currentsource')
        self.vector_emp()
    
    def currentprobe(self):
        self.take_token('currentprobe')
        self.vector_emp()

    def vector_emp(self):
        if self.token.type == 'PO':
            self.take_token('PO')
            self.value()
            self.take_token('PC')
        else:
            self.take_token('PO')
            self.take_token('PC')

    def resistor(self):
        self.take_token('resistor')
        self.vector()

    def capacitor(self):
        self.take_token('capacitor')
        self.vector()

    def inductor(self):
        self.take_token('inductor')
        self.vector()    

    def vector(self):
        self.take_token('PO')
        self.value_must()
        self.take_token('PC')

    def diode(self):
        self.take_token('diode')
        self.vector_multi_emp() 

    def vector_multi_emp(self):
        self.take_token('PO')
        self.vector_multi_emp_count()
        self.take_token('PC')

    def vector_multi_emp_count(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('EQ')
            self.value()
            self.vector_multi_emp_count_next()
        else:
            pass

    def vector_multi_emp_count_next(self):
        if self.token.type == 'COMA':
            self.take_token('COMA')
            self.take_token('ID')
            self.take_token('EQ')
            self.value()
            self.vector_multi_emp_count_next()
        else:
            pass

    def value(self):
        # value -> REAL
        if self.token.type == 'POW':
            self.pow()
        # value -> ID
        elif self.token.type == 'ID':
            self.take_token('ID')
        # value -> INT    
        elif self.token.type == 'INT':
            self.take_token('INT')
        elif self.token.type == 'REAL':
            self.take_token('REAL')
        else:
            pass

    def value_must(self):
        # value -> REAL
        if self.token.type == 'POW':
            self.pow()
        # value -> ID
        elif self.token.type == 'ID':
            self.take_token('ID')
        # value -> INT    
        elif self.token.type == 'INT':
            self.take_token('INT')
        elif self.token.type == 'REAL':
            self.take_token('REAL')
        else:
            self.error(f"Value must be given in line {self.token.line} and column {self.token.column}")

    def pow(self):
        self.take_token('POW')

    ###\N\N
    def NLine(self):
        if self.token.type == 'N':
            self.take_token('N')
        else:
            self.error(f"You must add empty line in {self.token.line} line")
    
    #connection -> connection_value connection_next
    #connection -> EMP
    def connection(self):
        if self.token.type == 'ID' or self.token.type == 'gnd':
            self.connection_value()
            self.connection_next()
            self.connection()
        else:
            pass
        

    #connection_value -> ID SBO INT SBC
    #                 -> gnd
    def connection_value(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('SBO')
            self.take_token('INT')
            self.take_token('SBC')
        elif self.token.type == 'gnd':
            self.gnd()
        else:
            pass

    def gnd(self):
        self.take_token('gnd')

    #connection_next -> CON connection_value connection_next
    #connection_next -> EMP
    def connection_next(self):
        if self.token.type == 'CON':
            self.take_token('CON')
            self.connection_value()
            self.connection_next()
        else:
            pass
