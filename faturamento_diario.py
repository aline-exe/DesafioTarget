import json

with open("dados.json",'r') as json_arquivo:
    faturamento = json.load(json_arquivo)
    
faturamento_n_nulo = [dia['valor'] for dia in faturamento if dia['valor'] != 0.0] #incluir apenas os dados onde 'valor' é maior que 0 pra não contar na média

menor_faturamento = min(faturamento_n_nulo)
maior_faturamento = max(faturamento_n_nulo)

media = sum(faturamento_n_nulo)/len(faturamento_n_nulo)

print(f'A média do faturamento foi de R${media}.')
print(f'Sendo o maior faturamento R${maior_faturamento}, e o menor, R${menor_faturamento}.')