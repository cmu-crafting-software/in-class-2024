import pandas as pd

first = pd.read_csv('data/gapminder_all.csv', index_col='country')
second = first[first['continent'] == 'Americas']
third = second.drop('Puerto Rico')
fourth = third.drop('continent', axis = 1)
fourth.to_csv('result.csv')

europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(europe_gdp_data.iloc[0:2, 0:2])
print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])

# 4a GDP per capita for all countries in 1982.
data = pd.read_csv('data/gapminder_all.csv', index_col='country')
print(data['gdpPercap_1982'])
# 4b GDP per capita for Denmark for all years.
print(data.loc['Denmark','gdpPercap_1952':'gdpPercap_2007'])
# 4c GDP per capita for all countries for years after 1985.
print(data.loc['country','gdpPercap_1985':])

