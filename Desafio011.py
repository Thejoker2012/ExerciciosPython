print('========================================Desafio011============================================')
larg = float(input('Digite a largura da parede : '))
alt = float(input('Digite a altura da parede : '))
Area = larg * alt
tinta = Area / 2
print('Sua área total tem {} m², vai precisar de {:.2f} litros de tinta.'.format(Area, tinta))