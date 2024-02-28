import pandas as pd

data_all = pd.read_csv('data/gapminder_all.csv', index_col='country')


#1
gdpPercap_Serbia_2007 = data_all['gdpPercap_2007']['Serbia']
print('Per capita GDP of Serbia in 2007: ',gdpPercap_Serbia_2007)


#3
europe_gdp_data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(europe_gdp_data.iloc[0:2, 0:2])
print(europe_gdp_data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])

#4
gdpPercap_allcountries_1982 = data_all.loc[:,'gdpPercap_1982']
print(gdpPercap_allcountries_1982)

gdpPercap_Denmark_allYears = data_all.loc['Denmark','gdpPercap_1952':'gdpPercap_2007']
print(gdpPercap_Denmark_allYears)

gdpPercap_allcountries_after1985 = data_all.loc[:,'gdpPercap_1987':]
print(gdpPercap_allcountries_after1985)