# Operadores lógicos "or"
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser 
# verdadeiras.
# Se qualquer valor for considerado falso, a 
# expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado par 
# representar um não valor

#entrada = input('[E]ntrada [S]air: ')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'
# Obs: sempre que tiver uma expressão que tem 'or' e 'and', na 
# mesma expressão, essa expressão pode ficar ambigua em alguns 
# momentos
#if entrada == 'E' or entrada == 'e' and senha_digitada == #senha_permitida:
#    print('Entrar')
#else:
#  print('Sair')    

  # Avaliação de curto circuito

senha = input('senha: ') or 'sem senha'
print(senha)