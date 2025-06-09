meu_dicionario = {
    "nome": "Leandro",
    "idade": 30,
    "cidade": "São Paulo"
}

# --------------------------------
# Acessar um valor
print(meu_dicionario["nome"])  # Saída: Leandro

print("=" * 80)
# --------------------------------
# Adicionar ou alterar um valor
meu_dicionario["idade"] = 31  # Atualiza a idade
meu_dicionario["profissão"] = "Analista"  # Adiciona nova chave
print(meu_dicionario)

print("=" * 80)

# --------------------------------
# Remover um item
del meu_dicionario["cidade"]  # Remove a chave 'cidade'
print(meu_dicionario)

print("=" * 80)

# --------------------------------
# Percorrer o dicionário
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

print("=" * 80)

# --------------------------------
# Verificar se uma chave existe
if "nome" in meu_dicionario:
    print("Nome encontrado!")

print("=" * 80)

# --------------------------------
# Métodos úteis
chaves = meu_dicionario.keys()      # retorna todas as chaves
valores = meu_dicionario.values()   # retorna todos os valores
itens = meu_dicionario.items()      # retorna pares (chave, valor)

print("=" * 80)

# Exemplo completo
pessoa = {
    "nome": "Joana",
    "idade": 25
}

pessoa["cidade"] = "Recife" # adicionando
pessoa["idade"] = 26        # alterando

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print("=" * 80)