# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('alt="Pet Shop, Banho & Tosa e Vet"', 'alt="Pawly • Pet Shop & E-commerce Premium"')
c = c.replace('pet shop, banho & tosa e vet', 'pawly pet shop e-commerce')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated all alt tags and data-category attributes.')
