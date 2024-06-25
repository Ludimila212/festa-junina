from modelos.jurado import Jurado
from modelos.aluno import Aluno

rhaenys = Aluno('Rhaenys', 'TI', 'Miss')
laena = Aluno('Laena', 'TI', 'Miss')
romina = Aluno('Romina', 'TI', 'Miss')
thiago = Aluno('Thiago', 'TI', 'Mister')

jurado = Jurado('Daemon', 'Educacional')
jurado = Jurado('Lucerys', 'Educacional')
jurado = Jurado('Alicent', 'Educacional')

jurado.atribuir_nota(rhaenys, 5, 5, 5, 5)
jurado.atribuir_nota(laena, 6, 6, 6, 6)
jurado.atribuir_nota(romina,10,10,10,10)
jurado.atribuir_nota(thiago, 5,3,2,7)

print(rhaenys)
print(laena)
print(romina)
print(thiago)

def main():
    pass