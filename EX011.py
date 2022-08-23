l = float(input('largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
quantidade = (area * 1) / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de tinta.'.format(l, a, area, quantidade))
