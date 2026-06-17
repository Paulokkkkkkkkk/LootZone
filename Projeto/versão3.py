import tkinter as tk
from tkinter import scrolledtext
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
    "jogos multiplayer": "Temos ótimos jogos multiplayer, como 'Among Us', 'Fortnite' e 'Call of Duty: Warzone', que proporcionam diversão e competição online com amigos e jogadores de todo o mundo.",
    "jogos singleplayer": "Temos uma excelente seleção de jogos singleplayer, incluindo títulos de ação, aventura e RPG que oferecem histórias envolventes e jogabilidade imersiva.",
    "jogos mobiles": "Oferecemos uma ampla variedade de jogos mobiles para todos os gostos, desde clássicos até lançamentos exclusivos para dispositivos móveis.",

    #plataformas
    "steam": "Jogos disponíveis na Steam incluem uma vasta gama de gêneros, desde indie até AAA, com títulos populares como 'Counter-Strike: Global Offensive', 'Hollow Knight' e 'The Witcher 3'.",
    "playStation": "A PlayStation oferece uma ampla seleção de jogos exclusivos e aclamados, incluindo títulos da série 'The Last of Us' e 'God of War'.",
    "xbox": "A Xbox possui uma biblioteca diversificada de jogos, com destaque para títulos exclusivos como 'Halo' e 'Forza'.",
    "nintendo": "A Nintendo é conhecida por seus títulos icônicos, como 'The Legend of Zelda' e 'Mario', que oferecem experiências únicas e envolventes.",

    #suporte
    "gift cards": "Oferecemos gift cards para diversas plataformas, incluindo Steam, PlayStation, Xbox e Nintendo. Você pode adquirir nossos gift cards em nosso site ou em lojas parceiras.",
    "reembolso": "Para solicitar um reembolso, por favor, entre em contato com nosso suporte ao cliente através do e-mail suporte@lootzone.com.",
    "suporte": "Nosso suporte ao cliente está disponível 24/7 para ajudar com qualquer dúvida ou problema que você possa ter. Entre em contato conosco pelo e-mail suporte@lootzone.com."
}

# Lista de opções numeradas

opcoes = [
    "1. Jogos Destaques",
    "2. Formas de Pagamento",
    "3. Promoções",
    "4. Lançamentos",
    "5. Gêneros de jogos",
    "6. Jogos Multiplayer",
    "7. Jogos Singleplayer",
    "8. Jogos Mobiles",
    "9. Steam",
    "10. PlayStation",
    "11. Xbox",
    "12. Nintendo",
    "13. Gift Cards",
    "14. Reembolso",
    "15. Suporte",
    "16. Sair"
]

# Mapear número para chave ou ação especial
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
    13: "gift cards",
    14: "reembolso",
    15: "suporte",
    16: "sair"
}

# Função para obter resposta aproximada
def obter_resposta(pergunta):
    pergunta = pergunta.lower().strip()
    chaves = list(perguntas_respostas.keys())
    melhor_match = difflib.get_close_matches(pergunta, chaves, n=1, cutoff=0.6)
    if melhor_match:
        return perguntas_respostas[melhor_match[0]]
    else:
        return "Desculpe, não entendi sua pergunta. Use os botões ou tente outra frase."

# Função para enviar mensagem
def enviar_mensagem(pergunta=None):
    if pergunta is None:
        pergunta = entrada_texto.get()
        entrada_texto.delete(0, tk.END)
    if pergunta.strip() == "":
        return
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"Você: {pergunta}\n")
    
    if pergunta.lower() == "sair":
        chat_area.insert(tk.END, "Chatbot: Obrigado pelo contato! Até mais.\n")
        chat_area.config(state='disabled')
        return

    resposta = obter_resposta(pergunta)
    chat_area.insert(tk.END, f"Chatbot: {resposta}\n\n")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)

# Função para botões de opções
def botao_opcao(numero):
    acao = mapa_opcoes[numero]
    if acao == "sair":
        enviar_mensagem("sair")
    elif acao == "livre":
        pergunta_livre = entrada_texto.get()
        if pergunta_livre.strip() == "":
            pergunta_livre = "Escreva sua pergunta aqui..."
        enviar_mensagem(pergunta_livre)
    else:
        enviar_mensagem(acao)

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Chatbot da LootZone")

# Área de chat
chat_area = scrolledtext.ScrolledText(root, width=70, height=20, state='disabled', wrap='word')
chat_area.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Entrada de texto
entrada_texto = tk.Entry(root, width=50)
entrada_texto.grid(row=1, column=0, padx=10, pady=10)

# Botão enviar texto
btn_enviar = tk.Button(root, text="Enviar", width=12, command=lambda: enviar_mensagem())
btn_enviar.grid(row=1, column=1, padx=5, pady=10)

# Criar botões para opções numeradas
for i, opcao in enumerate(opcoes, start=1):
    linha = 2 + (i-1)//4
    coluna = (i-1)%4
    btn = tk.Button(root, text=opcao, width=20, command=lambda i=i: botao_opcao(i))
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

# Inicia interface
root.mainloop()