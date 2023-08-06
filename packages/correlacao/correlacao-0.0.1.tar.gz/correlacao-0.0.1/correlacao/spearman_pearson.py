import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def start(df, alvo):
    df['alvo'] = alvo
    correlations_s = df.corr(method = 'spearman')
    correlations_p = df.corr(method = 'pearson')
    print('Valores Spearman: ')
    print(correlations_s['alvo'])
    print('--------------------------------------------------')
    print('Valores Pearson: ')
    print(correlations_p['alvo'])

    plt.figure(figsize=(10,6))
    spearman = correlations_s['alvo'].drop('alvo').sort_values(ascending=False)
    pearson = correlations_p['alvo'].drop('alvo').sort_values(ascending=False)
    plot_graf = pd.DataFrame(columns=['Spearman','Pearson'])
    plot_graf['Spearman'] = spearman
    plot_graf['Pearson'] =  pearson
    plot_graf['Spearman'].plot(kind='barh',color="0.8")
    plot_graf['Pearson'].plot(kind='barh',color="#4F4F4F")
    plt.xlim(-1,1)
    plt.xlabel('Correlação', fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.grid(None)
    plt.legend(loc='upper right',fontsize=16)
    plt.show()



