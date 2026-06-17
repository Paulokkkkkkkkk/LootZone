import tkinter as tk
from tkinter import scrolledtext
import difflib

# Dicionário de perguntas e respostas
perguntas_respostas = {
    # Informações gerais
    "jogos destaques": "Confira os jogos em destaque desta semana.",
    "matricula": "As matrículas estão abertas até o dia 30 de junho. Procure a secretaria para mais informações.",
    "cursos": "Oferecemos cursos de Informática, Administração e Técnico em Desenvolvimento de Sistemas.",
    "contato": "Você pode nos contatar pelo telefone (11) 1234-5678 ou pelo e-mail contato@escola.com.br",
    "endereco": "Nossa escola fica na Rua das Flores, 123, Centro, Cidade Exemplo.",

    # Curso Técnico em Desenvolvimento de Sistemas
    "desenvolvimento": "O curso Técnico em Desenvolvimento de Sistemas tem duração de 2 anos, abordando programação, bancos de dados e automação.",
    "curso desenvolvimento": "O curso oferece conhecimentos em Python, Java, SQL, redes e práticas de desenvolvimento de software.",
    "disciplinas desenvolvimento": "Algumas disciplinas: Lógica de Programação, Estrutura de Dados, Banco de Dados, Desenvolvimento Web e Automação.",
    "habilidades desenvolvimento": "Os alunos aprendem a criar sistemas, desenvolver aplicações e automatizar processos de forma prática.",

    # Curso de Administração
    "administracao": "O curso de Administração tem duração de 2 anos, abordando gestão, finanças, marketing e empreendedorismo.",
    "curso administracao": "O curso prepara o aluno para funções administrativas, planejamento estratégico e gestão de equipes.",
    "disciplinas administracao": "Algumas disciplinas: Contabilidade, Gestão de Pessoas, Marketing, Planejamento Estratégico e Empreendedorismo.",
    "habilidades administracao": "Os alunos aprendem a gerir empresas, tomar decisões estratégicas e organizar processos administrativos."
}

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
    "16. Pergunta livre",
    "17. Sair"
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
    13: "livre",
    14: "sair"
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