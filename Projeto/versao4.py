# chatbot_escola_final4.py

import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import difflib

# Dicionário de perguntas e respostas detalhadas
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

# Função de correspondência aproximada
def obter_resposta(pergunta):
    pergunta = pergunta.lower().strip()
    chaves = list(perguntas_respostas.keys())
    melhor_match = difflib.get_close_matches(pergunta, chaves, n=1, cutoff=0.6)
    if melhor_match:
        return perguntas_respostas[melhor_match[0]]
    else:
        return "Desculpe, não entendi sua pergunta. Por favor, use os menus ou tente escrever de forma diferente."

# Enviar mensagem para a área de chat
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

# Função para botões de opção
def botao_opcao(chave):
    enviar_mensagem(chave)

# Função para atualizar botões do submenu de categoria
def atualizar_botoes_categoria(event):
    for widget in frame_botoes.winfo_children():
        widget.destroy()
    categoria = combo_categoria.get()
    botoes_categoria = []

    if categoria == "Geral":
        botoes_categoria = ["jogos destaques", "formas de pagamento", "promoções", "lançamentos", "gêneros de jogos"]
    elif categoria == "Jogos Específicos":
        botoes_categoria = ["jogos multiplayer", "jogos singleplayer", "jogos mobiles"]
    elif categoria == "Plataformas":
        botoes_categoria = ["steam", "playstation", "xbox", "nintendo"]
    elif categoria == "Suporte":
        botoes_categoria = ["gift cards", "reembolso", "suporte"]

    for chave in botoes_categoria:
        btn = tk.Button(frame_botoes, text=chave.replace("_", " ").title(), width=30, command=lambda c=chave: botao_opcao(c))
        btn.pack(pady=2)

# Configuração da interface
root = tk.Tk()
root.title("Chatbot da LootZone - Versão Final 4")
root.geometry("700x550")

# Área de chat
chat_area = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled', wrap='word')
chat_area.pack(padx=10, pady=10)

# Entrada de texto
entrada_frame = tk.Frame(root)
entrada_frame.pack(pady=5)

entrada_texto = tk.Entry(entrada_frame, width=50)
entrada_texto.pack(side=tk.LEFT, padx=5)

btn_enviar = tk.Button(entrada_frame, text="Enviar", width=12, command=lambda: enviar_mensagem())
btn_enviar.pack(side=tk.LEFT)

# Menu suspenso de categoria
frame_categoria = tk.Frame(root)
frame_categoria.pack(pady=5)

tk.Label(frame_categoria, text="Escolha uma categoria:").pack(side=tk.LEFT, padx=5)

combo_categoria = ttk.Combobox(frame_categoria, values=["Geral", "Jogos Específicos", "Plataformas", "Suporte"])
combo_categoria.current(0)
combo_categoria.bind("<<ComboboxSelected>>", atualizar_botoes_categoria)
combo_categoria.pack(side=tk.LEFT, padx=5)

# Frame para botões de submenu
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=5)

# Inicializa os botões da categoria padrão
atualizar_botoes_categoria(None)

# Botão de Sair
btn_sair = tk.Button(root, text="Sair", width=12, command=lambda: enviar_mensagem("sair"))
btn_sair.pack(pady=5)

root.mainloop()