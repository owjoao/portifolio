# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('Lumina OS CRM', 'Pawly E-commerce')
c = c.replace('Acompanhamento ao Vivo do Pet', 'E-commerce + Adoção & Quiz')
c = c.replace('Simulador Pet Spa & Táxi', 'Carrinho Interativo')
c = c.replace('CRM Pet Care', 'Adoção de Pets')
c = c.replace('Vacinas & Insumos', 'Quiz Personalizado')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Card badges and pills updated successfully.')
