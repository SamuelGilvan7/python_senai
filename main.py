#01
print("Digite seu login")
login_digitado = input("login:")
print("Digite sua senha:")
senha_digitada = input("Senha:")

login_salvo = "admin_ti"
senha_salva = "Sistema@admin"

if (login_digitado == login_salvo) and (senha_digitada == senha_salva):
    print("Acesso Concedido. Bem-vindo ao Painel de Controle.")
elif (login_digitado == "guest") and (senha_digitada == "123456"):
     print("Acesso Negado: Credenciais de baixo risco ou padrão de segurança.")
else:
     print("Erro de acesso:Login ou Senha Invalidos.")


#Cond

#1
login_salvo = "admin_ti"
senha_salva = "Sistema@123"

login_digitado = input("Digite o login: ")
senha_digitada = input("Digite a senha: ")

if login_digitado == login_salvo and senha_digitada == senha_salva:
    print("Acesso Concedido. Bem-vindo ao Painel de Controle.")
elif login_digitado == "guest" or senha_digitada == "123456":
    print("Acesso Negado: Credenciais de baixo risco ou padrão de segurança.")
else:
    print("Erro de Acesso: Login ou Senha inválidos.")

#02
chamado = {
    "equipamento": "Servidor Principal",
    "tempo_parado_horas": 5,
    "setor": "Financeiro",
    "status": "aberto"
}

if chamado["equipamento"] == "Servidor Principal" or chamado["tempo_parado_horas"] > 4:
    prioridade = "P1 - Crítica"
elif chamado["setor"] == "Financeiro" and chamado["tempo_parado_horas"] > 1:
    prioridade = "P2 - Alta"
else:
    prioridade = "P3 - Normal"

#03  
softwares_criticos = ["ERP", "Banco de Dados SQL", "Firewall"]
software_novo = input("Digite o nome do software a ser instalado: ")

if software_novo in softwares_criticos:
    print("Atenção: Este software é crítico e já está instalado. Nenhuma alteração é necessária.")
else:
    print("Software não encontrado na lista. Iniciando instalação...")
    softwares_criticos.append(software_novo)
    print("Instalação concluída com sucesso.")

print("Lista atualizada de softwares críticos:")
print(softwares_criticos)  

# Saída
print(f"Equipamento: {chamado['equipamento']}")
print(f"Prioridade definida: {prioridade}")

# 01
num = int(input("Informe qual será a tabuada:"))

for n in range(11):
    print (f"{num} x {n} = {n * num}")

#02

inventario = [
 {"id": 101, "modelo": "Notebook i5", "status": "ativo"},
 {"id": 102, "modelo": "Desktop i3", "status": "manutenção"},
 {"id": 103, "modelo": "Notebook i7", "status": "ativo"},
 {"id": 104, "modelo": "Servidor Dell", "status": "ativo"}
]

for item in inventario:
    if item["status"] == "ativo":
        print(item["modelo"])
   
            
#3
total_critica = 0
pontuacoes = [5, 9, 3, 10, 2, 7, 8] 

for n in range(len(pontuacoes)):
    if pontuacoes [n] >= 8:
        total_critica +=1  
print(f"O total de máquinas em Situação Crítica: {total_critica}")

"""for item in  pontuacoes:
    if item >= 8:
        total_critica += 1"""
