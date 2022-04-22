# Hubert Kruk, 2022-03-22

from analizator_leksykalny import *
from analizator_skladniowy import *

def remove_comments(src):
    return re.sub('[\s]+#.+', ' ', src)

input_string = '''begin # O rany, nie ma pustej linii między elementami a połączeniami
  R1 = resistor(13.2) # rezystor o wartości 13.2 ohm
  C1 = capacitor(100e-9) # kondensator o wartości 100e-9 faradów
  VIN = voltagesource()
  AM1 = currentprobe()
#
  VIN[2] -- R1[1] -- gnd
  R1[2] -- C1[1]
  C1[2] -- AM1[1]
  AM1[2] -- VIN[1]
  VIN[1] -- gnd
end'''

print(remove_comments(input_string))
scanner = Scanner(remove_comments(input_string))

parser = Parser(scanner)
parser.start()

with open('C:\JFK\projekt_1\example1\cir1.net', 'r') as file:
    cir1 = file.read()

print(remove_comments(cir1))
scanner2 = Scanner(remove_comments(cir1))

parser = Parser(scanner2)
parser.start()

with open('C:\JFK\projekt_1\example1\cir2.net', 'r') as file:
    cir2 = file.read()

print(remove_comments(cir2))
scanner3 = Scanner(remove_comments(cir2))

parser = Parser(scanner3)
parser.start()

with open('C:\JFK\projekt_1\example1\cir00.net', 'r') as file:
    cir00 = file.read()

print(remove_comments(cir00))
scanner4 = Scanner(remove_comments(cir00))

parser = Parser(scanner4)
parser.start()

with open('C:\JFK\projekt_1\example1\cir01.net', 'r') as file:
    cir01 = file.read()

print(remove_comments(cir01))
scanner5 = Scanner(remove_comments(cir01))

parser = Parser(scanner5)
parser.start()

with open('C:\JFK\projekt_1\example1\cir02.net', 'r') as file:
    cir02 = file.read()

print(remove_comments(cir02))
scanner6 = Scanner(remove_comments(cir02))

parser = Parser(scanner6)
parser.start()

with open('C:\JFK\projekt_1\example1\cir30.net', 'r') as file:
    cir30 = file.read()

print(remove_comments(cir30))
scanner7 = Scanner(remove_comments(cir30))

parser = Parser(scanner7)
parser.start()