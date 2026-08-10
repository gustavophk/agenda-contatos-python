#Agenda para salvar contatos

def salvar_contato(contatos, nome, numero):
    contato = {
        "nome": nome,
        "numero": numero
    }
    contatos.append(contato)
    print("Contato salvo com sucesso!")
    return

def editar_contato(contatos,indice):
    indice_ajustado = indice - 1
    
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contato_atual = contatos[indice_ajustado]

        print(f"Editando contato: {contato_atual['nome']} ({contato_atual['numero']})")
        print(f"Digite ENTER caso nao queira modificar.")

        novo_nome = input("Novo nome: ")
        novo_numero = input("Novo numero: ")

        if novo_nome != "":
            contatos[indice_ajustado]['nome'] = novo_nome
        if novo_numero != "":
            contatos[indice_ajustado]['numero'] = novo_numero
        print(f"Contato: {indice} atualizado para {novo_nome} com o numero {novo_numero}!")
    else:
        print("Indice invalido!")
    return

def deletar_contato(contatos, contatos_favoritados, indice):
    indice_ajustado = int(indice) - 1
    for i, contato in enumerate(contatos):
        if indice_ajustado == i:
            contatos.remove(contato)
            contatos_favoritados.remove(contato)
    print(f"Contato: {indice} excluido com sucesso!")
    return

def favoritar_contato(contatos, indice):
    indice_ajustado = int(indice) - 1

    for i, contato in enumerate(contatos):
        if indice_ajustado == i:
            contatos_favoritados.append(contato)
    print(f"Contato: {indice} favoritado com sucesso!")
    return

def mostrar_contatos_favoritos(contatos_favoritados):

    if len(contatos_favoritados) > 0:
        print("-- LISTA DE CONTATOS FAVORITADOS --")
        for j, contato in enumerate(contatos_favoritados, start=1):
            print(f"{indice}. nome: {contato['nome']} - numero {contato['numero']}")
    else:
        print("Lista de contatos favoritos vazia!")
    return

def mostrar_contatos(contatos):
    
    for indice, contato in enumerate(contatos, start=1):
        print(f"{indice}. nome: {contato['nome']} - numero {contato['numero']}")
    return

contatos = []
contatos_favoritados = []
#menu
while True:
    print("\nMenu do gerenciador de Agenda:")
    print("1. Salvar contato")
    print("2. Editar contato")
    print("3. Deletar contato")
    print("4. Favoritar contato")
    print("5. Mostrar contatos")
    print("6. Mostrar contatos favoritos")
    print("7. Sair")

    escolha = input("\nSelecione uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome: ")
        numero = input("Digite agora o numero: ")
        salvar_contato(contatos, nome, numero)
    
    elif escolha == '2':
        mostrar_contatos(contatos)
        indice = int(input("Digite qual contato quer editar: "))
        editar_contato(contatos,indice)
    
    elif escolha == '3':
        mostrar_contatos(contatos)
        indice = input("Digite o contato a ser deletado: ")
        deletar_contato(contatos, contatos_favoritados, indice)
    
    elif escolha == '4':
        mostrar_contatos(contatos)
        indice = input("Qual o contato deseja favoritar?: ")
        favoritar_contato(contatos, indice)

    elif escolha == '5':
        mostrar_contatos(contatos)

    elif escolha == '6':
        mostrar_contatos_favoritos(contatos_favoritados)
    elif escolha == '7':
        break

print("Sistema finalizado!")

