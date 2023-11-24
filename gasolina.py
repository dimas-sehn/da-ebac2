import pandas as pd
import seaborn as sns

dados_gasolina = pd.read_csv('gasolina.csv')

with sns.axes_style('darkgrid'):
  grafico_gasolina = sns.lineplot(
      x = 'dia',
      y = 'venda',
      data = dados_gasolina
  )

  grafico_gasolina.set(
      title = 'Valor médio de venda',
      xlabel = 'Dia_aferido',
      ylabel = 'Valor (R$)'
  )

  figura = grafico_gasolina.get_figure()
  figura.savefig('gasolina.png', dpi=600)
