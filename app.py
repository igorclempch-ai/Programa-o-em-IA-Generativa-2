import streamlit as st 
import random
import datetime 



temperatura  = st.number_input('CONVERSOR DE TEMPERATURA')

if st.button('CONVERTER PARA F° PARA C°') and temperatura:
   calculo =  (temperatura * 1.8) + 32
   st.info(calculo)

if st.button('CONVERTER PARA C°PARA F°') and temperatura:
   calculo =  (temperatura - 32) / 1.8
   st.info(calculo)      

# gerador de senhas 


st.write('GERADOR DE SENHAS...')

l1 = ['a','b','c','d','e']
l2 = [12145,34433,41045545,1231245,1214654,47878545,4688754]
l3 = ['Z','X','O','P','J','kls']
l4 = ['ana','karla', 'josep', 'luidy','marcoli']

lm = random.choice(l1)
num = random.choice(l2)
lms = random.choice(l3)
nome = random.choice(l4)

st.write (f'{lm}{num}{lms}{nome}')



# cadastro simples


st.write('CADASTRO SIMPLES')

nome = st.text_input('Nome: ')
endereco = st.text_input('Endereço: ')
idade  = st.number_input('Idade: ', value = 0)
curso = st.text_input('Curso: ')


if st.button('Cadastrar...'):
   st.info('Dados enviados')



# contador


st.write('CONTADOR')

n =  0

# st.write(n)

x =  st.number_input('contador', value = 0)


# tabuada 

st.write('TABUADA')
n =  st.number_input('Nº:  ')


for x in range(0,11):
   c = n * x
   st.write(n , 'x', x, '=', c)

st.write('PAR OU IMPAR')

n  =  st.number_input('nº:  ')

if n % 2 == 0:
   st.info('PAR')
else:
   st.info('IMPAR')


st.write('MÉDIA DE NOTAS')

n1 = st.number_input('1 >>')
n2 = st.number_input('2 >>')
n3 = st.number_input('3 >>')

media  = (n1+n2+n3)/3

st.info(media)


st.write('SORTEADOR DE NOMES')


nome = st.text_input('Nome:')
nomes =  ['Ana', 'Fernanda', 'Paula', 'Juliana', 'Henrique']

nomes.append(nome)

if st.button('sortear'):
   sorteado = random.choices(nomes)

   st.warning(sorteado)