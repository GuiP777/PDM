from datetime import datetime

# Obtem a hora do dia
def obter_saudacao():
    hora = datetime.now().hour
    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"