import requests



#exemplo da estrutura json da aplicacao professores
# {
#     "cod_professor": "cfd38e58-82c9-4d09-8e9c-054a6d07efe6",
#     "nome_professor": "nomeprofessor2",
#     "ru": "ru2",
#     "matricula": 2,
#     "formacao": "formacao2",
#     "titulacao": "titulacao2",
#     "area_titulacao": "areatitulacao2",
#     "endereco_completo": "enderecocompleto2",
#     "telefone_fixo": "2222222",
#     "whatsapp": "2222222",
#     "email": "email2@email2.com",
#     "data_ingresso_instituicao": "2021-11-20",
#     "data_docencia": null,
#     "data_docencia_instituicao": null,
#     "funcao": "funcao2",
#     "regime_trabalho": "regimetrabalho2"
# }



print('consumindo a api professores\n\n')

print('   ensaio 1 usando id especifico \n\n')

cod_professor = 'cfd38e58-82c9-4d09-8e9c-054a6d07efe6'

request = requests.get('http://127.0.0.1:8000/professores/' + cod_professor)

dados_da_request = request.json()

print('nome do professor: {}'.format(dados_da_request['nome_professor']))

print('ru: '+ dados_da_request['ru'])

print('matricula:', dados_da_request['matricula'])

print('formacao: {}'.format(dados_da_request['formacao']))

print('titulacao: {}'.format(dados_da_request['titulacao']))

print('area da titulacao: {}'.format(dados_da_request['area_titulacao']))

print('endereco completo: {}'.format(dados_da_request['endereco_completo']))

print('telefone fixo: {}'.format(dados_da_request['telefone_fixo']))

print('whatsapp: {}'.format(dados_da_request['whatsapp']))

print('email: {}'.format(dados_da_request['email']))

print('data de ingresso na instituicao: {}'.format(dados_da_request['data_ingresso_instituicao']))

if not dados_da_request['data_docencia'] == None:
    print('docente desde: {}'.format(dados_da_request['data_docencia']))

if not dados_da_request['data_docencia_instituicao'] == None:
    print('docente na instituicao desde: {}'.format(dados_da_request['data_docencia_instituicao']))

print('funcao: {}'.format(dados_da_request['funcao']))

print('regime de trabalho: {}'.format(dados_da_request['regime_trabalho']))







print('\n\n   ensaio2 obtendo lista dos id da api professores\n\n')

#ids_professores = Professores.objects.values_list('cod_professor', flat=True)
#ids_professores = professores.values_list('cod_professor', flat=True)
ids_professores = requests.get('http://127.0.0.1:8000/professores/')

print('\n\nlistando ids dos professores\n')
print(ids_professores.content)



print('\n\n   ensaio3 convertendo request pra json\n\n')

#ids_professores = Professores.objects.values_list('cod_professor', flat=True)
#ids_professores = professores.values_list('cod_professor', flat=True)
professores_obtidos = requests.get('http://127.0.0.1:8000/professores/')

print('\n\nlistando ids dos professores 3\n')
#print(f'id: {professores_obtidos.json().get("cod_professor")}')
#print(professores_obtidos.get('total'))
#print(professores_obtidos['cod_professor'])
json_professores = professores_obtidos.json()
print(json_professores)

print('\n\njson_professores\n\n')

for elemento in json_professores:
    print(elemento.get('cod_professor'))

print('\n\n\n\n')



print('\n\n   ensaio 4 trabalhando todos os registros\n\n')

for elemento in json_professores:

    print('\n\n')

    cod_professor = elemento.get('cod_professor')

    request = requests.get('http://127.0.0.1:8000/professores/' + cod_professor)

    dados_da_request = request.json()

    print('nome do professor: {}'.format(dados_da_request['nome_professor']))

    print('ru: '+ dados_da_request['ru'])

    print('matricula:', dados_da_request['matricula'])

    print('formacao: {}'.format(dados_da_request['formacao']))

    print('titulacao: {}'.format(dados_da_request['titulacao']))

    print('area da titulacao: {}'.format(dados_da_request['area_titulacao']))

    print('endereco completo: {}'.format(dados_da_request['endereco_completo']))

    print('telefone fixo: {}'.format(dados_da_request['telefone_fixo']))

    print('whatsapp: {}'.format(dados_da_request['whatsapp']))

    print('email: {}'.format(dados_da_request['email']))

    print('data de ingresso na instituicao: {}'.format(dados_da_request['data_ingresso_instituicao']))

    if not dados_da_request['data_docencia'] == None:
        print('docente desde: {}'.format(dados_da_request['data_docencia']))

    if not dados_da_request['data_docencia_instituicao'] == None:
        print('docente na instituicao desde: {}'.format(dados_da_request['data_docencia_instituicao']))

    print('funcao: {}'.format(dados_da_request['funcao']))

    print('regime de trabalho: {}'.format(dados_da_request['regime_trabalho']))



