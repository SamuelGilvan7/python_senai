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
