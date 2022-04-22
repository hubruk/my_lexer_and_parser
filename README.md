# my_lexer_and_parser
Polecenie projektowe:
Walidator dla składni ﻿plików z opisem obwodów elektrycznych (*.net). Zakres sprawdzanej składni powinien obejmować konstrukcje wykorzystujące, słowa kluczowe:
voltagesource
voltageprobe
currentsource
currentprobe
resistor
capacitor
inductor
diode
begin
end
gnd

Walidator nie powinien skupiać się na pełnej definicji formatu.

Projekt można pisać w dowolnym języku programowania, ale koncepcyjnie musi to być zgodne z załączonym przykładem. Zwrócić uwagę na:
analiza  składniowa poprzez rekurencyjne wywołanie funkcji (symbole nieterminalne to nazwy funkcji/metod),
analiza leksykalna wyraźnie oddzielona od analizy składniowej,
analiza leksykalna zrealizowana w dowolny sposób (while-if-switch, prosty automat skończony, wyrażenia regularne, zewnętrzna biblioteka),
możliwie precyzyjne komunikaty o błędach
