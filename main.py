# Pesquisa de satisfação de clientes - TudoWeb

# Contadores das respostas que serão exibidas no resultado final
excelente = 0
ruim = 0

# Repete a pesquisa para cada entrevistado
# Para os testes da atividade, utilize range(10).
# Na versão final, utilize range(50).
for i in range(50):

   
    # Exibe o número do entrevistado atual
    print(f"\nEntrevistado {i + 1}")

   
   
    # Coleta os dados básicos do entrevistado
    nome = input("Digite nome: ")
    idade = int(input("Digite idade: "))

   
   
    # Apresenta as opções disponíveis para avaliação do atendimento
    print("Opinião sobre atendimento:")
    print("1 - Excelente")
    print("2 - Bom")
    print("3 - Ruim")

    opiniao = int(input("Escolha uma opção: "))

   
    # Valida a resposta e solicita novamente enquanto
    # o usuário informar uma opção fora do intervalo permitido
    while opiniao < 1 or opiniao > 3:
        print("Opção inválida! Digite apenas 1, 2 ou 3.")
        opiniao = int(input("Escolha novamente: "))

    
    # Contabiliza somente as respostas exigidas no resultado da pesquisa
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1


# Exibe os resultados após o término de todas as entrevistas
print("\nResultado da pesquisa")
print(f"Quantidade de respostas excelente: {excelente}")
print(f"Quantidade de respostas ruim: {ruim}")