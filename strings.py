Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nome = 'anderson'
>>> type
<class 'type'>
>>> type(nome)
<class 'str'>
>>> sobrenome_mae = 'silva'
>>> sobrenome_pai = 'pereira'
>>> nome + sobrenome_mae
'andersonsilva'
>>> nome_completo = nome + ' ' + sobrenome_pai + ' ' + sobrenome_pai
>>> nome_completo
'anderson pereira pereira'
>>> nome * 5
'andersonandersonandersonandersonanderson'
>>> nome_completo = nome + ' ' + sobrenome_pai + ' da ' + sobrenome_mae
>>> nome_completo
'anderson pereira da silva'
>>> nome
'anderson'
>>> len(nome)
8
>>> len(sobrenome_mae)
5
>>> len(sobrenome_pai)
7
>>> nome[0]
'a'
>>> nome [1]
'n'
>>> 
>>> nome [2]
'd'
>>> nome [3]
'e'
>>> nome [4]
'r'
>>> nome [5]
's'
>>> nome [6]
'o'
>>> nome [7]
'n'
>>> nome [-1]
'n'
>>> nome [-2]
'o'
>>> nome [-7]
'n'
>>> nome [-3]
's'
>>> nome [-4]
'r'
>>> nome [-6]
'd'
>>> nome [0:2]
'an'
>>> nome [0:5]
'ander'
>>> nome [0:4]
'ande'
>>> nome [0:7]
'anderso'
>>> nome [-2:-1]
'o'
>>> nome [-2:]
'on'
>>> nome [:3]
'and'
>>> print (nome)
anderson
>>> nome [4:7]
'rso'
>>> 
