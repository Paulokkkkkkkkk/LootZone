# chatbot_escola_2_1.py

import difflib

# Dicionário de perguntas e respostas
perguntas_respostas = {
    # Informações gerais
    "jogos destaques": "Nossos destaques estão sendo os jogos de ação e aventura, como 'The Legend of Zelda' e 'God of War'.",
    "formas de pagamento": "Aceitamos cartões de crédito, pix, débito, PayPal e boleto bancário.",
    "promocoes": "Estamos com uma promoção especial de 20% de desconto em todos os jogos do gênero casual durante esta semana!",
    "lançamentos": "Temos um lançamento incrível chegando em breve para os jogadores mobile: 'Red Dead Redemption 2'! Fique atento para mais detalhes.",
    "gêneros dos jogos": "Nossos jogos estão disponíveis em diversos gêneros, incluindo ação, aventura, casual, RPG e esportes.",
    
    #Jogos específicos
    "jogos multiplayer": "",
    "jogos singleplayer": "",
    "jogos mobiles": "",

    #plataformas
    "steam": "",
    "playStation": "",
    "xbox": "",
    "nintendo": "",
}

# Lista de opções numeradas
opcoes = [
    "jogos destaques",
    "formas de pagamento",
    "promocoes",
    "lancamentos",
    "gêneros dos jogos",
    "jogos multiplayer",
    "jogos singleplayer",
    "jogos mobiles",
    "steam",
    "playStation",
    "xbox",
    "nintendo",
    "Sair"
]

# Mapear número para chave do dicionário ou ação especial
mapa_opcoes = {
    1: "jogos destaques",
    2: "formas de pagamento",
    3: "promoções",
    4: "lançamentos",
    5: "gêneros de jogos",
    6: "jogos multiplayer",
    7: "jogos singleplayer",
    8: "jogos mobiles",
    9: "steam",
    10: "playstation",
    11: "xbox",
    12: "nintendo",
    13: "sair"
}


def obter_resposta(pergunta, perguntas_respostas, limite_similaridade=0.6):
    """Busca correspondência aproximada para perguntas livres."""
    pergunta = pergunta.lower().strip()
    chaves = list(perguntas_respostas.keys())
    melhor_match = difflib.get_close_matches(pergunta, chaves, n=1, cutoff=limite_similaridade)
    if melhor_match:
        return perguntas_respostas[melhor_match[0]]
    else:
        return "Desculpe, não entendi sua pergunta. Tente escolher uma das opções numeradas."

def iniciar_chat():
    print("=== Bem-vindo ao Chatbot da LootZone ===\n")

    while True:
        print("Escolha uma opção digitando o número correspondente:")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")

        try:
            escolha = int(input("\nSua escolha: "))
        except ValueError:
            print("Por favor, digite um número válido.\n")
            continue

        if escolha not in mapa_opcoes:
            print("Opção inválida, tente novamente.\n")
            continue

        acao = mapa_opcoes[escolha]

        if acao == "sair":
            print("\nChatbot: Obrigado pelo contato! Até mais.")
            break
        elif acao == "livre":
            pergunta_livre = input("\nDigite sua pergunta livre: ")
            resposta = obter_resposta(pergunta_livre, perguntas_respostas)
            print(f"\nChatbot: {resposta}\n")
        else:
            resposta = obter_resposta(acao, perguntas_respostas)
            print(f"\nChatbot: {resposta}\n")

if __name__ == "__main__":
    iniciar_chat()