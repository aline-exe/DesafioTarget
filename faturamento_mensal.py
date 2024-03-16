faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53


total_faturamento = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

percentual_sp = (faturamento_sp/total_faturamento) * 100
percentual_rj = (faturamento_rj/total_faturamento) * 100
percentual_mg = (faturamento_mg/total_faturamento) * 100
percentual_es = (faturamento_es/total_faturamento) * 100
percentual_outros = (faturamento_outros/total_faturamento) * 100

print(f'Percentual de faturamento de SP: {percentual_sp:.2f}%')
print(f'Percentual de faturamento de RJ: {percentual_rj:.2f}%')
print(f'Percentual de faturamento de MG: {percentual_mg:.2f}%')
print(f'Percentual de faturamento de ES: {percentual_es:.2f}%')
print(f'Percentual de faturamento de outros: {percentual_outros:.2f}%')
