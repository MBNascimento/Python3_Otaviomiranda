print(12, 34)
print(56, 78)  # esse exemplo de print terá como saída os núneros
# sem separadores,
# apenas com espaços.

print(12, 34, sep="Jõao")
# esse código esta com argumento nomeado sep=()

print(56, 78, sep='-', end='\n')
# se usar o end='\n' nada muda pois ja é padrão

print(12, 34, sep='-', end='##')
""" mas se usar o end='com qualquer caracter
 o caracter é lido e deixa de ser quebrada a linha """

print(56, 78, sep='-', end='\n')

print(12, 34, sep='-', end='##\n')

print(56, 78, sep='-', end='\n##')

print(9, 10, sep='-', end=' FIM '*3)
# nesse caso a saída tem escrito FIM três veses.

# \r \n -> CRLF  é um sistema padrão de quebra de linha no Windows
# \n  -> LF  é um sistema padão de quebra de linha no sistema baseado em iunix.
