import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("C:\\Users\\USER\\Desktop\\drive_eba\\top10s.csv", encoding="ISO-8859-1")

df.head

##grafico de barras

top_genre=(df.
           groupby('top genre')
           ['title']
           .count()
           .to_frame()
           .reset_index())

fig=px.bar(top_genre,x='top genre',y='title')
fig.show()

##melhorando o grafico de barras , utilizando as cores do spotify
fig=px.bar(top_genre,x='top genre',y='title')
fig.update_traces(marker_color='#1db954') #alterar a cor das barras
fig.update_layout(title_text='Numero de musicas por genero', font_family='Courier New',
                  font_color='#1db954',
                  title_font_family='Courier New',
                  title_font_color='#1db954',
                  legend_title_font_color='#1db954',
                  plot_bgcolor='#191414',
                  height=700,
                  width=1300)  #alterar layout , colocar titulo, cor do titulo, fonte,altura, largura, fundo
fig.update_yaxes(showgrid=False,zeroline=False,visible=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,visible=True,hoverformat=None,categoryorder='total descending')
fig.show()

#grafico de barras trazendo so o top10
top_genre_top10=(df.
           groupby('top genre')
           ['title']
           .count()
           .to_frame()
           .reset_index()
           [:10])

fig=px.bar(top_genre_top10,x='top genre',y='title')
fig.update_traces(marker_color='#1db954') #alterar a cor das barras
fig.update_layout(title_text='Numero de musicas por genero', font_family='Courier New',
                  font_color='#1db954',
                  title_font_family='Courier New',
                  title_font_color='#1db954',
                  legend_title_font_color='#1db954',
                  plot_bgcolor='#191414',
                  height=700,
                  width=1300)  #alterar layout , colocar titulo, cor do titulo, fonte,altura, largura, fundo
fig.update_yaxes(showgrid=False,zeroline=False,visible=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,visible=True,hoverformat=None,categoryorder='total descending')
fig.show()

df.head

## grafico de barras empilhadas - por ano e genero
df_empilhado=(df.
              groupby(['year','top genre'])
              ['title'] #contar as musicas
              .count()
              .to_frame() #criar o dataframe
              .reset_index()
              )

df_empilhado.head()

fig=px.bar(df_empilhado,x='year',y='title',color='top genre' , barmode='stack')
fig.show()

##grafico barras empilhadas com o top5 categorias e alteração de layout
df_empilhado2=df_empilhado.loc[df_empilhado['top genre'].isin(['dance pop','pop','canadian pop','barbadian pop','boy band'])]
fig=px.bar(df_empilhado2,x='year',y='title',color='top genre' , color_discrete_sequence=['#1db954','#0C4F24','#D3E5D9','#679778','#57615A'], barmode='stack')
fig.update_layout(title_text='Numero de musicas por genero', font_family='Courier New',
                  font_color='#1db954',
                  title_font_family='Courier New',
                  title_font_color='#1db954',
                  legend_title_font_color='#1db954',
                  plot_bgcolor='#807E7E',
                  height=700,
                  width=1300)
fig.update_yaxes(showgrid=False,zeroline=False,visible=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,visible=True,hoverformat=None,categoryorder='total descending',tickmode='linear')
fig.show()

##grafico agrupado
#ao inves de as categorias serem as barrinhas em cima da outra, serão as barrinhas uma ao lado da outra
fig=px.bar(df_empilhado,x='year',y='title',color='top genre' , barmode='group')
fig.show()

##grafico agrupado com alteração de layout
fig=px.bar(df_empilhado2,x='year',y='title',color='top genre' , color_discrete_sequence=['#1db954','#0C4F24','#D3E5D9','#679778','#57615A'], barmode='group')
fig.update_layout(title_text='Numero de musicas por genero', font_family='Courier New',
                  font_color='#1db954',
                  title_font_family='Courier New',
                  title_font_color='#1db954',
                  legend_title_font_color='#1db954',
                  plot_bgcolor='#807E7E',
                  height=700,
                  width=1300)
fig.update_yaxes(showgrid=False,zeroline=False,visible=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,visible=True,hoverformat=None,categoryorder='total descending',tickmode='linear')
fig.show()

##grafico de pizza
fig=px.pie(df_empilhado, values='title', names = 'year')
fig.show()

##grafico de pizza com alteração de layout
df3=(df_empilhado
     .groupby('year')
     ['title']
     .sum()
     .to_frame()
     .reset_index()
     .query("year>=2017")
     )

fig=px.pie(df3, values='title', names = 'year',color_discrete_sequence=['#1db954','#0C4F24','#D3E5D9'])
fig.show()


##grafico de rosca
fig=px.pie(df_empilhado, values='title', names = 'year')
fig.update_traces(hole=0.4) #esse comando que faz ter o buraco no meio, quanto maior o numero maior fica
fig.show()

##grafico de rosca com alteração de layout
fig=px.pie(df3, values='title', names = 'year',color_discrete_sequence=['#1db954','#0C4F24','#D3E5D9'])
fig.update_traces(hole=0.5) #esse comando que faz ter o buraco no meio, quanto maior o numero maior fica
fig.show()


##histograma
fig=px.histogram(df,x='year')
fig.show()

#histograma com alteração de layout
fig=px.histogram(df,x='year')
fig.update_traces(marker_color='#1db954') #alterar a cor das barras
fig.update_layout(title_text='Numero de musicas por genero', font_family='Courier New',
                  font_color='#1db954',
                  title_font_family='Courier New',
                  title_font_color='#1db954',
                  legend_title_font_color='#1db954',
                  plot_bgcolor='#191414',
                  height=700,
                  width=1300)  #alterar layout , colocar titulo, cor do titulo, fonte,altura, largura, fundo
fig.update_yaxes(showgrid=False,zeroline=False,visible=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,visible=True,hoverformat=None)
fig.show()

##histograma com boxplot
fig=px.histogram(df,x='year',marginal='box')
fig.show()

##histograma com boxplot com alteração de layout
fig=px.histogram(df,x='year', marginal='box')
fig.update_traces(marker_color='#1db954') #alterar a cor das barras
fig.update_layout(title_text='Numero de musicas por genero', font_family='Courier New',
                  font_color='#1db954',
                  title_font_family='Courier New',
                  title_font_color='#1db954',
                  legend_title_font_color='#1db954',
                  plot_bgcolor='#191414',
                  height=700,
                  width=1300)  #alterar layout , colocar titulo, cor do titulo, fonte,altura, largura, fundo
fig.update_yaxes(showgrid=False,zeroline=False,visible=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,visible=True,hoverformat=None)
fig.show()

##histograma violino
fig=px.histogram(df,x='year',marginal='violin')
fig.show()

##histograma violino com alteração de layout
fig=px.histogram(df,x='year', marginal='violin')
fig.update_traces(marker_color='#1db954') #alterar a cor das barras
fig.update_layout(title_text='Numero de musicas por genero', font_family='Courier New',
                  font_color='#1db954',
                  title_font_family='Courier New',
                  title_font_color='#1db954',
                  legend_title_font_color='#1db954',
                  plot_bgcolor='#191414',
                  height=700,
                  width=1300)  #alterar layout , colocar titulo, cor do titulo, fonte,altura, largura, fundo
fig.update_yaxes(showgrid=False,zeroline=False,visible=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,visible=True,hoverformat=None)
fig.show()

##scatterplot
fig=px.scatter(df,x='nrgy', y='dnce')
fig.show()

##scatterplot com alteração de layout
fig=px.scatter(df,x='nrgy', y='dnce')
fig.update_traces(marker_color='#1db954')
fig.update_yaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.show()

##scatterplot aumentando o tamanho das bolinhas
fig=px.scatter(df,x='nrgy', y='dnce',size='dur')
fig.show()

##scatterplot aumentando o tamanho dos pontos e alterando layout
fig=px.scatter(df,x='nrgy', y='dnce',size='dur')
fig.update_traces(marker_color='#1db954')
fig.update_yaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.show()

#incluir outro parametro e dividir por genero
fig=px.scatter(df,x='nrgy', y='dnce',size='dur',color='top genre')
fig.show()

#incluir outro parametro e dividir por genero / por categorias - limitando a top
df_2=df.loc[df['top genre'].isin(['dance pop','pop','canadian pop','barbadian pop','boy band'])]
fig=px.scatter(df_2,x='nrgy', y='dnce',size='dur', color='top genre',color_discrete_sequence=['#1db954','#0C4F24','#D3E5D9','#679778','#57615A'])
fig.update_yaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.show()

#criar um scatterplot usando simbolos ao inves de bolinha
fig=px.scatter(df,x='nrgy', y='dnce',size='dur',symbol='top genre')
fig.show()

fig=px.scatter(df,x='nrgy', y='dnce',size='dur',symbol='top genre', color='top genre')
fig.show()

#criar um scatterplot usando simbolos ao inves de bolinha e alterando layout
fig=px.scatter(df_2,x='nrgy', y='dnce',size='dur', color='top genre',symbol='top genre',color_discrete_sequence=['#1db954','#0C4F24','#D3E5D9','#679778','#57615A'])
fig.update_yaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.show()

##grafico de linhas
fig=px.line(top_genre, x='top genre', y='title')
fig.show()

##grafico de linhas e alterando layout
fig=px.line(top_genre,x='top genre',y='title')
fig.update_traces(marker_color='#1db954') #alterar a cor da linha
fig.update_layout(title_text='Numero de musicas por genero', font_family='Courier New',
                  font_color='#1db954',
                  title_font_family='Courier New',
                  title_font_color='#1db954',
                  legend_title_font_color='#1db954',
                  plot_bgcolor='#191414',
                  height=700,
                  width=1300)  #alterar layout , colocar titulo, cor do titulo, fonte,altura, largura, fundo
fig.update_yaxes(showgrid=False,zeroline=False,visible=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,visible=True,hoverformat=None,categoryorder='total descending')
fig.show()

##melhorando mais ainda e organizando as linhas do grafico de linhas
## tirar o category order
fig=px.line(top_genre,x='top genre',y='title',title='title')
fig.update_traces(marker_color='#1db954',line=go.scatter.Line(color='white'),textposition='bottom right') #alterar a cor da linha
fig.update_layout(title_text='Numero de musicas por genero', font_family='Courier New',
                  font_color='#1db954',
                  title_font_family='Courier New',
                  title_font_color='#1db954',
                  legend_title_font_color='white',
                  plot_bgcolor='#191414',
                  height=700,
                  width=1300)  #alterar layout , colocar titulo, cor do titulo, fonte,altura, largura, fundo
fig.update_yaxes(showgrid=False,zeroline=False,visible=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,visible=True,hoverformat=None)
fig.show()

top_genre.head()