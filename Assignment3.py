# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get
#  help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](
# https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 3 - More Pandas All questions are weighted the same in this assignment. This assignment requires more
# individual learning then the last one did - you are encouraged to check out the [pandas documentation](
# http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet,
# or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of
# course, the discussion forums are open for interaction with your peers and the course staff.

# ### Question 1 (20%) Load the energy data from the file `Energy Indicators.xls`, which is a list of indicators of [
# energy supply and renewable electricity production](Energy%20Indicators.xls) from the [United Nations](
# http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013,
# and should be put into a DataFrame with the variable name of **energy**.
# 
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the
# footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of
# them, and you should change the column labels so that the columns are:
# 
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]`
# 
# Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have
#  missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
# 
# Rename the following list of countries (for use in later questions):
# 
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# 
# There are also several countries with parenthesis in their name. Be sure to remove these, e.g. `'Bolivia (
# Plurinational State of)'` should be `'Bolivia'`.
# 
# <br>
# 
# Next, load the GDP data from the file `world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015
# from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**. # ---
#
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get
#  help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](
# https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
#
# ---

# # Assignment 3 - More Pandas All questions are weighted the same in this assignment. This assignment requires more
# individual learning then the last one did - you are encouraged to check out the [pandas documentation](
# http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet,
# or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of
# course, the discussion forums are open for interaction with your peers and the course staff.

# ### Question 1 (20%) Load the energy data from the file `Energy Indicators.xls`, which is a list of indicators of [
# energy supply and renewable electricity production](Energy%20Indicators.xls) from the [United Nations](
# http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013,
# and should be put into a DataFrame with the variable name of **energy**.
#
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the
# footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of
# them, and you should change the column labels so that the columns are:
#
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]`
#
# Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have
#  missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
#
# Rename the following list of countries (for use in later questions):
#
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
#
# There are also several countries with parenthesis in their name. Be sure to remove these, e.g. `'Bolivia (
# Plurinational State of)'` should be `'Bolivia'`.
#
# <br>
#
# Next, load the GDP data from the file `world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015
# from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**.
#
# Make sure to skip the header, and rename the following list of countries:
# 
# ```"Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```
# 
# <br>
# 
# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](
# http://www.scimagojr.com/countryrank.php?category=2102) from the file `scimagojr-3.xlsx`, which ranks countries
# based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
# 

##### More mess that needs cleaning
# foot notes
# 'Denmark', # 'Denmark5',
# 'Greenland', # 'Greenland7',
# 'Indonesia', # 'Indonesia8',
# 'Kuwait', # 'Kuwait11',
# 'Netherlands', # 'Netherlands Antilles' # 'Netherlands12',
# 'Portugal', # 'Portugal13',
# 'Saudi Arabia', # 'Saudi Arabia14',
# 'Serbia', # 'Serbia15',
# 'Switzerland', 'Switzerland17',
# 'Ukraine', 'Ukraine18',

# fix this? 'China, Macao Special Administrative Region4', ?
# fix this to south korea? 'Korea, Dem. People’s Rep.'
# 'Kyrgyz Republic', # 'Kyrgyzstan',
# 'Lao PDR', # "Lao People's Democratic Republic",
# 'Macao', # 'Macao SAR, China',
# 'Macedonia', # 'Macedonia, FYR',
# 'Micronesia', # 'Micronesia, Fed. Sts.',
# 'Slovak Republic', # 'Slovakia',
# 'Venezuela', 'Venezuela, RB',
# 'Congo', # 'Congo, Dem. Rep.', # 'Congo, Rep.',
# 'Egypt', # 'Egypt, Arab Rep.',
# 'Viet Nam', 'Vietnam',
# 'Yemen', 'Yemen, Rep.'
# 'Dominica', # 'Dominican Republic',
# 'Bahamas', # 'Bahamas, The',
# 'Gambia', # 'Gambia, The',


# special chars
# 'Curacao', # 'Curaçao',
# 'Haiti', # 'Haïti',
# 'Reunion', # 'Réunion',

# the quotes
# "Côte d'Ivoire", # 'Côte d’Ivoire',
# "Democratic People's Republic of Korea",
#####

import pandas as pd
import numpy as np
import re


def load_energy_data():
    # load the Energy Indicators data

    # missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
    # Rename the following list of countries (for use in later questions):
    # ```"Republic of Korea": "South Korea",
    # "United States of America": "United States",
    # "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    # "China, Hong Kong Special Administrative Region": "Hong Kong"```
    # remove text in parentheses `'Bolivia (Plurinational State of)'` should be `'Bolivia'`

    ######
    # exclude footer and header, and replace '...' with np.NaN
    # TODO: check if the NaN that read_excel uses is numpy's NaN
    energy = pd.read_excel('Energy Indicators.xls', skiprows=range(17), skipfooter=38, na_values='...')

    # drop the first two columns
    energy.drop(energy.columns[[0, 1]], axis=1, inplace=True)

    # rename columns
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

    # Convert `Energy Supply` to gigajoules; 1 PJ = 1000000 GJ
    energy['Energy Supply'] *= 1000000

    # rename countries
    korea_idx = energy[energy['Country'] == 'Republic of Korea'].index.values[0]
    energy.loc[korea_idx, 'Country'] = 'South Korea'
    us_idx = energy[energy['Country'] == 'United States of America20'].index.values[0]
    energy.loc[us_idx, 'Country'] = 'United States'
    uk_idx = energy[energy['Country'] == 'United Kingdom of Great Britain and Northern Ireland19'].index.values[0]
    energy.loc[uk_idx, 'Country'] = 'United Kingdom'
    hk_idx = energy[energy['Country'] == 'China, Hong Kong Special Administrative Region3'].index.values[0]
    energy.loc[hk_idx, 'Country'] = 'Hong Kong'
    iran_idx = energy[energy['Country'] == 'Iran (Islamic Republic of)'].index.values[0]
    energy.loc[iran_idx, 'Country'] = 'Iran'

    # Remove foot note numbers from country names
    tmp_idx = energy[energy['Country'] == 'Australia1'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Australia'
    tmp_idx = energy[energy['Country'] == 'China2'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'China'
    tmp_idx = energy[energy['Country'] == 'France6'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'France'
    tmp_idx = energy[energy['Country'] == 'Italy9'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Italy'
    tmp_idx = energy[energy['Country'] == 'Japan10'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Japan'
    tmp_idx = energy[energy['Country'] == 'Spain16'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Spain'
    # 'Denmark', # 'Denmark5',
    tmp_idx = energy[energy['Country'] == 'Denmark5'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Denmark'
    # 'Greenland', # 'Greenland7',
    tmp_idx = energy[energy['Country'] == 'Greenland7'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Greenland'
    # 'Indonesia', # 'Indonesia8',
    tmp_idx = energy[energy['Country'] == 'Indonesia8'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Indonesia'
    # 'Kuwait', # 'Kuwait11',
    tmp_idx = energy[energy['Country'] == 'Kuwait11'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Kuwait'
    # 'Netherlands', # 'Netherlands Antilles' # 'Netherlands12',
    tmp_idx = energy[energy['Country'] == 'Netherlands12'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Netherlands'
    # 'Portugal', # 'Portugal13',
    tmp_idx = energy[energy['Country'] == 'Portugal13'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Portugal'
    # 'Saudi Arabia', # 'Saudi Arabia14',
    tmp_idx = energy[energy['Country'] == 'Saudi Arabia14'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Saudi Arabia'
    # 'Serbia', # 'Serbia15',
    tmp_idx = energy[energy['Country'] == 'Serbia15'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Serbia'
    # 'Switzerland', 'Switzerland17',
    tmp_idx = energy[energy['Country'] == 'Switzerland17'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Switzerland'
    # 'Ukraine', 'Ukraine18',
    tmp_idx = energy[energy['Country'] == 'Ukraine18'].index.values[0]
    energy.loc[tmp_idx, 'Country'] = 'Ukraine'

    # remove text in parentheses in country names
    # generate a list of country names that has a '(" in its name
    pcn_list = energy[energy['Country'].str.contains("\(")].index.values.tolist()
    # generate a list of tuples (index_value, country_name_with_text_in_paran_removed)
    ctlist = [(cidx, (re.sub(r'\([^()]*\)', '', energy.loc[cidx, 'Country']).rstrip())) for cidx in pcn_list]
    # replace country names with parentheses with their names with text in paran removed
    for c in ctlist:
        energy.loc[c[0], 'Country'] = c[1].rstrip()
        # end for ctlist

    return energy
# end load_energy_data()


# GDP data
def load_GDP_data():
    # read in the data and skip the header (first 4 rows)
    GDP = pd.read_csv('world_bank.csv', skiprows=range(4))
    # rename countries
    # "Korea, Rep.": "South Korea", 
    korea_idx = GDP[GDP['Country Name'] == 'Korea, Rep.'].index.values[0]
    GDP.loc[korea_idx, 'Country Name'] = 'South Korea'
    # "Iran, Islamic Rep.": "Iran",
    iran_idx = GDP[GDP['Country Name'] == 'Iran, Islamic Rep.'].index.values[0]
    GDP.loc[iran_idx, 'Country Name'] = 'Iran'
    # "Hong Kong SAR, China": "Hong Kong"
    hk_idx = GDP[GDP['Country Name'] == 'Hong Kong SAR, China'].index.values[0]
    GDP.loc[hk_idx, 'Country Name'] = 'Hong Kong'

    return GDP
# end load_GDP_data()


# ScimEn data
def load_ScimEn_data():
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    # print(ScimEn.head())

    return ScimEn
# end load_ScimEn_data()


def validate_clean_up():
    GDP = load_GDP_data()
    energy = load_energy_data()
    ScimEn = load_ScimEn_data()
    gcn_s = set(GDP['Country Name'].tolist())
    ecn_s = set(energy['Country'].tolist())
    scn_s = set(ScimEn['Country'].tolist())
    eug = ecn_s.union(gcn_s)
    eugus = eug.union(scn_s)
    eing = ecn_s.intersection(gcn_s)
    eingins = eing.intersection(scn_s)
    print(len(eugus), len(eingins))
    return True
# end validate_clean_up()


# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use
# only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
#
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents',
# 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply',
# 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
# '2015'].
#
# *This function should return a DataFrame with 20 columns and 15 entries.*

# In[ ]:

def answer_one():
    # load all data
    energy = load_energy_data()
    GDP = load_GDP_data()
    ScimEn = load_ScimEn_data()

    sci_df = ScimEn.nsmallest(n=15, columns='Rank')
    sci_df.set_index(keys='Country', inplace=True)

    col_list = ['Country Name'] + [str(i) for i in range(2006, 2016)]
    gdp_df = GDP[col_list]
    gdp_df.set_index(keys='Country Name', inplace=True)

    energy_df = energy.set_index(keys='Country')

    # inner merge
    sci_energy_df = pd.merge(sci_df, energy_df, how='inner', left_index=True, right_index=True)
    sci_energy_gdp_df = pd.merge(sci_energy_df, gdp_df, how='inner', left_index=True, right_index=True)

    # print(sci_energy_gdp_df.head(20))
    return sci_energy_gdp_df


# ### Question 2 (6.6%) The previous question joined three datasets then reduced this to just the top 15 entries.
# When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# 
# *This function should return a single number.*

# In[1]:

# get_ipython().run_cell_magic('HTML', '', '<svg width="800" height="300">\n  <circle cx="150" cy="180" r="80"
# fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80"
# fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80"
# fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150"
# stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text  x="300" y="165"
# font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


# In[ ]:


def answer_two():
    # load all data
    GDP = load_GDP_data()
    energy = load_energy_data()
    ScimEn = load_ScimEn_data()

    sci_df = ScimEn.set_index(keys='Country')
    gdp_df = GDP.set_index(keys='Country Name')
    energy_df = energy.set_index(keys='Country')

    # outer merge
    outer_sci_energy_df = pd.merge(sci_df, energy_df, how='outer', left_index=True, right_index=True)
    outer_sci_energy_gdp_df = pd.merge(outer_sci_energy_df, gdp_df, how='outer', left_index=True, right_index=True)
    outer_join_count = outer_sci_energy_gdp_df.shape[0]

    # inner merge
    sci_energy_df = pd.merge(sci_df, energy_df, how='inner', left_index=True, right_index=True)
    sci_energy_gdp_df = pd.merge(sci_energy_df, gdp_df, how='inner', left_index=True, right_index=True)
    inner_join_count = sci_energy_gdp_df.shape[0]
    # old answer 176, correct answer = 156? # inner_join_count = 162?
    # print("Using merge/joins:", "Union: ", outer_join_count, "Intersection: ", inner_join_count)

    # GDP = load_GDP_data()
    # energy = load_energy_data()
    # ScimEn = load_ScimEn_data()
    # gcn_s = set(GDP['Country Name'].tolist())
    # ecn_s = set(energy['Country'].tolist())
    # scn_s = set(ScimEn['Country'].tolist())
    # eug = ecn_s.union(gcn_s)
    # eugus = eug.union(scn_s)
    # eing = ecn_s.intersection(gcn_s)
    # eingins = eing.intersection(scn_s)
    # print("Using set ops:", "Union: ", len(eugus), "Intersection: ", len(eingins))

    return outer_join_count - inner_join_count


# ### Question 3 (6.6%)
# What are the top 15 countries for average GDP over the last 10 years?
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending
# order.*

# In[ ]:

def answer_three():
    Top15 = answer_one()
    gdp_df = Top15[[str(i) for i in range(2006, 2016)]]
    gg = gdp_df.apply(np.average, axis=1)
    ggsorted = gg.sort_values(na_position='last', ascending=False)
    return ggsorted

# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[ ]:

def answer_four():
    # get the top15 sorted by average GDP
    top15gdp = answer_three()
    # get the sixth country in the list
    sixth = top15gdp.index.values[5]
    Top15 = answer_one()
    sixth_gdp = Top15.loc[sixth][[str(i) for i in range(2006, 2016)]]
    # apparently the answer is the difference between the GDP on 2015 and 2006!
    # print(sixth_gdp.max(), sixth_gdp.min())
    # return sixth_gdp.max() - sixth_gdp.min()
    return sixth_gdp['2015'] - sixth_gdp['2006']


# ### Question 5 (6.6%)
# What is the mean energy supply per capita?
# 
# *This function should return a single number.*

# In[ ]:

def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()


# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[ ]:

def answer_six():
    Top15 = answer_one()
    mpc = Top15['% Renewable'].nlargest(n=1)
    res = (mpc.index[0], mpc.values[0])
    return res


# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[ ]:

def answer_seven():
    Top15 = answer_one()
    cratio = Top15['Self-citations'] / Top15['Citations']
    crtop = cratio.nlargest(n=1)
    res = (crtop.index[0], crtop.values[0])
    return res


# ### Question 8 (6.6%)
# 
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return a single string value.*

# In[ ]:

def answer_eight():
    Top15 = answer_one()
    # espc = es / pop
    # pop = es / espc
    pop = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    pps = pop.sort_values(ascending=False)
    return pps.index[2]

# ### Question 9 Create a column that estimates the number of citable documents per person. What is the correlation
# between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method,
# (Pearson's correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs.
# Citable docs per Capita)*

# In[ ]:

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    return Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'], method='pearson')

# In[ ]:

def plot9():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')

    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# In[ ]:

# plot9() # Be sure to comment out plot9() before submitting the assignment!


# ### Question 10 (6.6%) Create a new column with a 1 if the country's % Renewable value is at or above the median
# for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order
# of rank.*

# In[ ]:

def answer_ten():
    Top15 = answer_one()
    Top15.sort_values(by='Rank', inplace=True)
    renew_median = Top15['% Renewable'].median()
    Top15['new01col'] = Top15['% Renewable'].apply(lambda x: 1 if x >= renew_median else 0)
    return Top15['new01col']


# ### Question 11 (6.6%) Use the following dictionary to group the Countries by Continent, then create a dateframe
# that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation
#  for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe',
# 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[ ]:

def answer_eleven():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable
# bins. How many countries are in each of these groups?
# 
# *This function should return a Series with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not
# include groups with no countries.*

# In[ ]:

def answer_twelve():
    Top15 = answer_one()
    return "ANSWER"


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas).
# Use all significant digits (do not round the results).
# 
# e.g. 12345678.90 -> 12,345,678.90
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population
# estimate string.*

# In[ ]:

def answer_thirteen():
    Top15 = answer_one()
    return "ANSWER"


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[ ]:

def plot_optional():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter',
                    c=['#e41a1c', '#377eb8', '#e41a1c', '#4daf4a', '#4daf4a', '#377eb8', '#4daf4a', '#e41a1c',
                       '#4daf4a', '#e41a1c', '#4daf4a', '#4daf4a', '#e41a1c', '#dede00', '#ff7f00'],
                    xticks=range(1, 16), s=6 * Top15['2014'] / 10 ** 10, alpha=.75, figsize=[16, 6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print(
        "This is an example of a visualization that can be created to help understand the data. This is a bubble "
        "chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, "
        "and the color corresponds to the continent.")

# In[ ]:

# plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!
