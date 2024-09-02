This repository contains the documentation of my studies in statistics using Python. Throughout this project, I am exploring different aspects of data analysis, visualization, and statistical interpretation, focusing on the practical application of these concepts.

#Content

1.Python Code:

- Each section of this file presents the code I used to perform statistical analyses, create graphs, and interpret data.
- The code is commented to facilitate understanding and following the steps of the analysis.
  
2.Graphical Visualizations:

- The graphs included in this document were generated using the Plotly library.
- The graphs are highlighted in shades of green, representing the Spotify data used in the analyses.
- The visualizations were chosen to clearly illustrate the insights obtained from the data.
  
#Structure

- Data Analysis: A section where I explore the Spotify dataset, addressing aspects such as distribution, central tendency, dispersion, among others.
- Data Visualization: Practical examples of how to use Plotly to create interactive and visually appealing graphs.

#Final Remarks

This repository will be regularly updated as I progress in my studies. Feel free to explore, suggest improvements, or contribute to the project.

- Here is an example of Python code that I used to create a bar chart with Spotify data:

```python
fig = px.bar(top_genre, x='top genre', y='title')
fig.update_traces(marker_color='#1db954')  # Alterar a cor das barras
fig.update_layout(
    title_text='Número de músicas por gênero',
    font_family='Courier New',
    font_color='#1db954',
    title_font_family='Courier New',
    title_font_color='#1db954',
    legend_title_font_color='#1db954',
    plot_bgcolor='#191414',
    height=700,
    width=1300  # Alterar layout: colocar título, cor do título, fonte, altura, largura, fundo
)
fig.update_yaxes(showgrid=False, zeroline=False, visible=False, hoverformat=None)
fig.update_xaxes(showgrid=False, zeroline=False, visible=True, hoverformat=None, categoryorder='total descending')
fig.show()
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/bar_chart.JPG)

- Here is an example of Python code that I used to create a bar chart with Spotify data using only top10:

```python
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
```
![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/top10_chart_bar.png)

- Here is an example of Python code that I used to create a stacked bar chart with Spotify data:

```python
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
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/stacked_bar_chart.png)

- Here is an example of Python code that I used to create a clustered bar chart with Spotify data:

```python
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
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/clustered_bar_chart.png)

- Here is an example of Python code that I used to create a pizza chart with Spotify data:

```python
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
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/pizza_chart.png)

- Here is an example of Python code that I used to create a donut chart with Spotify data:

```python
fig=px.pie(df3, values='title', names = 'year',color_discrete_sequence=['#1db954','#0C4F24','#D3E5D9'])
fig.update_traces(hole=0.5) #esse comando que faz ter o buraco no meio, quanto maior o numero maior fica
fig.show()
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/donut_chart.png)

- Here is an example of Python code that I used to create a histogram with Spotify data:

```python
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
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/histogram.png)

- histogram bloxpot

```python
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
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/histogram_bloxpot.png)

- histogram violin

```python

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
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/histogram_violin.png)

- Here is an example of Python code that I used to create a scatterplot with Spotify data:

```python
fig=px.scatter(df,x='nrgy', y='dnce')
fig.update_traces(marker_color='#1db954')
fig.update_yaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.show()
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/scatterplot.png)

- This is a scatter plot where I increased the size of the markers.

```python
fig=px.scatter(df,x='nrgy', y='dnce',size='dur')
fig.update_traces(marker_color='#1db954')
fig.update_yaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.show()
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/sactterplot_large.png)

- This is a scatterplot where I included another parameter and divided the data by genre/categories, limiting the results to the top 5.

```python
df_2=df.loc[df['top genre'].isin(['dance pop','pop','canadian pop','barbadian pop','boy band'])]
fig=px.scatter(df_2,x='nrgy', y='dnce',size='dur', color='top genre',color_discrete_sequence=['#1db954','#0C4F24','#D3E5D9','#679778','#57615A'])
fig.update_yaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.show()
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/scatterplo_by_category.png)

- This is a scatterplot where I used symbols instead of circular markers.

```python
fig=px.scatter(df_2,x='nrgy', y='dnce',size='dur', color='top genre',symbol='top genre',color_discrete_sequence=['#1db954','#0C4F24','#D3E5D9','#679778','#57615A'])
fig.update_yaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.update_xaxes(showgrid=False,zeroline=False,hoverformat=None)
fig.show()
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/scatterplot_symbol.png)

- Here is an example of Python code that I used to create a line chart with Spotify data:

```python
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
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/line_chart.png)

- Improved further by organizing the lines in the line chart and removed the category order for a clearer and more straightforward presentation of the data.

```python
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
```

![Image Alt](https://github.com/mayaranori/estudos_estatistica/blob/31e5b0bc5906962bf70664958b86db5c162b903b/python_basico/line_chart_without_categoryorder.png)
