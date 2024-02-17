from tabela_Info import TabelaInfo  

# Criando objetos e armazenando-os em uma lista
objeto1 = TabelaInfo("Ronaldotraveco", 1, 42, "maconheiro", 300000)
objeto2 = TabelaInfo("Isadoraleite", 2, 20, "maconheiro", 7000)
objeto3 = TabelaInfo("otavio", 3, 26, "maconheiro", 5000)
objeto4 = TabelaInfo("Bernas", 4, 17, "devastaTheka", 1000)

lista_objetos = [objeto1, objeto2, objeto3, objeto4]

# Função para filtrar os objetos
def filtrar_objetos(lista, idade=None, salario=None, id=None):
    objetos_filtrados = []

    for obj in lista:
        if idade is not None and obj.idade < idade:
            continue
        if salario is not None and obj.salario < salario:
            continue
        if id is not None and obj.id < id:
            continue
        objetos_filtrados.append(obj)

    return objetos_filtrados

# Input do usuário para decidir se deseja filtrar
resposta = input("Deseja filtrar os objetos? (sim/não): ")

if resposta.lower() == "sim":
    idade_filtro = int(input("Filtrar a partir de qual idade? (Digite um número inteiro): "))

    salario_filtro = int(input("Filtrar a partir de qual salário? (Digite um número inteiro): "))

    id_filtro = int(input("Filtrar a partir de qual ID? (Digite um número inteiro): "))

    objetos_filtrados = filtrar_objetos(lista_objetos, idade_filtro, salario_filtro, id_filtro)

    # Mostrando os objetos filtrados
    print("\nObjetos filtrados:")
    for obj in objetos_filtrados:

        print(f"Nome: {obj.nome}, ID: {obj.id}, Idade: {obj.idade}, Vulgo: {obj.vulgo}, Salário: {obj.salario}")
else:
    print("\nObjetos sem filtro:")
    
    for obj in lista_objetos:
        print(f"Nome: {obj.nome}, ID: {obj.id}, Idade: {obj.idade}, Vulgo: {obj.vulgo}, Salário: {obj.salario}")
