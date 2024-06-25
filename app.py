from modelos.jurado import Jurado
from modelos.aluno import Aluno

rhaenys = Aluno('Rhaenys', 'TI', 'Miss')
jurado = Jurado('Daemon', 'Educacional')

jurado.atribuir_nota(rhaenys, 5, 5, 5, 5)
jurado.atribuir_nota(rhaenys, 6, 6, 6, 6)

print(rhaenys)