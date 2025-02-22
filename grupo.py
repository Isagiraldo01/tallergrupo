df_avg = df.groupby('origin', as_index=False)['mpg'].mean()

fig = px.bar(df_avg, x='origin', y='mpg', text='mpg', 
             title='Consumo Promedio de Combustible por Región', 
             color='origin')
fig.show()
