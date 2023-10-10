# Argumentos não nomeiados
print(12, 34)
print(56, 78)
# \r\n -> CRLF
# \n -> LF = Baseado em unix
print(12, 34, 1011, sep="-", end='\r\n')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')