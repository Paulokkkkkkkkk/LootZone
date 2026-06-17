# chatbot_escola.py

def obter_resposta(pergunta):
    # Dicionário de perguntas e respostas
    respostas = {
        "jogos destaques": "Nossos destaques estão sendo os jogos de ação e aventura, como 'The Legend of Zelda' e 'God of War'.",
        "formas de pagamento": "Aceitamos cartões de crédito, pix, débito, PayPal e boleto bancário.",
        "promocoes": "Estamos com uma promoção especial de 20% de desconto em todos os jogos do gênero casual durante esta semana!",
        "lançamentos": "Temos um lançamento incrível chegando em breve para os jogadores mobile: 'Red Dead Redemption 2'! Fique atento para mais detalhes.",
        "gênero dos jogos": "Nossos jogos estão disponíveis em diversos gêneros, incluindo ação, aventura, casual, RPG e esportes."
    }
    
    # Normaliza a pergunta
    chave = pergunta.lower().strip()
    
    # Busca a resposta
    if chave in respostas:
        return respostas[chave]
    else:
        return "Desculpe, não entendi sua pergunta. Tente: jogos destaques, formas de pagamento, promoções, lançamentos ou gênero dos jogos."

def iniciar_chat():
    print("=== Bem-vindo ao Chatbot da LootZone ===")
    print("Digite 'sair' para encerrar a conversa.\n")
    
    while True:
        pergunta = input("Você: ")
        
        if pergunta.lower() == "sair":
            print("Chatbot: Obrigado pelo contato! Até mais.")
            break
        
        resposta = obter_resposta(pergunta)
        print(f"Chatbot: {resposta}\n")

# Executa o chatbot
if __name__ == "__main__":
    iniciar_chat()