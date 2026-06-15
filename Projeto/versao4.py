# chatbot_escola_final4.py

import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import difflib

# Dicionário de perguntas e respostas detalhadas
perguntas_respostas = {
    # Informações gerais
    "horario": "O horário da escola é das 07:00 às 17:00, de segunda a sexta-feira. As aulas começam pontualmente às 7h e terminam às 17h, incluindo intervalos regulares para alimentação e descanso.",
    "matricula": "As matrículas estão abertas até o dia 30 de junho. É necessário apresentar documentos pessoais e comprovante de residência na secretaria. Mais informações pelo telefone ou e-mail.",
    "cursos": "A escola oferece cursos de Informática, Administração e Técnico em Desenvolvimento de Sistemas, cada um com conteúdos práticos e teóricos para capacitar o aluno.",
    "contato": "Você pode entrar em contato pelo telefone (11) 1234-5678 ou pelo e-mail contato@escola.com.br. A secretaria atende de segunda a sexta-feira, das 7h às 17h.",
    "endereco": "A escola está localizada na Rua das Flores, 123, Centro, Cidade Exemplo. Fácil acesso por transporte público e estacionamento disponível no local.",

    # Curso Técnico em Desenvolvimento de Sistemas
    "desenvolvimento": "O curso Técnico em Desenvolvimento de Sistemas tem duração de 2 anos, abordando lógica de programação, linguagens como Python e Java, banco de dados, redes e automação. Preparação completa para atuar como desenvolvedor de software.",
    "curso desenvolvimento": "O aluno aprende a criar sistemas, desenvolver aplicações web e desktop, automatizar processos e gerenciar projetos de TI.",
    "disciplinas desenvolvimento": "Disciplinas incluem Lógica de Programação, Estrutura de Dados, Banco de Dados, Desenvolvimento Web, Automação e Projeto Integrador.",
    "habilidades desenvolvimento": "Ao final do curso, o aluno será capaz de programar, criar aplicações completas, trabalhar em equipe em projetos de TI e aplicar soluções automatizadas.",

    # Curso de Administração
    "administracao": "O curso de Administração tem duração de 2 anos, com foco em gestão, planejamento estratégico, finanças, marketing e empreendedorismo, preparando o aluno para atuar em diversas áreas empresariais.",
    "curso administracao": "O aluno aprende a organizar empresas, planejar estratégias, gerenciar equipes e tomar decisões administrativas eficientes.",
    "disciplinas administracao": "Disciplinas incluem Contabilidade, Gestão de Pessoas, Marketing, Planejamento Estratégico, Empreendedorismo e Projeto Integrador.",
    "habilidades administracao": "Ao final do curso, o aluno será capaz de gerir processos administrativos, planejar e executar estratégias de negócio, administrar finanças e liderar equipes."
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
        botoes_categoria = ["horario", "matricula", "cursos", "contato", "endereco"]
    elif categoria == "Desenvolvimento de Sistemas":
        botoes_categoria = ["desenvolvimento", "curso desenvolvimento", "disciplinas desenvolvimento", "habilidades desenvolvimento"]
    elif categoria == "Administração":
        botoes_categoria = ["administracao", "curso administracao", "disciplinas administracao", "habilidades administracao"]

    for chave in botoes_categoria:
        btn = tk.Button(frame_botoes, text=chave.replace("_", " ").title(), width=30, command=lambda c=chave: botao_opcao(c))
        btn.pack(pady=2)

# Configuração da interface
root = tk.Tk()
root.title("Chatbot da Escola - Versão Final 4")
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

combo_categoria = ttk.Combobox(frame_categoria, values=["Geral", "Desenvolvimento de Sistemas", "Administração"])
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