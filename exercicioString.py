Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nome = 'Anderson'
>>> sobrenome_mae = 'Silva'
>>> sobrenome_pai = 'Pereira'
>>> 
>>> iniciais = nome [0] + sobrenome_pai [0] + sobrenome_mae [0]
>>> iniciais (nome [0] + sobrenome_pai [0] + sobrenome_mae [0])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    iniciais (nome [0] + sobrenome_pai [0] + sobrenome_mae [0])
TypeError: 'str' object is not callable
>>> iniciais = nome [0] + sobrenome_pai [0] + sobrenome_mae [0]
>>> print nome
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(nome)?
>>> print (iniciais)
APS
>>> 
