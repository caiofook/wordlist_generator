# Importando módulos necessários
import itertools

# Função para iniciar o programa e exibir o menu interativo
def iniciar_programa():
    
    # Variáveis para armazenar os inputs do usuario
    chaves_primarias = []
    chaves_secundarias = []

    # Variável para armazenar todas as combinações de caracteres especiais com 1 a 2 caracteres
    chaves_pseudoaleatorias = [''.join(p) for r in range(1, 3) for p in itertools.product("!@#$%&*+-_?", repeat=r)]

    # Variáveis para armazenar as permutações feitas ao longo da execução
    chaves_primarias_permutadas = []
    chaves_permutadas_finais = []
    wordlist_semi_final = []
    wordlist_final = []
    wordlist_semi_final_sem_espacos = []
    wordlist_final_sem_espacos = []


    # Saudacao
    print("Bem-vindo ao gerador de wordlists!")
    print("Por favor, siga as instruções abaixo.")

    # Menu Interativo
    input_chaves_primarias(chaves_primarias)
    ## OBS: deixar esse menu mais bonitinho e no futuro fazer o --help
    input_chaves_secundarias(chaves_secundarias)
    
    nome_do_arquivo = input_nome_arquivo()

    print("Iniciando as permutações...")

    permutacao_inicial(chaves_primarias, chaves_pseudoaleatorias, chaves_primarias_permutadas)
    print("Pode demorar um pouco...")
    
    permutacao_secundaria(chaves_primarias_permutadas, chaves_secundarias, chaves_permutadas_finais)
    
    print("Limpando lixo...")

    chaves_primarias_permutadas.clear()
    chaves_secundarias.clear()

    print("Permutação final...!")

    permutacao_final(chaves_permutadas_finais, chaves_pseudoaleatorias, wordlist_semi_final)
    ## OBS: preciso excluir os duplicados

    chaves_permutadas_finais.clear()

    print("Agora um pequeno polimento.")

    polimento(wordlist_semi_final, wordlist_final, wordlist_semi_final_sem_espacos, wordlist_final_sem_espacos)
    ## OBS: preciso excluir os duplicados
    ## OBS: preciso excluir tudo com menos de 5 caracteres
    ## OBS: é melhor deixar o usuario escolher quantos caracteres ele quer

    print("Quase lá")

    wordlist_semi_final.clear()
    wordlist_semi_final_sem_espacos.clear()

    organizar_output(nome_do_arquivo, wordlist_final, wordlist_final_sem_espacos)

    print("Wordlist concluída")


### DEFINIÇÕES DE FUNÇÕES
    
# Função para perguntar e receber as palavras principais do usuário
def input_chaves_primarias(chaves_primarias):
    resposta = input("Insira 1-3 palavras principais, separadas por vírgula: ")
    chaves_primarias.extend(resposta.split(","))

# Função para perguntar e receber as palavras secundárias do usuário
def input_chaves_secundarias(chaves_secundarias):
    resposta = input("Insira 2-6 palavras secundárias, separadas por vírgula: ")
    chaves_secundarias.extend(resposta.split(","))

# Função para perguntar e receber o nome do arquivo para salvar a wordlist
def input_nome_arquivo():
    nome_arquivo = input("Salvar wordlist como..? ")
    return nome_arquivo


# Lógica da permutação inicial
def permutacao_inicial(chaves_primarias, chaves_pseudoaleatorias, chaves_primarias_permutadas):
    # Gerar todas as combinações possíveis entre chaves_primarias e chaves_pseudoaleatorias
    for primaria in chaves_primarias:
        for aleatoria in chaves_pseudoaleatorias:
            permutacao1 = f"{primaria} {aleatoria}"
            permutacao2 = f"{aleatoria} {primaria}"
            chaves_primarias_permutadas.append(permutacao1)
            chaves_primarias_permutadas.append(permutacao2)
    for primaria in chaves_primarias:
        chaves_primarias_permutadas.append(primaria)

# Lógica da permutação secundárias
def permutacao_secundaria(chaves_primarias_permutadas, chaves_secundarias, chaves_permutadas_finais):
    # Gerar todas as combinações possíveis entre chaves_primarias e chaves_secundarias
    for primaria in chaves_primarias_permutadas:
        for secundaria in chaves_secundarias:
            permutacao1 = f"{primaria} {secundaria}"
            permutacao2 = f"{secundaria} {primaria}"
            chaves_permutadas_finais.append(permutacao1)
            chaves_permutadas_finais.append(permutacao2)
    for secundaria in chaves_secundarias:
        chaves_permutadas_finais.insert(0,secundaria)
    for primaria in chaves_primarias_permutadas:
        chaves_permutadas_finais.insert(0,primaria)

# Lógica da permutação final
def permutacao_final(chaves_permutadas_finais, chaves_pseudoaleatorias, wordlist_semi_final):
    wordlist_semi_final.append(chaves_permutadas_finais)
    for primaria in chaves_permutadas_finais:
         for aleatoria in chaves_pseudoaleatorias:
            permutacao = f"{primaria} {aleatoria}"
            wordlist_semi_final.append(permutacao)


# Lógica para o polimento da wordlist
def polimento(wordlist_semi_final, wordlist_final, wordlist_semi_final_sem_espacos, wordlist_final_sem_espacos):
  
    for entrada in wordlist_semi_final:
        # Verificar se a entrada tem mais de 4 caracteres
        if len(entrada) > 4:
            # Se tiver, adicionar à lista wordlist_final
            wordlist_final.append(entrada)

    # Para cada entrada em wordlist_semi_final
    for entrada in wordlist_final:
        # Abrir a entrada como string, remover os espaços vazios e salvar em wordlist_provisoria
        entrada_sem_espacos = str(entrada).replace(" ", "")
        wordlist_semi_final_sem_espacos.append(entrada_sem_espacos)
    
    for entrada in wordlist_semi_final_sem_espacos:
        # Verificar se a entrada tem mais de 4 caracteres
        if len(entrada) > 4:
            # Se tiver, adicionar à lista wordlist_final
            wordlist_final_sem_espacos.append(entrada)

# Salvar reusltado no arquivo
def organizar_output(nome_do_arquivo, wordlist_final, wordlist_final_sem_espacos):

    caminho_arquivo1 = nome_do_arquivo
    caminho_arquivo2 = str(nome_do_arquivo) + ".sem_espacos"

    # Abrir o arquivo para escrita
    with open(caminho_arquivo1, 'w+') as arquivo:
        # Escrever cada entrada de chaves_primarias no arquivo, uma por linha
        for entrada in wordlist_final:
            arquivo.write(entrada + '\n')

    with open(caminho_arquivo2, 'w+') as arquivo2:
        # Escrever cada entrada de chaves_primarias no arquivo, uma por linha
        for entrada in wordlist_final_sem_espacos:
            arquivo2.write(entrada + '\n')



# Chamada da função principal para iniciar o programa
if __name__ == "__main__":
    iniciar_programa()