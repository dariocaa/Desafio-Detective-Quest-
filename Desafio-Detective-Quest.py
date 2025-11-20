# Desafio-Detective-Quest: O Mistério da Chave Perdida

def iniciar_missao():
    """
    Função principal para o mini-jogo de detetive.
    O objetivo é encontrar a chave secreta.
    """
    
    # 

[Image of a magnifying glass over code]


    # Dicionário com as "Pistas"
    # A chave correta (solução) está camuflada aqui
    dados_confidenciais = {
        "cor_favorita": "azul",
        "animal_misterioso": "Coruja",
        "codigo_secreto": "PIRULITO_DOCE_2024", # <--- A chave correta
        "fruta_rara": "lichia",
        "nome_do_agente": "Sr. Smith"
    }

    # O "Segredo" que o detetive deve encontrar
    segredo = "A senha de acesso ao cofre é '1-3-5-7'."

    print("--- Missão: Chave Perdida ---")
    print("Você é um Detetive e precisa descobrir a Chave Secreta para desbloquear o Segredo.")
    print("Analise as pistas disponíveis no código (dados_confidenciais) e insira a chave correta.")
    print("Pistas:** 'cor_favorita', 'animal_misterioso', 'fruta_rara', 'nome_do_agente', 'codigo_secreto'")
    
    # Loop de tentativas
    tentativas = 0
    while True:
        tentativas += 1
        chave_digitada = input("\nDetetive, insira sua tentativa de Chave: ").strip()

        if chave_digitada in dados_confidenciais:
            
            # Condição de Vitoria
            if chave_digitada == "codigo_secreto":
                print(f"\n✅ **SUCESSO!** A chave '{chave_digitada}' está correta!")
                print(f"O Segredo Desbloqueado é: **{segredo}**")
                print(f"Você resolveu o mistério em {tentativas} tentativa(s)!")
                break
            else:
                # Caso a chave exista, mas não seja a chave-mestra
                valor_pista = dados_confidenciais[chave_digitada]
                print(f"💡 Pista Encontrada! O valor da chave '{chave_digitada}' é: '{valor_pista}'")
                print("Continue procurando a Chave Secreta!")
        
        else:
            print("❌ Erro. Essa chave não existe nas pistas. Tente novamente!")

# Executa o jogo
if __name__ == "__main__":
    iniciar_missao()