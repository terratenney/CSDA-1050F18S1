
# csda 1050

### Sprint
Describe what is in here. 

After evaluating the data by importing it into Python and doing some data clean up we realized the housing data have too many missing values and won’t be instumental for our analysis. The only datasets that seem to be functional is the Renter Household, Monthly Payments and the Annual Income after Tax datasets. We have decided that we have to change our research question to focus only on rental properties and exclude the house price data. Our new research question is to determine the most cost effective price for renter’s base on their household income.

Describe what is needed to be done to run it. 

We have used Python to do our analysis to run the codes and see thout puts you will have to have Python on you desktop.
We would ike to take some more time to be more decriptive with our findings
Our next step is to complete the data clean up process to prepare the data sets for modelling.

#### Python Codes 
#### Below are the codes that we have used so far to get a better understanding of our 3 datasets


```python
# Loading packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
%matplotlib inline
```


```python
# Importing the Renter Household data
mydata= pd.read_csv(r"C:\\Users\\susie\\Documents\\Data Science\\Capstone data\\RenterHouseholds.csv"
                   ,encoding="latin")


```


```python
# Checking the data contents
mydata.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Household Income Range</th>
      <th>Quartile</th>
      <th>Average Income</th>
      <th>Studio</th>
      <th>1-Bed</th>
      <th>2-Bed</th>
      <th>3-Bed</th>
      <th>4-Bed</th>
      <th>All Units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alberta</td>
      <td>0 - 33,002</td>
      <td>Q1</td>
      <td>19941.0</td>
      <td>2655.00</td>
      <td>44025.0</td>
      <td>33850.0</td>
      <td>15685.0</td>
      <td>3835.0</td>
      <td>101570.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alberta</td>
      <td>33,002 - 60,357</td>
      <td>Q2</td>
      <td>46487.0</td>
      <td>1160.00</td>
      <td>28735.0</td>
      <td>40325.0</td>
      <td>22640.0</td>
      <td>6205.0</td>
      <td>101500.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alberta</td>
      <td>60,357 - 96,607</td>
      <td>Q3</td>
      <td>76896.0</td>
      <td>525.00</td>
      <td>20340.0</td>
      <td>40355.0</td>
      <td>28120.0</td>
      <td>8805.0</td>
      <td>101630.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alberta</td>
      <td>96607.00</td>
      <td>Q4</td>
      <td>153437.0</td>
      <td>200.00</td>
      <td>10820.0</td>
      <td>33620.0</td>
      <td>34055.0</td>
      <td>15250.0</td>
      <td>101515.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>British Columbia</td>
      <td>0 - 23,378</td>
      <td>Q1</td>
      <td>13557.0</td>
      <td>10805.00</td>
      <td>79850.0</td>
      <td>41400.0</td>
      <td>11365.0</td>
      <td>3060.0</td>
      <td>147935.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Checking the number of rows and columns
mydata.shape
```




    (57, 10)




```python
# Looking at the dimention of the data
mydata.ndim
```




    2




```python
# Checking the data types
mydata.dtypes
```




    Name                       object
    Household Income Range     object
    Quartile                   object
    Average Income            float64
    Studio                     object
    1-Bed                     float64
    2-Bed                     float64
    3-Bed                     float64
    4-Bed                     float64
    All Units                 float64
    dtype: object




```python
# Describing the entire DataFrame it only shows results for columns with numeric datatypes.
mydata.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Income</th>
      <th>1-Bed</th>
      <th>2-Bed</th>
      <th>3-Bed</th>
      <th>4-Bed</th>
      <th>All Units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>57.000000</td>
      <td>57.000000</td>
      <td>57.000000</td>
      <td>57.000000</td>
      <td>57.000000</td>
      <td>57.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>57825.526316</td>
      <td>27780.877193</td>
      <td>31234.122807</td>
      <td>15417.807018</td>
      <td>3802.807018</td>
      <td>81179.912281</td>
    </tr>
    <tr>
      <th>std</th>
      <td>45915.811291</td>
      <td>48052.684509</td>
      <td>48436.754235</td>
      <td>25223.236878</td>
      <td>6544.161317</td>
      <td>123318.547515</td>
    </tr>
    <tr>
      <th>min</th>
      <td>12730.000000</td>
      <td>100.000000</td>
      <td>375.000000</td>
      <td>160.000000</td>
      <td>25.000000</td>
      <td>1245.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>26489.000000</td>
      <td>725.000000</td>
      <td>2090.000000</td>
      <td>840.000000</td>
      <td>245.000000</td>
      <td>4365.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>46332.000000</td>
      <td>5755.000000</td>
      <td>9630.000000</td>
      <td>4310.000000</td>
      <td>1055.000000</td>
      <td>26840.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>83058.000000</td>
      <td>28735.000000</td>
      <td>40325.000000</td>
      <td>20575.000000</td>
      <td>3835.000000</td>
      <td>101570.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>205724.000000</td>
      <td>216740.000000</td>
      <td>162155.000000</td>
      <td>107270.000000</td>
      <td>35875.000000</td>
      <td>388150.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Looking at the columns 
mydata.columns
```




    Index(['Name', 'Household Income Range', 'Quartile', 'Average Income',
           'Studio', '1-Bed', '2-Bed', '3-Bed', '4-Bed', 'All Units'],
          dtype='object')




```python
# Droping 'Household Income Range', 'Quartile' columns.
mydata.drop(['Household Income Range', 'Quartile'], axis=1)
```


```python
# Finding the correclation in the data
mydata.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Income</th>
      <th>1-Bed</th>
      <th>2-Bed</th>
      <th>3-Bed</th>
      <th>4-Bed</th>
      <th>All Units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Average Income</th>
      <td>1.000000</td>
      <td>-0.227739</td>
      <td>-0.057341</td>
      <td>0.105870</td>
      <td>0.230439</td>
      <td>-0.079781</td>
    </tr>
    <tr>
      <th>1-Bed</th>
      <td>-0.227739</td>
      <td>1.000000</td>
      <td>0.844631</td>
      <td>0.647515</td>
      <td>0.508548</td>
      <td>0.914716</td>
    </tr>
    <tr>
      <th>2-Bed</th>
      <td>-0.057341</td>
      <td>0.844631</td>
      <td>1.000000</td>
      <td>0.930808</td>
      <td>0.773809</td>
      <td>0.982815</td>
    </tr>
    <tr>
      <th>3-Bed</th>
      <td>0.105870</td>
      <td>0.647515</td>
      <td>0.930808</td>
      <td>1.000000</td>
      <td>0.928389</td>
      <td>0.898050</td>
    </tr>
    <tr>
      <th>4-Bed</th>
      <td>0.230439</td>
      <td>0.508548</td>
      <td>0.773809</td>
      <td>0.928389</td>
      <td>1.000000</td>
      <td>0.771047</td>
    </tr>
    <tr>
      <th>All Units</th>
      <td>-0.079781</td>
      <td>0.914716</td>
      <td>0.982815</td>
      <td>0.898050</td>
      <td>0.771047</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plotting the correlation graph
f,ax = plt.subplots(figsize=(10,10))
sns.heatmap(mydata.corr(), annot = True,linewidths=.4, fmt='.1f', ax=ax)
plt.show()
```


![png](output_10_0.png)



```python
#histogram of the average income
sns.distplot(mydata['Average Income']);
```


![png](output_11_0.png)



```python
# Scatter Plot of the average income, 1 bedroom and 2 ped room
# x = Average Income, y = Bedroom
mydata.plot(kind='scatter',x = 'Average Income', y = '1-Bed', alpha=0.5, color='b')
plt.xlabel('Average Income')
plt.ylabel('1-Bed')
plt.title('Average Income or 1 bedroom')
mydata.plot(kind='scatter',x = 'Average Income', y = '2-Bed', alpha=0.5, color='r')
plt.xlabel('Average Income')
plt.ylabel('2-Bed')
plt.title('Average Income or 1 Bedroom')
```




    Text(0.5, 1.0, 'Average Income or 1 Bedroom')




![png](output_12_1.png)



![png](output_12_2.png)



```python
# let's look at the average income
Income_mean=np.mean(mydata['Average Income'])
print("Income_mean:",Income_mean)
# let's look at the average total 4 bedrooms above grade
room_mean=np.mean(mydata['4-Bed'])
print("room_mean:",room_mean)
```

    Income_mean: 57825.52631578947
    room_mean: 3802.8070175438597
    


```python
# Now, let's find income under the average price and the number of rooms above the average.
# Filtering pandas with logical_and
filt1=mydata[np.logical_and(mydata['Average Income']<Income_mean,mydata['2-Bed']>room_mean)]
filt1.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Household Income Range</th>
      <th>Quartile</th>
      <th>Average Income</th>
      <th>Studio</th>
      <th>1-Bed</th>
      <th>2-Bed</th>
      <th>3-Bed</th>
      <th>4-Bed</th>
      <th>All Units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alberta</td>
      <td>0 - 33,002</td>
      <td>Q1</td>
      <td>19941.0</td>
      <td>2655.00</td>
      <td>44025.0</td>
      <td>33850.0</td>
      <td>15685.0</td>
      <td>3835.0</td>
      <td>101570.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alberta</td>
      <td>33,002 - 60,357</td>
      <td>Q2</td>
      <td>46487.0</td>
      <td>1160.00</td>
      <td>28735.0</td>
      <td>40325.0</td>
      <td>22640.0</td>
      <td>6205.0</td>
      <td>101500.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>British Columbia</td>
      <td>0 - 23,378</td>
      <td>Q1</td>
      <td>13557.0</td>
      <td>10805.00</td>
      <td>79850.0</td>
      <td>41400.0</td>
      <td>11365.0</td>
      <td>3060.0</td>
      <td>147935.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>British Columbia</td>
      <td>23,378 - 45,979</td>
      <td>Q2</td>
      <td>34352.0</td>
      <td>5025.00</td>
      <td>61155.0</td>
      <td>54130.0</td>
      <td>20575.0</td>
      <td>4815.0</td>
      <td>147855.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>British Columbia</td>
      <td>23,378 - 45,979</td>
      <td>Q2</td>
      <td>34352.0</td>
      <td>5025.00</td>
      <td>61155.0</td>
      <td>54130.0</td>
      <td>20575.0</td>
      <td>4815.0</td>
      <td>147855.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# let’s filter numeric variables
numerical = [
  'Average Income','Studio','1-Bed','2-Bed','3-Bed','4-Bed','All Units'
]
```


```python
# Histograms of the nueric variables
mydata[numerical].hist(bins=15, figsize=(15, 6), layout=(2, 4));
```


![png](output_16_0.png)



```python
# Check the index values
mydata.index.values
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
           34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           51, 52, 53, 54, 55, 56], dtype=int64)




```python
# Loading the income after tax dataset
income= pd.read_csv(r"C:\\Users\\susie\\Documents\\Data Science\\Capstone data\\median-income-after-tax-renters.csv"
                   ,encoding="latin1")
```


```python
# Viewing the data contents
income.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Canada</th>
      <th>2006</th>
      <th>2007</th>
      <th>2008</th>
      <th>2009</th>
      <th>2010</th>
      <th>2011</th>
      <th>2012</th>
      <th>2013</th>
      <th>2014</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>\nProvinces</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Newfoundland and Labrador</td>
      <td>26300.0</td>
      <td>28800.0</td>
      <td>31300.0</td>
      <td>31900.0</td>
      <td>32500.0</td>
      <td>37200.0</td>
      <td>36000.0</td>
      <td>38600.0</td>
      <td>38100.0</td>
      <td>36300.0</td>
      <td>35000.0</td>
      <td>34000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Prince Edward Island</td>
      <td>33400.0</td>
      <td>33200.0</td>
      <td>33500.0</td>
      <td>36800.0</td>
      <td>37700.0</td>
      <td>32000.0</td>
      <td>33500.0</td>
      <td>34500.0</td>
      <td>34300.0</td>
      <td>34500.0</td>
      <td>38900.0</td>
      <td>37300.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Nova Scotia</td>
      <td>33200.0</td>
      <td>34600.0</td>
      <td>33000.0</td>
      <td>32800.0</td>
      <td>34000.0</td>
      <td>34800.0</td>
      <td>35000.0</td>
      <td>37100.0</td>
      <td>35800.0</td>
      <td>36100.0</td>
      <td>35300.0</td>
      <td>36700.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New Brunswick</td>
      <td>31200.0</td>
      <td>31500.0</td>
      <td>31900.0</td>
      <td>32900.0</td>
      <td>34200.0</td>
      <td>31800.0</td>
      <td>31100.0</td>
      <td>32100.0</td>
      <td>32800.0</td>
      <td>29100.0</td>
      <td>34200.0</td>
      <td>33000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Checking the shape of the data
income.shape
```




    (41, 13)




```python
# Checking the data types
income.dtypes
```




    Canada     object
    2006      float64
    2007      float64
    2008      float64
    2009      float64
    2010      float64
    2011      float64
    2012      float64
    2013      float64
    2014      float64
    2015      float64
    2016      float64
    2017      float64
    dtype: object




```python
# Describing the entire DataFrame it only shows results for columns with numeric datatypes.
income.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2006</th>
      <th>2007</th>
      <th>2008</th>
      <th>2009</th>
      <th>2010</th>
      <th>2011</th>
      <th>2012</th>
      <th>2013</th>
      <th>2014</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>35174.358974</td>
      <td>36623.076923</td>
      <td>37438.461538</td>
      <td>37646.153846</td>
      <td>37402.564103</td>
      <td>37887.179487</td>
      <td>38453.846154</td>
      <td>38941.025641</td>
      <td>39792.307692</td>
      <td>39192.307692</td>
      <td>40805.128205</td>
      <td>40307.692308</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5704.048329</td>
      <td>5720.483120</td>
      <td>6534.387395</td>
      <td>6462.924471</td>
      <td>6095.144192</td>
      <td>5863.050198</td>
      <td>7332.510382</td>
      <td>6661.741433</td>
      <td>8302.865219</td>
      <td>7452.000248</td>
      <td>7462.148298</td>
      <td>7908.236367</td>
    </tr>
    <tr>
      <th>min</th>
      <td>23600.000000</td>
      <td>26900.000000</td>
      <td>30300.000000</td>
      <td>27400.000000</td>
      <td>28400.000000</td>
      <td>26000.000000</td>
      <td>26300.000000</td>
      <td>26200.000000</td>
      <td>23200.000000</td>
      <td>24500.000000</td>
      <td>29400.000000</td>
      <td>27000.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>31050.000000</td>
      <td>32150.000000</td>
      <td>33150.000000</td>
      <td>33400.000000</td>
      <td>33750.000000</td>
      <td>34250.000000</td>
      <td>33600.000000</td>
      <td>34800.000000</td>
      <td>34450.000000</td>
      <td>34800.000000</td>
      <td>34650.000000</td>
      <td>35350.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>34300.000000</td>
      <td>35400.000000</td>
      <td>35300.000000</td>
      <td>35700.000000</td>
      <td>36000.000000</td>
      <td>37200.000000</td>
      <td>37500.000000</td>
      <td>37300.000000</td>
      <td>39100.000000</td>
      <td>38400.000000</td>
      <td>40100.000000</td>
      <td>38500.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>38300.000000</td>
      <td>39100.000000</td>
      <td>39500.000000</td>
      <td>39800.000000</td>
      <td>38150.000000</td>
      <td>40350.000000</td>
      <td>41300.000000</td>
      <td>42450.000000</td>
      <td>43450.000000</td>
      <td>43000.000000</td>
      <td>43700.000000</td>
      <td>44250.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>46900.000000</td>
      <td>52500.000000</td>
      <td>59900.000000</td>
      <td>54600.000000</td>
      <td>55900.000000</td>
      <td>51000.000000</td>
      <td>61100.000000</td>
      <td>57200.000000</td>
      <td>62000.000000</td>
      <td>57200.000000</td>
      <td>57700.000000</td>
      <td>59700.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Checking the data index values
income.index.values
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
           34, 35, 36, 37, 38, 39, 40], dtype=int64)




```python
# Checking the column names
income.columns
```




    Index(['Canada', '2006', '2007', '2008', '2009', '2010', '2011', '2012',
           '2013', '2014', '2015', '2016', '2017'],
          dtype='object')




```python
# Checking the correlation of the data
income.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2006</th>
      <th>2007</th>
      <th>2008</th>
      <th>2009</th>
      <th>2010</th>
      <th>2011</th>
      <th>2012</th>
      <th>2013</th>
      <th>2014</th>
      <th>2015</th>
      <th>2016</th>
      <th>2017</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2006</th>
      <td>1.000000</td>
      <td>0.876773</td>
      <td>0.677358</td>
      <td>0.717369</td>
      <td>0.609049</td>
      <td>0.526359</td>
      <td>0.646890</td>
      <td>0.595413</td>
      <td>0.520911</td>
      <td>0.530322</td>
      <td>0.644431</td>
      <td>0.699813</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>0.876773</td>
      <td>1.000000</td>
      <td>0.857235</td>
      <td>0.816989</td>
      <td>0.804540</td>
      <td>0.721547</td>
      <td>0.710484</td>
      <td>0.693834</td>
      <td>0.663112</td>
      <td>0.655241</td>
      <td>0.780259</td>
      <td>0.824914</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>0.677358</td>
      <td>0.857235</td>
      <td>1.000000</td>
      <td>0.833432</td>
      <td>0.855253</td>
      <td>0.806039</td>
      <td>0.764217</td>
      <td>0.738080</td>
      <td>0.727629</td>
      <td>0.743761</td>
      <td>0.796789</td>
      <td>0.756176</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>0.717369</td>
      <td>0.816989</td>
      <td>0.833432</td>
      <td>1.000000</td>
      <td>0.813959</td>
      <td>0.831747</td>
      <td>0.638535</td>
      <td>0.638719</td>
      <td>0.694942</td>
      <td>0.643793</td>
      <td>0.833089</td>
      <td>0.738159</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>0.609049</td>
      <td>0.804540</td>
      <td>0.855253</td>
      <td>0.813959</td>
      <td>1.000000</td>
      <td>0.822027</td>
      <td>0.803990</td>
      <td>0.832260</td>
      <td>0.830172</td>
      <td>0.813906</td>
      <td>0.847016</td>
      <td>0.851348</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>0.526359</td>
      <td>0.721547</td>
      <td>0.806039</td>
      <td>0.831747</td>
      <td>0.822027</td>
      <td>1.000000</td>
      <td>0.711404</td>
      <td>0.711410</td>
      <td>0.764419</td>
      <td>0.722209</td>
      <td>0.803220</td>
      <td>0.730914</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>0.646890</td>
      <td>0.710484</td>
      <td>0.764217</td>
      <td>0.638535</td>
      <td>0.803990</td>
      <td>0.711404</td>
      <td>1.000000</td>
      <td>0.827360</td>
      <td>0.818370</td>
      <td>0.858074</td>
      <td>0.730558</td>
      <td>0.808860</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>0.595413</td>
      <td>0.693834</td>
      <td>0.738080</td>
      <td>0.638719</td>
      <td>0.832260</td>
      <td>0.711410</td>
      <td>0.827360</td>
      <td>1.000000</td>
      <td>0.885378</td>
      <td>0.867326</td>
      <td>0.732176</td>
      <td>0.800927</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>0.520911</td>
      <td>0.663112</td>
      <td>0.727629</td>
      <td>0.694942</td>
      <td>0.830172</td>
      <td>0.764419</td>
      <td>0.818370</td>
      <td>0.885378</td>
      <td>1.000000</td>
      <td>0.886442</td>
      <td>0.771017</td>
      <td>0.773988</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>0.530322</td>
      <td>0.655241</td>
      <td>0.743761</td>
      <td>0.643793</td>
      <td>0.813906</td>
      <td>0.722209</td>
      <td>0.858074</td>
      <td>0.867326</td>
      <td>0.886442</td>
      <td>1.000000</td>
      <td>0.797639</td>
      <td>0.868127</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>0.644431</td>
      <td>0.780259</td>
      <td>0.796789</td>
      <td>0.833089</td>
      <td>0.847016</td>
      <td>0.803220</td>
      <td>0.730558</td>
      <td>0.732176</td>
      <td>0.771017</td>
      <td>0.797639</td>
      <td>1.000000</td>
      <td>0.833017</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>0.699813</td>
      <td>0.824914</td>
      <td>0.756176</td>
      <td>0.738159</td>
      <td>0.851348</td>
      <td>0.730914</td>
      <td>0.808860</td>
      <td>0.800927</td>
      <td>0.773988</td>
      <td>0.868127</td>
      <td>0.833017</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plotting the correlation for the income data 
f,ax = plt.subplots(figsize=(10,10))
sns.heatmap(income.corr(), annot = True,linewidths=.4, fmt='.1f', ax=ax)
plt.show()
```


![png](output_26_0.png)



```python
# Plotting a scotter plot for income dataset with the 2006 and Canada column
sns.scatterplot(x=income['2006'], y=income['Canada']);
```


![png](output_27_0.png)



```python
# Loading the monthly debt payments
pmt= pd.read_csv(r"C:\\Users\\susie\\Documents\\Data Science\\Capstone data\\average-monthly-payment-2017.csv"
                   ,encoding="latin1")
```


```python
# Checking the data contents
pmt.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Geography</th>
      <th>Mortgage</th>
      <th>HELOC</th>
      <th>Line Of Credit</th>
      <th>Auto Loan</th>
      <th>Credit Card</th>
      <th>All Other Credit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Canada</td>
      <td>1230.86</td>
      <td>170.26</td>
      <td>63.59</td>
      <td>470.02</td>
      <td>46.42</td>
      <td>235.83</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Large</td>
      <td>1437.58</td>
      <td>183.80</td>
      <td>60.37</td>
      <td>481.14</td>
      <td>42.89</td>
      <td>207.58</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Calgary</td>
      <td>1485.66</td>
      <td>194.04</td>
      <td>78.53</td>
      <td>515.22</td>
      <td>46.08</td>
      <td>231.01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Edmonton</td>
      <td>1420.65</td>
      <td>194.07</td>
      <td>86.87</td>
      <td>542.78</td>
      <td>48.95</td>
      <td>264.47</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Montréal</td>
      <td>1050.52</td>
      <td>163.30</td>
      <td>42.23</td>
      <td>433.70</td>
      <td>59.40</td>
      <td>170.05</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Checking the shape of the data
pmt.shape
```




    (79, 7)




```python
# Looking at the data types
pmt.dtypes
```




    Geography            object
    Mortgage            float64
    HELOC               float64
    Line Of Credit      float64
    Auto Loan            object
    Credit Card         float64
    All Other Credit    float64
    dtype: object




```python
# Describing the entire DataFrame it only shows results for columns with numeric datatypes.
pmt.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mortgage</th>
      <th>HELOC</th>
      <th>Line Of Credit</th>
      <th>Credit Card</th>
      <th>All Other Credit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
      <td>39.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1166.459231</td>
      <td>159.471282</td>
      <td>67.649744</td>
      <td>46.903846</td>
      <td>235.112051</td>
    </tr>
    <tr>
      <th>std</th>
      <td>246.685764</td>
      <td>23.818590</td>
      <td>21.614966</td>
      <td>10.018198</td>
      <td>35.973665</td>
    </tr>
    <tr>
      <th>min</th>
      <td>685.010000</td>
      <td>70.660000</td>
      <td>17.180000</td>
      <td>33.590000</td>
      <td>168.260000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1018.750000</td>
      <td>149.755000</td>
      <td>61.025000</td>
      <td>39.615000</td>
      <td>212.295000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1145.400000</td>
      <td>158.650000</td>
      <td>67.830000</td>
      <td>44.190000</td>
      <td>231.240000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1322.140000</td>
      <td>172.615000</td>
      <td>79.410000</td>
      <td>51.325000</td>
      <td>258.760000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1772.200000</td>
      <td>199.410000</td>
      <td>109.430000</td>
      <td>70.400000</td>
      <td>312.780000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The list of coloumns in the monthly payment dataset
pmt.columns
```




    Index(['Geography', 'Mortgage', 'HELOC', 'Line Of Credit', 'Auto Loan',
           'Credit Card', 'All Other Credit'],
          dtype='object')




```python
# Dropping the not availables
pmt.dropna()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Geography</th>
      <th>Mortgage</th>
      <th>HELOC</th>
      <th>Line Of Credit</th>
      <th>Auto Loan</th>
      <th>Credit Card</th>
      <th>All Other Credit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Canada</td>
      <td>1230.86</td>
      <td>170.26</td>
      <td>63.59</td>
      <td>470.02</td>
      <td>46.42</td>
      <td>235.83</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Large</td>
      <td>1437.58</td>
      <td>183.80</td>
      <td>60.37</td>
      <td>481.14</td>
      <td>42.89</td>
      <td>207.58</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Calgary</td>
      <td>1485.66</td>
      <td>194.04</td>
      <td>78.53</td>
      <td>515.22</td>
      <td>46.08</td>
      <td>231.01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Edmonton</td>
      <td>1420.65</td>
      <td>194.07</td>
      <td>86.87</td>
      <td>542.78</td>
      <td>48.95</td>
      <td>264.47</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Montréal</td>
      <td>1050.52</td>
      <td>163.30</td>
      <td>42.23</td>
      <td>433.70</td>
      <td>59.40</td>
      <td>170.05</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Ottawa-Gatineau</td>
      <td>1198.22</td>
      <td>151.92</td>
      <td>65.76</td>
      <td>454.69</td>
      <td>45.11</td>
      <td>213.12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Toronto</td>
      <td>1635.25</td>
      <td>188.74</td>
      <td>66.59</td>
      <td>489.38</td>
      <td>35.21</td>
      <td>204.29</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Vancouver</td>
      <td>1772.20</td>
      <td>199.41</td>
      <td>49.70</td>
      <td></td>
      <td>33.59</td>
      <td>223.11</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Medium</td>
      <td>1145.40</td>
      <td>151.85</td>
      <td>63.98</td>
      <td>449.67</td>
      <td>44.19</td>
      <td>219.81</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Halifax</td>
      <td>1099.44</td>
      <td>172.65</td>
      <td>95.68</td>
      <td>437.57</td>
      <td>49.41</td>
      <td>240.42</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Hamilton</td>
      <td>1328.58</td>
      <td>158.65</td>
      <td>68.13</td>
      <td>466.18</td>
      <td>38.22</td>
      <td>204.14</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Kitchener-Cambridge-Waterloo</td>
      <td>1259.01</td>
      <td>160.38</td>
      <td>68.57</td>
      <td>443.84</td>
      <td>35.11</td>
      <td>223.87</td>
    </tr>
    <tr>
      <th>12</th>
      <td>London</td>
      <td>1064.33</td>
      <td>152.39</td>
      <td>77.69</td>
      <td>447.96</td>
      <td>37.19</td>
      <td>222.72</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Oshawa</td>
      <td>1377.41</td>
      <td>148.44</td>
      <td>68.35</td>
      <td>434.65</td>
      <td>40.46</td>
      <td>227.57</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Québec</td>
      <td>847.15</td>
      <td>112.63</td>
      <td>18.53</td>
      <td>413.96</td>
      <td>70.40</td>
      <td>168.26</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Regina</td>
      <td>1315.70</td>
      <td>172.21</td>
      <td>99.58</td>
      <td>525.89</td>
      <td>49.03</td>
      <td>301.70</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Saskatoon</td>
      <td>1250.51</td>
      <td>172.58</td>
      <td>88.81</td>
      <td>514.10</td>
      <td>47.80</td>
      <td>280.73</td>
    </tr>
    <tr>
      <th>17</th>
      <td>St. Catharines-Niagara</td>
      <td>1050.17</td>
      <td>147.35</td>
      <td>65.99</td>
      <td>436.96</td>
      <td>39.89</td>
      <td>211.47</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Victoria</td>
      <td>1530.36</td>
      <td>166.79</td>
      <td>50.85</td>
      <td>467.52</td>
      <td>39.34</td>
      <td>198.60</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Windsor</td>
      <td>943.45</td>
      <td>137.13</td>
      <td>66.84</td>
      <td>454.20</td>
      <td>37.52</td>
      <td>222.11</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Winnipeg</td>
      <td>1056.09</td>
      <td>151.07</td>
      <td>65.19</td>
      <td>477.73</td>
      <td>40.84</td>
      <td>231.24</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Small</td>
      <td>1007.85</td>
      <td>157.05</td>
      <td>67.41</td>
      <td>465.64</td>
      <td>53.24</td>
      <td>274.47</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Abbotsford-Mission</td>
      <td>1385.80</td>
      <td>164.92</td>
      <td>51.39</td>
      <td>487.88</td>
      <td>40.04</td>
      <td>252.53</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Barrie</td>
      <td>1310.81</td>
      <td>153.93</td>
      <td>73.63</td>
      <td>448.27</td>
      <td>43.02</td>
      <td>235.95</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Brantford</td>
      <td>1118.22</td>
      <td>153.18</td>
      <td>73.27</td>
      <td>443.46</td>
      <td>41.51</td>
      <td>257.64</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Charlottetown</td>
      <td>927.47</td>
      <td>180.73</td>
      <td>85.30</td>
      <td>416.12</td>
      <td>46.77</td>
      <td>251.96</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Greater Sudbury</td>
      <td>1076.65</td>
      <td>175.88</td>
      <td>88.10</td>
      <td>452.44</td>
      <td>47.68</td>
      <td>284.87</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Guelph</td>
      <td>1314.17</td>
      <td>146.44</td>
      <td>61.44</td>
      <td>441.99</td>
      <td>34.80</td>
      <td>240.35</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Kelowna</td>
      <td>1409.10</td>
      <td>192.00</td>
      <td>60.61</td>
      <td>510.96</td>
      <td>41.82</td>
      <td>242.12</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Kingston</td>
      <td>1156.81</td>
      <td>151.15</td>
      <td>77.88</td>
      <td>443.13</td>
      <td>39.21</td>
      <td>215.95</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Moncton</td>
      <td>853.60</td>
      <td>144.16</td>
      <td>86.25</td>
      <td>422.79</td>
      <td>61.58</td>
      <td>282.28</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Other Cities</td>
      <td>991.43</td>
      <td>157.73</td>
      <td>67.83</td>
      <td>472.42</td>
      <td>54.32</td>
      <td>282.05</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Peterborough</td>
      <td>1116.64</td>
      <td>142.10</td>
      <td>71.61</td>
      <td>429.21</td>
      <td>38.20</td>
      <td>236.86</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Saguenay</td>
      <td>713.95</td>
      <td>134.90</td>
      <td>22.41</td>
      <td>422.36</td>
      <td>64.83</td>
      <td>196.19</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Saint John</td>
      <td>898.67</td>
      <td>182.58</td>
      <td>109.43</td>
      <td>420.53</td>
      <td>56.83</td>
      <td>284.76</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Sherbrooke</td>
      <td>802.99</td>
      <td>136.67</td>
      <td>27.31</td>
      <td>403.15</td>
      <td>66.16</td>
      <td>182.60</td>
    </tr>
    <tr>
      <th>36</th>
      <td>St. John's</td>
      <td>1194.55</td>
      <td>163.04</td>
      <td>105.17</td>
      <td>462.11</td>
      <td>60.01</td>
      <td>312.78</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Thunder Bay</td>
      <td>1029.65</td>
      <td>162.60</td>
      <td>80.29</td>
      <td>473.99</td>
      <td>43.33</td>
      <td>259.88</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Trois-Rivieres</td>
      <td>685.01</td>
      <td>70.66</td>
      <td>17.18</td>
      <td>407.52</td>
      <td>68.85</td>
      <td>174.03</td>
    </tr>
  </tbody>
</table>
</div>




```python
# correlation in the payment dataset
pmt.corr()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Mortgage</th>
      <th>HELOC</th>
      <th>Line Of Credit</th>
      <th>Credit Card</th>
      <th>All Other Credit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mortgage</th>
      <td>1.000000</td>
      <td>0.681225</td>
      <td>0.205755</td>
      <td>-0.680500</td>
      <td>0.073155</td>
    </tr>
    <tr>
      <th>HELOC</th>
      <td>0.681225</td>
      <td>1.000000</td>
      <td>0.554539</td>
      <td>-0.445077</td>
      <td>0.418714</td>
    </tr>
    <tr>
      <th>Line Of Credit</th>
      <td>0.205755</td>
      <td>0.554539</td>
      <td>1.000000</td>
      <td>-0.296063</td>
      <td>0.805166</td>
    </tr>
    <tr>
      <th>Credit Card</th>
      <td>-0.680500</td>
      <td>-0.445077</td>
      <td>-0.296063</td>
      <td>1.000000</td>
      <td>-0.056040</td>
    </tr>
    <tr>
      <th>All Other Credit</th>
      <td>0.073155</td>
      <td>0.418714</td>
      <td>0.805166</td>
      <td>-0.056040</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Plotting the correlation data
f,ax = plt.subplots(figsize=(10,10))
sns.heatmap(pmt.corr(), annot = True,linewidths=.4, fmt='.1f', ax=ax)
plt.show()
```


![png](output_36_0.png)



```python
# Plotting mortgage payment and the geography 
sns.scatterplot(x=pmt['Mortgage'], y=pmt['Geography']);
```


![png](output_37_0.png)



```python
# Looking for the missing data and sum them up
pmt.isnull().sum()
```




    Geography           40
    Mortgage            40
    HELOC               40
    Line Of Credit      40
    Auto Loan           40
    Credit Card         40
    All Other Credit    40
    dtype: int64




```python
# the median for geography and mortgage
pmt.groupby('Geography', as_index=True)['Mortgage'].median()

```




    Geography
    Abbotsford-Mission              1385.80
    Barrie                          1310.81
    Brantford                       1118.22
    Calgary                         1485.66
    Canada                          1230.86
    Charlottetown                    927.47
    Edmonton                        1420.65
    Greater Sudbury                 1076.65
    Guelph                          1314.17
    Halifax                         1099.44
    Hamilton                        1328.58
    Kelowna                         1409.10
    Kingston                        1156.81
    Kitchener-Cambridge-Waterloo    1259.01
    Large                           1437.58
    London                          1064.33
    Medium                          1145.40
    Moncton                          853.60
    Montréal                        1050.52
    Oshawa                          1377.41
    Other Cities                     991.43
    Ottawa-Gatineau                 1198.22
    Peterborough                    1116.64
    Québec                           847.15
    Regina                          1315.70
    Saguenay                         713.95
    Saint John                       898.67
    Saskatoon                       1250.51
    Sherbrooke                       802.99
    Small                           1007.85
    St. Catharines-Niagara          1050.17
    St. John's                      1194.55
    Thunder Bay                     1029.65
    Toronto                         1635.25
    Trois-Rivieres                   685.01
    Vancouver                       1772.20
    Victoria                        1530.36
    Windsor                          943.45
    Winnipeg                        1056.09
    Name: Mortgage, dtype: float64




```python

```

