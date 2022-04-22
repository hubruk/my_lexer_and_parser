import collections
from msilib.schema import Error
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])

class Scanner:
    def __init__(self, input):
        self.tokens = []
        self.current_token_number = 0
        for token in self.tokenize(input):
            self.tokens.append(token)
            
    def tokenize(self, input_string):
        keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN', 'PRINT', 'EOF','voltagesource', 'voltageprobe', 'currentsource', 'currentprobe',
                    'resistor', 'capacitor', 'inductor', 'diode', 'begin', 'end', 'gnd'}
        token_specification = [
                ('POW',         r'[\+\-]?[0-9]+(\.[0-9]+)?e[\+\-]?[0-9]+'),
                ('REAL',        r'\d+\.\d+'),          # Integer or decimal number
                ('EQ',          r'='),                 # EQment operator
                ('ID',          r'[A-Za-z]+[\w]*'),      # Identifiers
                ('N',           r'\n\n'),                    
                ('Newline',     r'\n'),
                ('SKIP',        r'[ \t]'),             # Skip over spaces and tabs
                ('EMP',         r'^ $'),                # empty
                ('INT',         r'[0-9]+'),
                ('PO',          r'\('),
                ('PC',          r'\)'),
                ('CON',         r'--'),
                ('SBO',         r'\['),
                ('SBC',         r'\]'),
                ("COMA",        r',')
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification) #wypisuje wszyskie tokeny w formacie ? odzielonym |
        #print("tok_regex\n",tok_regex)
        get_token = re.compile(tok_regex).match 
        #print("get_token\n",get_token)
        line_number = 1
        current_position = line_start = 0
        match = get_token(input_string) #daje kazdy pojedynczy token (spacje tez)
        #print(match, "!!!!!!!!!!!!!!!!!!!")
        while match is not None:
                #print(match)
                type = match.lastgroup #The name of the last matched capturing group, or None if the group didn’t have a name, or if no group was matched at all.
                #print("type:::", type)
                if type == 'Newline':
                        line_start = current_position
                        line_number += 1
                        #value = match.group(type)
                        #yield Token(type, value, line_number, match.start()-line_start)
                elif type == 'EMP':
                        raise RuntimeError('Newline is missing.')
                elif type != 'SKIP':
                        value = match.group(type)
                        #print("value:::", value)
                        if type == 'ID' and value in keywords:
                                type = value
                        yield Token(type, value, line_number, match.start()-line_start)
                current_position = match.end()
                #print("current_position", current_position)
                match = get_token(input_string, current_position)

        if current_position != len(input_string):
                pass
        yield Token('EOF', '', line_number, current_position-line_start)

    def next_token(self):
        self.current_token_number += 1
        if self.current_token_number-1 < len(self.tokens):
            return self.tokens[self.current_token_number-1]
        else:
            raise RuntimeError('Error: No more tokens')
        #print(tokens)
