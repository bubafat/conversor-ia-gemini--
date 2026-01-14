import random
import os

# 1. FUNÇÕES AUXILIARES (Lá no topo, fora da função jogar)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_recorde():
    if os.path.exists("arquivo_recorde.txt"):
        with open("arquivo_recorde.txt", "r") as f:
            return int(f.read())
    return 0

def salvar_recorde(novo_recorde):
    with open("arquivo_recorde.txt", "w") as f:
        f.write(str(novo_recorde))

# 2. FUNÇÃO PRINCIPAL
def jogar():
    total_rounds = 3
    max_tentativas = 7
    score_total = 0  # Começa com zero pontos
    recorde_atual = carregar_recorde()

    limpar_tela()
    print(f"Bem-vindo ao jogo de adivinhação!")
    print(f"Você terá {total_rounds} rounds para juntar pontos.")
    print(f"O recorde atual é: {recorde_atual} pontos.")
    input("Pressione Enter para começar...")

    # TUDO o que deve acontecer em cada round fica dentro deste FOR
    for r in range(1, total_rounds + 1):
        limpar_tela()
        secreto = random.randint(1, 50)
        tentativas = 0
        acertou_neste_round = False
        
        print(f"\n---- Round {r} de {total_rounds}! ----")
        print(f"Score Total: {score_total}")

        # TUDO o que deve acontecer em cada tentativa fica dentro deste WHILE
        while tentativas < max_tentativas:
            try:
                palpite = int(input(f"Tentativa {tentativas + 1} de {max_tentativas}: "))
            except ValueError:
                print("⚠️ Insira um número válido.")
                continue

            if palpite < 1 or palpite > 50:
                print("Escolha entre 1 e 50.")
                continue

            tentativas += 1

            if palpite == secreto:
                pontos_ganhos = (max_tentativas - tentativas) + 1
                score_total += pontos_ganhos
                print(f"✅ Parabéns! Você acertou o {secreto} e ganhou {pontos_ganhos} pontos!")
                acertou_neste_round = True
                break # Para o while e vai para o próximo round
            elif palpite < secreto:
                print("Muito baixo!")
            else:
                print("Muito alto!")
        
        if not acertou_neste_round:
            print(f"❌ Suas tentativas acabaram! O número era {secreto}.")
        
        input("\nPressione Enter para continuar...")

    # 3. FINAL DO JOGO (Fora de todos os loops)
    limpar_tela()
    print(f"Fim de jogo! Seu score final: {score_total}")
    
    if score_total > recorde_atual:
        print(f"🏆 NOVO RECORDE! Você superou os {recorde_atual} pontos!")
        salvar_recorde(score_total)

# Iniciar
jogar()