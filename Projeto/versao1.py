# chatbot_escola.py

def obter_resposta(pergunta):
    # Dicionário de perguntas e respostas
    respostas = {
        "horario": "O horário da escola é das 07:00 às 17:00, de segunda a sexta.",
        "matricula": "As matrículas estão abertas até o dia 30 de junho. Procure a secretaria para mais informações.",
        "cursos": "Oferecemos cursos de Informática, Administração e Técnico em Desenvolvimento de Sistemas.",
        "contato": "Você pode nos contatar pelo telefone (11) 1234-5678 ou pelo e-mail contato@escola.com.br",
        "endereco": "Nossa escola fica na Rua das Flores, 123, Centro, Cidade Exemplo."
    }
    
    # Normaliza a pergunta
    chave = pergunta.lower().strip()
    
    # Busca a resposta
    if chave in respostas:
        return respostas[chave]
    else:
        return "Desculpe, não entendi sua pergunta. Tente: horario, matricula, cursos, contato ou endereco."

def iniciar_chat():
    print("=== Bem-vindo ao Chatbot da Escola ===")
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