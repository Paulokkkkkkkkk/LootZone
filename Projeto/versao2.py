# chatbot_escola_2_1.py

import difflib

# Dicionário de perguntas e respostas
perguntas_respostas = {
    # Informações gerais
    "horario": "O horário da escola é das 07:00 às 17:00, de segunda a sexta.",
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

# Lista de opções numeradas
opcoes = [
    "Horário da escola",
    "Matrícula",
    "Cursos oferecidos",
    "Contato",
    "Endereço",
    "Curso Desenvolvimento de Sistemas",
    "Disciplinas Desenvolvimento de Sistemas",
    "Habilidades Desenvolvimento de Sistemas",
    "Curso Administração",
    "Disciplinas Administração",
    "Habilidades Administração",
    "Escrever pergunta livre",
    "Sair"
]

# Mapear número para chave do dicionário ou ação especial
mapa_opcoes = {
    1: "horario",
    2: "matricula",
    3: "cursos",
    4: "contato",
    5: "endereco",
    6: "desenvolvimento",
    7: "disciplinas desenvolvimento",
    8: "habilidades desenvolvimento",
    9: "administracao",
    10: "disciplinas administracao",
    11: "habilidades administracao",
    12: "livre",
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
    print("=== Bem-vindo ao Chatbot da Escola ===\n")

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