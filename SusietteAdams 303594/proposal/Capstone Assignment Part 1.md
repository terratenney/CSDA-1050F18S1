##SusietteAdams 3030594

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```


```python
mydata= pd.read_csv("C:\\Users\\susie\\Documents\\Data Science\\Robbery.csv")
```


```python
mydata.head()
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
      <th>X</th>
      <th>Y</th>
      <th>Index_</th>
      <th>event_unique_id</th>
      <th>occurrencedate</th>
      <th>reporteddate</th>
      <th>premisetype</th>
      <th>ucr_code</th>
      <th>ucr_ext</th>
      <th>offence</th>
      <th>...</th>
      <th>occurrencedayofyear</th>
      <th>occurrencedayofweek</th>
      <th>occurrencehour</th>
      <th>MCI</th>
      <th>Division</th>
      <th>Hood_ID</th>
      <th>Neighbourhood</th>
      <th>Lat</th>
      <th>Long</th>
      <th>ObjectId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-79.374847</td>
      <td>43.660656</td>
      <td>8440</td>
      <td>GO-2015942657</td>
      <td>2015-06-05T14:15:00.000Z</td>
      <td>2015-06-05T15:41:00.000Z</td>
      <td>Outside</td>
      <td>1610</td>
      <td>220</td>
      <td>Robbery - Other</td>
      <td>...</td>
      <td>156.0</td>
      <td>Friday</td>
      <td>14</td>
      <td>Robbery</td>
      <td>D51</td>
      <td>73</td>
      <td>Moss Park (73)</td>
      <td>43.660656</td>
      <td>-79.374847</td>
      <td>1001</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-79.222259</td>
      <td>43.751030</td>
      <td>8441</td>
      <td>GO-2015942418</td>
      <td>2015-06-02T15:00:00.000Z</td>
      <td>2015-06-05T15:09:00.000Z</td>
      <td>Other</td>
      <td>1610</td>
      <td>200</td>
      <td>Robbery - Mugging</td>
      <td>...</td>
      <td>153.0</td>
      <td>Tuesday</td>
      <td>15</td>
      <td>Robbery</td>
      <td>D43</td>
      <td>137</td>
      <td>Woburn (137)</td>
      <td>43.751030</td>
      <td>-79.222259</td>
      <td>1002</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-79.420914</td>
      <td>43.663029</td>
      <td>8445</td>
      <td>GO-20151975524</td>
      <td>2015-11-17T21:05:00.000Z</td>
      <td>2015-11-17T22:18:00.000Z</td>
      <td>Outside</td>
      <td>1610</td>
      <td>200</td>
      <td>Robbery - Mugging</td>
      <td>...</td>
      <td>321.0</td>
      <td>Tuesday</td>
      <td>21</td>
      <td>Robbery</td>
      <td>D14</td>
      <td>93</td>
      <td>Dovercourt-Wallace Emerson-Junction (93)</td>
      <td>43.663029</td>
      <td>-79.420914</td>
      <td>1003</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-79.381638</td>
      <td>43.667374</td>
      <td>8447</td>
      <td>GO-20151976833</td>
      <td>2015-11-18T05:23:00.000Z</td>
      <td>2015-11-18T05:23:00.000Z</td>
      <td>Commercial</td>
      <td>1610</td>
      <td>210</td>
      <td>Robbery - Business</td>
      <td>...</td>
      <td>322.0</td>
      <td>Wednesday</td>
      <td>5</td>
      <td>Robbery</td>
      <td>D51</td>
      <td>75</td>
      <td>Church-Yonge Corridor (75)</td>
      <td>43.667374</td>
      <td>-79.381638</td>
      <td>1004</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-79.313820</td>
      <td>43.675320</td>
      <td>8453</td>
      <td>GO-20152102376</td>
      <td>2015-12-08T12:10:00.000Z</td>
      <td>2015-12-08T12:19:00.000Z</td>
      <td>Outside</td>
      <td>1610</td>
      <td>220</td>
      <td>Robbery - Other</td>
      <td>...</td>
      <td>342.0</td>
      <td>Tuesday</td>
      <td>12</td>
      <td>Robbery</td>
      <td>D55</td>
      <td>64</td>
      <td>Woodbine Corridor (64)</td>
      <td>43.675320</td>
      <td>-79.313820</td>
      <td>1005</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 29 columns</p>
</div>




```python
mydata.shape
```




    (18128, 29)




```python
mydata.dtypes
```




    X                      float64
    Y                      float64
    Index_                   int64
    event_unique_id         object
    occurrencedate          object
    reporteddate            object
    premisetype             object
    ucr_code                 int64
    ucr_ext                  int64
    offence                 object
    reportedyear             int64
    reportedmonth           object
    reportedday              int64
    reporteddayofyear        int64
    reporteddayofweek       object
    reportedhour             int64
    occurrenceyear         float64
    occurrencemonth         object
    occurrenceday          float64
    occurrencedayofyear    float64
    occurrencedayofweek     object
    occurrencehour           int64
    MCI                     object
    Division                object
    Hood_ID                  int64
    Neighbourhood           object
    Lat                    float64
    Long                   float64
    ObjectId                 int64
    dtype: object




```python
# Any missing values?
print mydata.isnull().values.any()
```


      File "<ipython-input-21-2b10e1c3b684>", line 2
        print mydata.isnull().values.any()
                   ^
    SyntaxError: invalid syntax
    



```python
data = pd.read_csv("C:\\Users\\susie\\Documents\\Data Science\\Ranking.csv") 
```


```python
data.head(5)
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
      <th>Forward Sortation Area ID</th>
      <th># Basics | Total Population, 2018</th>
      <th># Basics | Total Households, 2018</th>
      <th>% Total Households For Period Built Before 1961, 2018</th>
      <th>Median Household Income (Current Year $), 2018</th>
      <th>% Household Income $100,000 Or Over (Current Year $), 2018</th>
      <th>% Household Population 25 To 64 Years | No Certificate, Diploma Or Degree, 2018</th>
      <th>% Household Population 25 To 64 Years | University Certificate, Diploma Or Degree At Bachelor Level Or Above, 2018</th>
      <th># Female Population by Age | Females, 2018</th>
      <th># Male Population by Age | Males, 2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M2N, ON (FSA)</td>
      <td>M2N</td>
      <td>80,788</td>
      <td>36,085</td>
      <td>10.01%</td>
      <td>$53,967.03</td>
      <td>28.60%</td>
      <td>2.97%</td>
      <td>64.21%</td>
      <td>42,474</td>
      <td>38,314</td>
    </tr>
    <tr>
      <th>1</th>
      <td>M1B, ON (FSA)</td>
      <td>M1B</td>
      <td>69,822</td>
      <td>21,405</td>
      <td>3.40%</td>
      <td>$69,030.40</td>
      <td>27.71%</td>
      <td>14.10%</td>
      <td>23.60%</td>
      <td>36,057</td>
      <td>33,765</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M2J, ON (FSA)</td>
      <td>M2J</td>
      <td>62,478</td>
      <td>23,398</td>
      <td>8.48%</td>
      <td>$56,317.30</td>
      <td>26.31%</td>
      <td>6.50%</td>
      <td>48.99%</td>
      <td>32,257</td>
      <td>30,221</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M9V, ON (FSA)</td>
      <td>M9V</td>
      <td>59,619</td>
      <td>17,941</td>
      <td>17.93%</td>
      <td>$51,937.87</td>
      <td>22.12%</td>
      <td>21.05%</td>
      <td>20.65%</td>
      <td>30,106</td>
      <td>29,513</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M1V, ON (FSA)</td>
      <td>M1V</td>
      <td>58,107</td>
      <td>17,114</td>
      <td>2.10%</td>
      <td>$56,514.30</td>
      <td>29.15%</td>
      <td>21.43%</td>
      <td>26.35%</td>
      <td>29,712</td>
      <td>28,395</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.shape
```




    (96, 11)




```python

```


```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
```


```python
url = "https://toronto.listing.ca/"
html = urlopen(url)
```


```python
soup = BeautifulSoup(html, 'lxml')
type(soup)
```




    bs4.BeautifulSoup




```python
# Get the title
title = soup.title
print(title)
```

    <title>
    	Toronto MLS® Listings for Sale | Listing.ca
    </title>
    


```python
# Print out the text
text = soup.get_text()
#print(soup.text)
```


```python
soup.find_all('a')
```




    [<a href="https://listing.ca"><img src="https://listing.ca/images/listing.ca.logo.png" title="Listing.ca Home"/></a>,
     <a class="f13" href="https://ajax.listing.ca/real-estate-price-history.htm">Ajax Price History</a>,
     <a class="f13" href="https://aurora.listing.ca/real-estate-price-history.htm">Aurora Price History</a>,
     <a class="f13" href="https://barrie.listing.ca/real-estate-price-history.htm">Barrie Price History</a>,
     <a class="f13" href="https://brampton.listing.ca/real-estate-price-history.htm">Brampton Price History</a>,
     <a class="f13" href="https://clarington.listing.ca/real-estate-price-history.htm">Clarington Price History</a>,
     <a class="f13" href="https://georgina.listing.ca/real-estate-price-history.htm">Georgina Price History</a>,
     <a class="f13" href="https://markham.listing.ca/real-estate-price-history.htm">Markham Price History</a>,
     <a class="f13" href="https://milton.listing.ca/real-estate-price-history.htm">Milton Price History</a>,
     <a class="f13" href="https://mississauga.listing.ca/real-estate-price-history.htm">Mississauga Price History</a>,
     <a class="f13" href="https://newmarket.listing.ca/real-estate-price-history.htm">Newmarket Price History</a>,
     <a class="f13" href="https://oakville.listing.ca/real-estate-price-history.htm">Oakville Price History</a>,
     <a class="f13" href="https://oshawa.listing.ca/real-estate-price-history.htm">Oshawa Price History</a>,
     <a class="f13" href="https://richmond-hill.listing.ca/real-estate-price-history.htm">Richmond Hill Price History</a>,
     <a class="f13" href="https://toronto.listing.ca/real-estate-price-history.htm">Toronto Price History</a>,
     <a class="f13" href="https://vaughan.listing.ca/real-estate-price-history.htm">Vaughan Price History</a>,
     <a class="f13" href="https://whitby.listing.ca/real-estate-price-history.htm">Whitby Price History</a>,
     <a href="https://ecovinyl.ca/windows/replacement/toronto.htm" style="color:inherit;font-size:inherit;">Toronto Windows</a>,
     <a class="f13" href="https://mortgagecalculator.ca">Mortgage Calculator</a>,
     <a class="f13" href="https://toronto.listing.ca/second-mortgage-calculator.htm">Second Mortgage Calculator</a>,
     <a class="f13" href="https://toronto.listing.ca/bad-credit-mortgages.htm">Bad Credit Mortgages</a>,
     <a class="f13" href="https://toronto.listing.ca/debt-consolidation.htm">Debt Consolidation</a>,
     <a class="f13" href="https://toronto.listing.ca/home-equity-loans.htm">Home Equity Loans</a>,
     <a class="f13" href="https://toronto.listing.ca/mortgage-refinancing.htm">Mortgage Refinancing</a>,
     <a class="f13" href="https://toronto.listing.ca/private-mortgages.htm">Private Mortgages</a>,
     <a class="f13" href="https://toronto.listing.ca/private-lenders.htm">Private Lenders</a>,
     <a class="f13" href="https://toronto.listing.ca/private-loans.htm">Private Loans</a>,
     <a class="f13" href="https://toronto.listing.ca/stop-power-of-sale.htm">Stop Power of Sale</a>,
     <a class="f13" href="https://toronto.listing.ca/stop-bankruptcy.htm">Stop Bankruptcy</a>,
     <a class="f13" href="https://торонто.listing.ca/консолидация-долгов">Консолидация Долгов</a>,
     <a class="f13" href="https://多伦多.listing.ca/债务合并">债务合并</a>,
     <a class="button" href="https://toronto.listing.ca/for-rent.htm">FOR RENT</a>,
     <a href="https://toronto.listing.ca/condos.htm">Condos</a>,
     <a href="https://toronto.listing.ca/condo-townhomes.htm">Condo Townhomes</a>,
     <a href="https://toronto.listing.ca/freehold-townhomes.htm">Freehold Townhomes</a>,
     <a href="https://toronto.listing.ca/detached-homes.htm">Detached Homes</a>,
     <a href="https://listing.ca" rel="nofollow">clear</a>,
     <a href="https://barrie.listing.ca">Barrie</a>,
     <a href="https://brampton.listing.ca">Brampton</a>,
     <a href="https://burlington.listing.ca">Burlington</a>,
     <a href="https://clarington.listing.ca">Clarington</a>,
     <a href="https://hamilton.listing.ca">Hamilton</a>,
     <a href="https://innisfil.listing.ca">Innisfil</a>,
     <a href="https://markham.listing.ca">Markham</a>,
     <a href="https://mississauga.listing.ca">Mississauga</a>,
     <a href="https://newmarket.listing.ca">Newmarket</a>,
     <a href="https://oakville.listing.ca">Oakville</a>,
     <a href="https://oshawa.listing.ca">Oshawa</a>,
     <a href="https://richmond-hill.listing.ca">Richmond Hill</a>,
     <a href="https://toronto.listing.ca">Toronto</a>,
     <a href="https://toronto.listing.ca/bay-street-corridor.htm">Bay Street Corridor</a>,
     <a href="https://toronto.listing.ca/church-yonge-corridor.htm">Church-Yonge Corridor</a>,
     <a href="https://toronto.listing.ca/mimico.htm">Mimico</a>,
     <a href="https://toronto.listing.ca/waterfront-communities-c1.htm">Waterfront Communities C1</a>,
     <a href="https://toronto.listing.ca/willowdale-east.htm">Willowdale East</a>,
     <a href="https://vaughan.listing.ca">Vaughan</a>,
     <a href="https://whitby.listing.ca">Whitby</a>,
     <a href="https://listing.ca/mls/?.cy..0.........$" rel="nofollow">0-Beds</a>,
     <a href="https://listing.ca/mls/?.cy..1.........$" rel="nofollow">1-Bed</a>,
     <a href="https://listing.ca/mls/?.cy..2.........$" rel="nofollow">2-Beds</a>,
     <a href="https://listing.ca/mls/?.cy..3.........$" rel="nofollow">3-Beds</a>,
     <a href="https://listing.ca/mls/?.cy..4.........$" rel="nofollow">4-Beds</a>,
     <a href="https://listing.ca/mls/?.cy..5.........$" rel="nofollow">5-Beds</a>,
     <a href="https://listing.ca/mls/?.cy..6.........$" rel="nofollow">6-Beds</a>,
     <a href="https://listing.ca/mls/?.cy..7.........$" rel="nofollow">7-Beds</a>,
     <a href="https://listing.ca/mls/?.cy..8.........$" rel="nofollow">8-Beds</a>,
     <a href="https://listing.ca/mls/?.cy..9.........$" rel="nofollow">9-Beds</a>,
     <a href="https://listing.ca/mls/?.cy...0........$" rel="nofollow">0-Beds</a>,
     <a href="https://listing.ca/mls/?.cy...1........$" rel="nofollow">1-Bed</a>,
     <a href="https://listing.ca/mls/?.cy...2........$" rel="nofollow">2-Beds</a>,
     <a href="https://listing.ca/mls/?.cy...3........$" rel="nofollow">3-Beds</a>,
     <a href="https://listing.ca/mls/?.cy...4........$" rel="nofollow">4-Beds</a>,
     <a href="https://listing.ca/mls/?.cy...5........$" rel="nofollow">5-Beds</a>,
     <a href="https://listing.ca/mls/?.cy...6........$" rel="nofollow">6-Beds</a>,
     <a href="https://listing.ca/mls/?.cy...7........$" rel="nofollow">7-Beds</a>,
     <a href="https://listing.ca/mls/?.cy...8........$" rel="nofollow">8-Beds</a>,
     <a href="https://listing.ca/mls/?.cy...9........$" rel="nofollow">9-Beds</a>,
     <a href="https://listing.ca/mls/?.cy....0.......$" rel="nofollow">0-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....1.......$" rel="nofollow">1-Bath</a>,
     <a href="https://listing.ca/mls/?.cy....2.......$" rel="nofollow">2-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....3.......$" rel="nofollow">3-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....4.......$" rel="nofollow">4-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....5.......$" rel="nofollow">5-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....6.......$" rel="nofollow">6-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....7.......$" rel="nofollow">7-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....8.......$" rel="nofollow">8-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....9.......$" rel="nofollow">9-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....10.......$" rel="nofollow">10-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....11.......$" rel="nofollow">11-Baths</a>,
     <a href="https://listing.ca/mls/?.cy....12.......$" rel="nofollow">12-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">0-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">1-Bath</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">2-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">3-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">4-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">5-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">6-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">7-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">8-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">9-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">10-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">11-Baths</a>,
     <a href="https://toronto.listing.ca" rel="nofollow">12-Baths</a>,
     <a href="https://listing.ca/mls/?.cy......50000.....$" rel="nofollow">$50k</a>,
     <a href="https://listing.ca/mls/?.cy......100000.....$" rel="nofollow">$100k</a>,
     <a href="https://listing.ca/mls/?.cy......150000.....$" rel="nofollow">$150k</a>,
     <a href="https://listing.ca/mls/?.cy......200000.....$" rel="nofollow">$200k</a>,
     <a href="https://listing.ca/mls/?.cy......300000.....$" rel="nofollow">$300k</a>,
     <a href="https://listing.ca/mls/?.cy......400000.....$" rel="nofollow">$400k</a>,
     <a href="https://listing.ca/mls/?.cy......500000.....$" rel="nofollow">$500k</a>,
     <a href="https://listing.ca/mls/?.cy......600000.....$" rel="nofollow">$600k</a>,
     <a href="https://listing.ca/mls/?.cy......700000.....$" rel="nofollow">$700k</a>,
     <a href="https://listing.ca/mls/?.cy......800000.....$" rel="nofollow">$800k</a>,
     <a href="https://listing.ca/mls/?.cy......900000.....$" rel="nofollow">$900k</a>,
     <a href="https://listing.ca/mls/?.cy......1000000.....$" rel="nofollow">$1.00m</a>,
     <a href="https://listing.ca/mls/?.cy......1250000.....$" rel="nofollow">$1.25m</a>,
     <a href="https://listing.ca/mls/?.cy......1500000.....$" rel="nofollow">$1.50m</a>,
     <a href="https://listing.ca/mls/?.cy......1750000.....$" rel="nofollow">$1.75m</a>,
     <a href="https://listing.ca/mls/?.cy......2000000.....$" rel="nofollow">$2.00m</a>,
     <a href="https://listing.ca/mls/?.cy......2500000.....$" rel="nofollow">$2.50m</a>,
     <a href="https://listing.ca/mls/?.cy......3000000.....$" rel="nofollow">$3.00m</a>,
     <a href="https://listing.ca/mls/?.cy......4000000.....$" rel="nofollow">$4.00m</a>,
     <a href="https://listing.ca/mls/?.cy......5000000.....$" rel="nofollow">$5.00m</a>,
     <a href="https://listing.ca/mls/?.cy......7500000.....$" rel="nofollow">$7.50m</a>,
     <a href="https://listing.ca/mls/?.cy......10000000.....$" rel="nofollow">$10.0m</a>,
     <a href="https://listing.ca/mls/?.cy......15000000.....$" rel="nofollow">$15.0m</a>,
     <a href="https://listing.ca/mls/?.cy......20000000.....$" rel="nofollow">$20.0m</a>,
     <a href="https://listing.ca/mls/?.cy......30000000.....$" rel="nofollow">$30.0m</a>,
     <a href="https://listing.ca/mls/?.cy.......50000....$" rel="nofollow">$50k</a>,
     <a href="https://listing.ca/mls/?.cy.......100000....$" rel="nofollow">$100k</a>,
     <a href="https://listing.ca/mls/?.cy.......150000....$" rel="nofollow">$150k</a>,
     <a href="https://listing.ca/mls/?.cy.......200000....$" rel="nofollow">$200k</a>,
     <a href="https://listing.ca/mls/?.cy.......300000....$" rel="nofollow">$300k</a>,
     <a href="https://listing.ca/mls/?.cy.......400000....$" rel="nofollow">$400k</a>,
     <a href="https://listing.ca/mls/?.cy.......500000....$" rel="nofollow">$500k</a>,
     <a href="https://listing.ca/mls/?.cy.......600000....$" rel="nofollow">$600k</a>,
     <a href="https://listing.ca/mls/?.cy.......700000....$" rel="nofollow">$700k</a>,
     <a href="https://listing.ca/mls/?.cy.......800000....$" rel="nofollow">$800k</a>,
     <a href="https://listing.ca/mls/?.cy.......900000....$" rel="nofollow">$900k</a>,
     <a href="https://listing.ca/mls/?.cy.......1000000....$" rel="nofollow">$1.00m</a>,
     <a href="https://listing.ca/mls/?.cy.......1250000....$" rel="nofollow">$1.25m</a>,
     <a href="https://listing.ca/mls/?.cy.......1500000....$" rel="nofollow">$1.50m</a>,
     <a href="https://listing.ca/mls/?.cy.......1750000....$" rel="nofollow">$1.75m</a>,
     <a href="https://listing.ca/mls/?.cy.......2000000....$" rel="nofollow">$2.00m</a>,
     <a href="https://listing.ca/mls/?.cy.......2500000....$" rel="nofollow">$2.50m</a>,
     <a href="https://listing.ca/mls/?.cy.......3000000....$" rel="nofollow">$3.00m</a>,
     <a href="https://listing.ca/mls/?.cy.......4000000....$" rel="nofollow">$4.00m</a>,
     <a href="https://listing.ca/mls/?.cy.......5000000....$" rel="nofollow">$5.00m</a>,
     <a href="https://listing.ca/mls/?.cy.......7500000....$" rel="nofollow">$7.50m</a>,
     <a href="https://listing.ca/mls/?.cy.......10000000....$" rel="nofollow">$10.0m</a>,
     <a href="https://listing.ca/mls/?.cy.......15000000....$" rel="nofollow">$15.0m</a>,
     <a href="https://listing.ca/mls/?.cy.......20000000....$" rel="nofollow">$20.0m</a>,
     <a href="https://listing.ca/mls/?.cy.......30000000....$" rel="nofollow">$30.0m</a>,
     <a class="tab" href="/real-estate-price-history.htm">Toronto Price History</a>,
     <a class="tab" href="/real-estate-prices-by-community.htm">Toronto Prices by Community</a>,
     <a class="navb" href="https://listing.ca/mls/?.cy.........2..$" rel="nofollow">2</a>,
     <a class="navb" href="https://listing.ca/mls/?.cy.........3..$" rel="nofollow">3</a>,
     <a class="navb" href="https://listing.ca/mls/?.cy.........4..$" rel="nofollow">4</a>,
     <a class="navb" href="https://listing.ca/mls/?.cy.........2..$" rel="nofollow">Next</a>,
     <a href="https://toronto.listing.ca/25-bellehaven-cres.E4492052.htm#15-1"><img alt="25 Bellehaven Cres, Toronto" class="noselect" height="125" id="im517498" src="https://media.listing.ca/E4/49/20/52/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/25-bellehaven-cres.E4492052.htm#15-1"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/25-bellehaven-cres.E4492052.htm#15-1" style="font-size:16px;">25 Bellehaven Cres</a>,
     <a class="na2" href="https://toronto.listing.ca">Toronto</a>,
     <a class="na2" href="https://toronto.listing.ca/scarborough-village.htm">Scarborough Village</a>,
     <a class="na2" href="https://toronto.listing.ca/bellehaven-cres.htm">Bellehaven Cres</a>,
     <a href="https://toronto.listing.ca/37-meadowcliffe-dr.E4492043.htm#15-2"><img alt="37 Meadowcliffe Dr, Toronto" class="noselect" height="125" id="im517497" src="https://media.listing.ca/E4/49/20/43/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/37-meadowcliffe-dr.E4492043.htm#15-2"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/37-meadowcliffe-dr.E4492043.htm#15-2" style="font-size:16px;">37 Meadowcliffe Dr</a>,
     <a class="na2" href="https://toronto.listing.ca/cliffcrest.htm">Cliffcrest</a>,
     <a class="na2" href="https://toronto.listing.ca/meadowcliffe-dr.htm">Meadowcliffe Dr</a>,
     <a href="https://toronto.listing.ca/62-pitt-ave.E4444534.htm#15-3"><img alt="62 Pitt Ave, Toronto" class="noselect" height="125" id="im480912" src="https://media.listing.ca/E4/44/45/34/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/62-pitt-ave.E4444534.htm#15-3"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/62-pitt-ave.E4444534.htm#15-3" style="font-size:16px;">62 Pitt Ave</a>,
     <a class="na2" href="https://toronto.listing.ca/clairlea-birchmount.htm">Clairlea-Birchmount</a>,
     <a class="na2" href="https://toronto.listing.ca/pitt-ave.htm">Pitt Ave</a>,
     <a href="https://toronto.listing.ca/10-navy-wharf-crt-1105.C4516834.htm#15-4"><img alt="10 Navy Wharf Crt 1105, Toronto" class="noselect" height="125" id="im537473" src="https://media.listing.ca/C4/51/68/34/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/10-navy-wharf-crt-1105.C4516834.htm#15-4"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/10-navy-wharf-crt-1105.C4516834.htm#15-4" style="font-size:16px;">10 Navy Wharf Crt 1105</a>,
     <a class="na2" href="https://toronto.listing.ca/waterfront-communities-c1.htm">Waterfront Communities C1</a>,
     <a class="na2" href="https://toronto.listing.ca/navy-wharf-crt.htm">Navy Wharf Crt</a>,
     <a href="https://toronto.listing.ca/42-camden-st-704.C4516966.htm#15-5"><img alt="42 Camden St 704, Toronto" class="noselect" height="125" id="im537466" src="https://media.listing.ca/C4/51/69/66/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/42-camden-st-704.C4516966.htm#15-5"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/42-camden-st-704.C4516966.htm#15-5" style="font-size:16px;">42 Camden St 704</a>,
     <a class="na2" href="https://toronto.listing.ca/camden-st.htm">Camden St</a>,
     <a href="https://toronto.listing.ca/2287-lake-shore-blvd-807.W4516945.htm#15-6"><img alt="2287 Lake Shore Blvd 807, Toronto" class="noselect" height="125" id="im537450" src="https://media.listing.ca/W4/51/69/45/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/2287-lake-shore-blvd-807.W4516945.htm#15-6"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/2287-lake-shore-blvd-807.W4516945.htm#15-6" style="font-size:16px;">2287 Lake Shore Blvd 807</a>,
     <a class="na2" href="https://toronto.listing.ca/mimico.htm">Mimico</a>,
     <a class="na2" href="https://toronto.listing.ca/lake-shore-blvd.htm">Lake Shore Blvd</a>,
     <a href="https://toronto.listing.ca/1111-steeles-ave-508.C4516931.htm#15-7"><img alt="1111 Steeles Ave 508, Toronto" class="noselect" height="125" id="im537449" src="https://media.listing.ca/C4/51/69/31/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/1111-steeles-ave-508.C4516931.htm#15-7"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/1111-steeles-ave-508.C4516931.htm#15-7" style="font-size:16px;">1111 Steeles Ave 508</a>,
     <a class="na2" href="https://toronto.listing.ca/westminster-branson.htm">Westminster-Branson</a>,
     <a class="na2" href="https://toronto.listing.ca/steeles-ave.htm">Steeles Ave</a>,
     <a href="https://toronto.listing.ca/215-bonis-ave-th18.E4516862.htm#15-8"><img alt="215 Bonis Ave Th18, Toronto" class="noselect" height="125" id="im537442" src="https://media.listing.ca/E4/51/68/62/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/215-bonis-ave-th18.E4516862.htm#15-8"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/215-bonis-ave-th18.E4516862.htm#15-8" style="font-size:16px;">215 Bonis Ave Th18</a>,
     <a class="na2" href="https://toronto.listing.ca/tam-o-shanter-sullivan.htm">Tam O'Shanter-Sullivan</a>,
     <a class="na2" href="https://toronto.listing.ca/bonis-ave.htm">Bonis Ave</a>,
     <a href="https://toronto.listing.ca/295-adelaide-st-2907.C4516936.htm#15-9"><img alt="295 Adelaide St 2907, Toronto" class="noselect" height="125" id="im537438" src="https://media.listing.ca/C4/51/69/36/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/295-adelaide-st-2907.C4516936.htm#15-9"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/295-adelaide-st-2907.C4516936.htm#15-9" style="font-size:16px;">295 Adelaide St 2907</a>,
     <a class="na2" href="https://toronto.listing.ca/adelaide-st.htm">Adelaide St</a>,
     <a href="https://toronto.listing.ca/25-carlton-st-1105.C4517078.htm#15-a"><img alt="25 Carlton St 1105, Toronto" class="noselect" height="125" id="im537436" src="https://media.listing.ca/C4/51/70/78/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/25-carlton-st-1105.C4517078.htm#15-a"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/25-carlton-st-1105.C4517078.htm#15-a" style="font-size:16px;">25 Carlton St 1105</a>,
     <a class="na2" href="https://toronto.listing.ca/church-yonge-corridor.htm">Church-Yonge Corridor</a>,
     <a class="na2" href="https://toronto.listing.ca/carlton-st.htm">Carlton St</a>,
     <a href="https://toronto.listing.ca/256-doris-ave-1202.C4517058.htm#15-b"><img alt="256 Doris Ave 1202, Toronto" class="noselect" height="125" id="im537435" src="https://media.listing.ca/C4/51/70/58/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/256-doris-ave-1202.C4517058.htm#15-b"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/256-doris-ave-1202.C4517058.htm#15-b" style="font-size:16px;">256 Doris Ave 1202</a>,
     <a class="na2" href="https://toronto.listing.ca/willowdale-east.htm">Willowdale East</a>,
     <a class="na2" href="https://toronto.listing.ca/doris-ave.htm">Doris Ave</a>,
     <a href="https://toronto.listing.ca/3-massey-sq-1104.E4516951.htm#15-c"><img alt="3 Massey Sq 1104, Toronto" class="noselect" height="125" id="im537432" src="https://media.listing.ca/E4/51/69/51/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/3-massey-sq-1104.E4516951.htm#15-c"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/3-massey-sq-1104.E4516951.htm#15-c" style="font-size:16px;">3 Massey Sq 1104</a>,
     <a class="na2" href="https://toronto.listing.ca/crescent-town.htm">Crescent Town</a>,
     <a class="na2" href="https://toronto.listing.ca/massey-sq.htm">Massey Sq</a>,
     <a href="https://toronto.listing.ca/68-abell-st-538.C4517055.htm#15-d"><img alt="68 Abell St 538, Toronto" class="noselect" height="125" id="im537430" src="https://listing.ca/images/no-image/167x125.gif" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/68-abell-st-538.C4517055.htm#15-d"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/68-abell-st-538.C4517055.htm#15-d" style="font-size:16px;">68 Abell St 538</a>,
     <a class="na2" href="https://toronto.listing.ca/little-portugal.htm">Little Portugal</a>,
     <a class="na2" href="https://toronto.listing.ca/abell-st.htm">Abell St</a>,
     <a href="https://toronto.listing.ca/16-brookers-lane.W4516947.htm#15-e"><img alt="16 Brookers Lane, Toronto" class="noselect" height="125" id="im537426" src="https://listing.ca/images/no-image/167x125.gif" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/16-brookers-lane.W4516947.htm#15-e"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/16-brookers-lane.W4516947.htm#15-e" style="font-size:16px;">16 Brookers Lane</a>,
     <a class="na2" href="https://toronto.listing.ca/brookers-lane.htm">Brookers Lane</a>,
     <a href="https://toronto.listing.ca/225-bamburgh-circ-ph-4.E4517006.htm#15-f"><img alt="225 Bamburgh Circ Ph 4, Toronto" class="noselect" height="125" id="im537423" src="https://media.listing.ca/E4/51/70/06/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/225-bamburgh-circ-ph-4.E4517006.htm#15-f"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/225-bamburgh-circ-ph-4.E4517006.htm#15-f" style="font-size:16px;">225 Bamburgh Circ Ph 4</a>,
     <a class="na2" href="https://toronto.listing.ca/steeles.htm">Steeles</a>,
     <a class="na2" href="https://toronto.listing.ca/bamburgh-circ.htm">Bamburgh Circ</a>,
     <a href="https://toronto.listing.ca/11-brunel-crt-1709.C4516960.htm#15-g"><img alt="11 Brunel Crt 1709, Toronto" class="noselect" height="125" id="im537421" src="https://media.listing.ca/C4/51/69/60/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/11-brunel-crt-1709.C4516960.htm#15-g"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/11-brunel-crt-1709.C4516960.htm#15-g" style="font-size:16px;">11 Brunel Crt 1709</a>,
     <a class="na2" href="https://toronto.listing.ca/brunel-crt.htm">Brunel Crt</a>,
     <a href="https://toronto.listing.ca/225-bamburgh-circ-1912.E4517080.htm#15-h"><img alt="225 Bamburgh Circ 1912, Toronto" class="noselect" height="125" id="im537420" src="https://media.listing.ca/E4/51/70/80/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/225-bamburgh-circ-1912.E4517080.htm#15-h"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/225-bamburgh-circ-1912.E4517080.htm#15-h" style="font-size:16px;">225 Bamburgh Circ 1912</a>,
     <a href="https://toronto.listing.ca/75-st-nicholas-st-2709.C4516987.htm#15-i"><img alt="75 St. Nicholas St 2709, Toronto" class="noselect" height="125" id="im537409" src="https://media.listing.ca/C4/51/69/87/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/75-st-nicholas-st-2709.C4516987.htm#15-i"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/75-st-nicholas-st-2709.C4516987.htm#15-i" style="font-size:16px;">75 St. Nicholas St 2709</a>,
     <a class="na2" href="https://toronto.listing.ca/bay-street-corridor.htm">Bay Street Corridor</a>,
     <a class="na2" href="https://toronto.listing.ca/st-nicholas-st.htm">St. Nicholas St</a>,
     <a href="https://toronto.listing.ca/17-snowshoe-millway.C4499407.htm#15-j"><img alt="17 Snowshoe Millway, Toronto" class="noselect" height="125" id="im537403" src="https://media.listing.ca/C4/49/94/07/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/17-snowshoe-millway.C4499407.htm#15-j"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/17-snowshoe-millway.C4499407.htm#15-j" style="font-size:16px;">17 Snowshoe Millway</a>,
     <a class="na2" href="https://toronto.listing.ca/st-andrew-windfields.htm">St. Andrew-Windfields</a>,
     <a class="na2" href="https://toronto.listing.ca/snowshoe-millway.htm">Snowshoe Millway</a>,
     <a href="https://toronto.listing.ca/5-sheppard-ave-1826.C4517061.htm#15-k"><img alt="5 Sheppard Ave 1826, Toronto" class="noselect" height="125" id="im537402" src="https://media.listing.ca/C4/51/70/61/1.167x125.jpg" style="cursor:pointer;" width="167"/></a>,
     <a href="https://toronto.listing.ca/5-sheppard-ave-1826.C4517061.htm#15-k"><img src="https://listing.ca/images/new.gif"/></a>,
     <a href="https://toronto.listing.ca/5-sheppard-ave-1826.C4517061.htm#15-k" style="font-size:16px;">5 Sheppard Ave 1826</a>,
     <a class="na2" href="https://toronto.listing.ca/sheppard-ave.htm">Sheppard Ave</a>,
     <a class="navb" href="https://listing.ca/mls/?.cy.........2..$" rel="nofollow">2</a>,
     <a class="navb" href="https://listing.ca/mls/?.cy.........3..$" rel="nofollow">3</a>,
     <a class="navb" href="https://listing.ca/mls/?.cy.........4..$" rel="nofollow">4</a>,
     <a class="navb" href="https://listing.ca/mls/?.cy.........2..$" rel="nofollow">Next</a>,
     <a class="join" href="https://listing.ca/team.htm">Join Our Team</a>,
     <a class="f12" href="mailto:info@listing.ca">info@listing.ca</a>,
     <a class="f12" href="https://twitter.com/ListingCa" target="_blank">Listing.ca on Twitter</a>,
     <a class="f12" href="https://www.facebook.com/RealEstateBayRealty/" target="_blank">RealEstateBay.ca on Facebook</a>]




```python
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
```


```python
# Print the first 10 rows for sanity check
rows = soup.find_all('tr')
print(rows[:10])
```

    [<tr>
    <td style="vertical-align: top; border-right: solid 1px #ccc; padding-right: 25px;">
    <div style="overflow:hidden;">
    <div id="popup_address"></div>
    <div id="popup_price"></div>
    </div>
    <div style="overflow:hidden;">
    <div id="popup_beds"></div>
    <div style="float:left;font-size:13px;width:55px;">beds</div>
    <div id="popup_baths"></div>
    <div style="float: left; font-size: 13px;">baths</div>
    </div>
    <div id="popup_image_c">
    <img id="popup_image" src=""/>
    </div>
    </td>
    <td style="vertical-align: top; padding-left: 25px;">
    <table>
    <tr>
    <td></td>
    <td id="popup_type" style="font-size: 20px; color: #0654ba; padding-bottom: 20px;"></td>
    </tr>
    <tr>
    <td class="popup_item">First Name:</td>
    <td><input name="first_name" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_first_name"></div></td>
    </tr>
    <tr>
    <td class="popup_item">Last Name:</td>
    <td><input name="last_name" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_last_name"></div></td>
    </tr>
    <tr>
    <td class="popup_item">Email:</td>
    <td><input name="email" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_email"></div></td>
    </tr>
    <tr>
    <td class="popup_item">Phone:</td>
    <td><input name="phone" style="width: 200px; font-size: 13px;" type="text" value=""/><div class="error" id="err_phone"></div></td>
    </tr>
    <tr id="popup_date">
    <td class="popup_item">Appointment Date:</td>
    <td>
    <select id="day" name="day"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option selected="" value="14">14</option><option value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option><option value="21">21</option><option value="22">22</option><option value="23">23</option><option value="24">24</option><option value="25">25</option><option value="26">26</option><option value="27">27</option><option value="28">28</option><option value="29">29</option><option value="30">30</option><option value="31">31</option></select>
    <select id="month" name="month"><option value="1">January</option><option value="2">February</option><option value="3">March</option><option value="4">April</option><option value="5">May</option><option value="6">June</option><option selected="" value="7">July</option><option value="8">August</option><option value="9">September</option><option value="10">October</option><option value="11">November</option><option value="12">December</option></select>
    <select id="year" name="year"><option selected="" value="2019">2019</option><option value="2020">2020</option></select>
    <div class="error" id="err_date"></div>
    </td>
    </tr>
    <tr>
    <td class="popup_item">Message:</td>
    <td>
    <textarea id="message" name="message" rows="5" style="width: 375px; font-size: 13px;"></textarea>
    </td>
    </tr>
    <tr>
    <td class="popup_item">How did you<br/>find us?</td>
    <td>
    <div style="width: 375px; overflow: hidden; padding-bottom:3px;">
    <div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_1" type="checkbox"/>Referred by my Realtor</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_2" type="checkbox"/>Google</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_3" type="checkbox"/>Facebook</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_4" type="checkbox"/>TV - CP24</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_5" type="checkbox"/>TV - CTV News</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_6" type="checkbox"/>TV - CTV Shark Tank</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_7" type="checkbox"/>Radio - Z103.5</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_8" type="checkbox"/>Radio - Chum FM</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_9" type="checkbox"/>Radio - Edge 92</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_10" type="checkbox"/>Word of Mouth</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_11" type="checkbox"/>Other</div>
    </div>
    </td>
    </tr>
    <tr>
    <td></td>
    <td style="padding-top:20px;">
    <div class="button btn2c btnred" onclick="$m.lead.submit();" style="float:none;">Send Request</div>
    <div class="button btn2c" onclick="$m.lead.close();" style="float:none;">Cancel</div>
    </td>
    </tr>
    </table>
    </td>
    </tr>, <tr>
    <td></td>
    <td id="popup_type" style="font-size: 20px; color: #0654ba; padding-bottom: 20px;"></td>
    </tr>, <tr>
    <td class="popup_item">First Name:</td>
    <td><input name="first_name" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_first_name"></div></td>
    </tr>, <tr>
    <td class="popup_item">Last Name:</td>
    <td><input name="last_name" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_last_name"></div></td>
    </tr>, <tr>
    <td class="popup_item">Email:</td>
    <td><input name="email" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_email"></div></td>
    </tr>, <tr>
    <td class="popup_item">Phone:</td>
    <td><input name="phone" style="width: 200px; font-size: 13px;" type="text" value=""/><div class="error" id="err_phone"></div></td>
    </tr>, <tr id="popup_date">
    <td class="popup_item">Appointment Date:</td>
    <td>
    <select id="day" name="day"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option selected="" value="14">14</option><option value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option><option value="21">21</option><option value="22">22</option><option value="23">23</option><option value="24">24</option><option value="25">25</option><option value="26">26</option><option value="27">27</option><option value="28">28</option><option value="29">29</option><option value="30">30</option><option value="31">31</option></select>
    <select id="month" name="month"><option value="1">January</option><option value="2">February</option><option value="3">March</option><option value="4">April</option><option value="5">May</option><option value="6">June</option><option selected="" value="7">July</option><option value="8">August</option><option value="9">September</option><option value="10">October</option><option value="11">November</option><option value="12">December</option></select>
    <select id="year" name="year"><option selected="" value="2019">2019</option><option value="2020">2020</option></select>
    <div class="error" id="err_date"></div>
    </td>
    </tr>, <tr>
    <td class="popup_item">Message:</td>
    <td>
    <textarea id="message" name="message" rows="5" style="width: 375px; font-size: 13px;"></textarea>
    </td>
    </tr>, <tr>
    <td class="popup_item">How did you<br/>find us?</td>
    <td>
    <div style="width: 375px; overflow: hidden; padding-bottom:3px;">
    <div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_1" type="checkbox"/>Referred by my Realtor</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_2" type="checkbox"/>Google</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_3" type="checkbox"/>Facebook</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_4" type="checkbox"/>TV - CP24</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_5" type="checkbox"/>TV - CTV News</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_6" type="checkbox"/>TV - CTV Shark Tank</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_7" type="checkbox"/>Radio - Z103.5</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_8" type="checkbox"/>Radio - Chum FM</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_9" type="checkbox"/>Radio - Edge 92</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_10" type="checkbox"/>Word of Mouth</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_11" type="checkbox"/>Other</div>
    </div>
    </td>
    </tr>, <tr>
    <td></td>
    <td style="padding-top:20px;">
    <div class="button btn2c btnred" onclick="$m.lead.submit();" style="float:none;">Send Request</div>
    <div class="button btn2c" onclick="$m.lead.close();" style="float:none;">Cancel</div>
    </td>
    </tr>]
    


```python
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
```

    https://listing.ca
    https://ajax.listing.ca/real-estate-price-history.htm
    https://aurora.listing.ca/real-estate-price-history.htm
    https://barrie.listing.ca/real-estate-price-history.htm
    https://brampton.listing.ca/real-estate-price-history.htm
    https://clarington.listing.ca/real-estate-price-history.htm
    https://georgina.listing.ca/real-estate-price-history.htm
    https://markham.listing.ca/real-estate-price-history.htm
    https://milton.listing.ca/real-estate-price-history.htm
    https://mississauga.listing.ca/real-estate-price-history.htm
    https://newmarket.listing.ca/real-estate-price-history.htm
    https://oakville.listing.ca/real-estate-price-history.htm
    https://oshawa.listing.ca/real-estate-price-history.htm
    https://richmond-hill.listing.ca/real-estate-price-history.htm
    https://toronto.listing.ca/real-estate-price-history.htm
    https://vaughan.listing.ca/real-estate-price-history.htm
    https://whitby.listing.ca/real-estate-price-history.htm
    https://ecovinyl.ca/windows/replacement/toronto.htm
    https://mortgagecalculator.ca
    https://toronto.listing.ca/second-mortgage-calculator.htm
    https://toronto.listing.ca/bad-credit-mortgages.htm
    https://toronto.listing.ca/debt-consolidation.htm
    https://toronto.listing.ca/home-equity-loans.htm
    https://toronto.listing.ca/mortgage-refinancing.htm
    https://toronto.listing.ca/private-mortgages.htm
    https://toronto.listing.ca/private-lenders.htm
    https://toronto.listing.ca/private-loans.htm
    https://toronto.listing.ca/stop-power-of-sale.htm
    https://toronto.listing.ca/stop-bankruptcy.htm
    https://торонто.listing.ca/консолидация-долгов
    https://多伦多.listing.ca/债务合并
    https://toronto.listing.ca/for-rent.htm
    https://toronto.listing.ca/condos.htm
    https://toronto.listing.ca/condo-townhomes.htm
    https://toronto.listing.ca/freehold-townhomes.htm
    https://toronto.listing.ca/detached-homes.htm
    https://listing.ca
    https://barrie.listing.ca
    https://brampton.listing.ca
    https://burlington.listing.ca
    https://clarington.listing.ca
    https://hamilton.listing.ca
    https://innisfil.listing.ca
    https://markham.listing.ca
    https://mississauga.listing.ca
    https://newmarket.listing.ca
    https://oakville.listing.ca
    https://oshawa.listing.ca
    https://richmond-hill.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca/bay-street-corridor.htm
    https://toronto.listing.ca/church-yonge-corridor.htm
    https://toronto.listing.ca/mimico.htm
    https://toronto.listing.ca/waterfront-communities-c1.htm
    https://toronto.listing.ca/willowdale-east.htm
    https://vaughan.listing.ca
    https://whitby.listing.ca
    https://listing.ca/mls/?.cy..0.........$
    https://listing.ca/mls/?.cy..1.........$
    https://listing.ca/mls/?.cy..2.........$
    https://listing.ca/mls/?.cy..3.........$
    https://listing.ca/mls/?.cy..4.........$
    https://listing.ca/mls/?.cy..5.........$
    https://listing.ca/mls/?.cy..6.........$
    https://listing.ca/mls/?.cy..7.........$
    https://listing.ca/mls/?.cy..8.........$
    https://listing.ca/mls/?.cy..9.........$
    https://listing.ca/mls/?.cy...0........$
    https://listing.ca/mls/?.cy...1........$
    https://listing.ca/mls/?.cy...2........$
    https://listing.ca/mls/?.cy...3........$
    https://listing.ca/mls/?.cy...4........$
    https://listing.ca/mls/?.cy...5........$
    https://listing.ca/mls/?.cy...6........$
    https://listing.ca/mls/?.cy...7........$
    https://listing.ca/mls/?.cy...8........$
    https://listing.ca/mls/?.cy...9........$
    https://listing.ca/mls/?.cy....0.......$
    https://listing.ca/mls/?.cy....1.......$
    https://listing.ca/mls/?.cy....2.......$
    https://listing.ca/mls/?.cy....3.......$
    https://listing.ca/mls/?.cy....4.......$
    https://listing.ca/mls/?.cy....5.......$
    https://listing.ca/mls/?.cy....6.......$
    https://listing.ca/mls/?.cy....7.......$
    https://listing.ca/mls/?.cy....8.......$
    https://listing.ca/mls/?.cy....9.......$
    https://listing.ca/mls/?.cy....10.......$
    https://listing.ca/mls/?.cy....11.......$
    https://listing.ca/mls/?.cy....12.......$
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://toronto.listing.ca
    https://listing.ca/mls/?.cy......50000.....$
    https://listing.ca/mls/?.cy......100000.....$
    https://listing.ca/mls/?.cy......150000.....$
    https://listing.ca/mls/?.cy......200000.....$
    https://listing.ca/mls/?.cy......300000.....$
    https://listing.ca/mls/?.cy......400000.....$
    https://listing.ca/mls/?.cy......500000.....$
    https://listing.ca/mls/?.cy......600000.....$
    https://listing.ca/mls/?.cy......700000.....$
    https://listing.ca/mls/?.cy......800000.....$
    https://listing.ca/mls/?.cy......900000.....$
    https://listing.ca/mls/?.cy......1000000.....$
    https://listing.ca/mls/?.cy......1250000.....$
    https://listing.ca/mls/?.cy......1500000.....$
    https://listing.ca/mls/?.cy......1750000.....$
    https://listing.ca/mls/?.cy......2000000.....$
    https://listing.ca/mls/?.cy......2500000.....$
    https://listing.ca/mls/?.cy......3000000.....$
    https://listing.ca/mls/?.cy......4000000.....$
    https://listing.ca/mls/?.cy......5000000.....$
    https://listing.ca/mls/?.cy......7500000.....$
    https://listing.ca/mls/?.cy......10000000.....$
    https://listing.ca/mls/?.cy......15000000.....$
    https://listing.ca/mls/?.cy......20000000.....$
    https://listing.ca/mls/?.cy......30000000.....$
    https://listing.ca/mls/?.cy.......50000....$
    https://listing.ca/mls/?.cy.......100000....$
    https://listing.ca/mls/?.cy.......150000....$
    https://listing.ca/mls/?.cy.......200000....$
    https://listing.ca/mls/?.cy.......300000....$
    https://listing.ca/mls/?.cy.......400000....$
    https://listing.ca/mls/?.cy.......500000....$
    https://listing.ca/mls/?.cy.......600000....$
    https://listing.ca/mls/?.cy.......700000....$
    https://listing.ca/mls/?.cy.......800000....$
    https://listing.ca/mls/?.cy.......900000....$
    https://listing.ca/mls/?.cy.......1000000....$
    https://listing.ca/mls/?.cy.......1250000....$
    https://listing.ca/mls/?.cy.......1500000....$
    https://listing.ca/mls/?.cy.......1750000....$
    https://listing.ca/mls/?.cy.......2000000....$
    https://listing.ca/mls/?.cy.......2500000....$
    https://listing.ca/mls/?.cy.......3000000....$
    https://listing.ca/mls/?.cy.......4000000....$
    https://listing.ca/mls/?.cy.......5000000....$
    https://listing.ca/mls/?.cy.......7500000....$
    https://listing.ca/mls/?.cy.......10000000....$
    https://listing.ca/mls/?.cy.......15000000....$
    https://listing.ca/mls/?.cy.......20000000....$
    https://listing.ca/mls/?.cy.......30000000....$
    /real-estate-price-history.htm
    /real-estate-prices-by-community.htm
    https://listing.ca/mls/?.cy.........2..$
    https://listing.ca/mls/?.cy.........3..$
    https://listing.ca/mls/?.cy.........4..$
    https://listing.ca/mls/?.cy.........2..$
    https://toronto.listing.ca/25-bellehaven-cres.E4492052.htm#15-1
    https://toronto.listing.ca/25-bellehaven-cres.E4492052.htm#15-1
    https://toronto.listing.ca/25-bellehaven-cres.E4492052.htm#15-1
    https://toronto.listing.ca
    https://toronto.listing.ca/scarborough-village.htm
    https://toronto.listing.ca/bellehaven-cres.htm
    https://toronto.listing.ca/37-meadowcliffe-dr.E4492043.htm#15-2
    https://toronto.listing.ca/37-meadowcliffe-dr.E4492043.htm#15-2
    https://toronto.listing.ca/37-meadowcliffe-dr.E4492043.htm#15-2
    https://toronto.listing.ca/cliffcrest.htm
    https://toronto.listing.ca/meadowcliffe-dr.htm
    https://toronto.listing.ca/62-pitt-ave.E4444534.htm#15-3
    https://toronto.listing.ca/62-pitt-ave.E4444534.htm#15-3
    https://toronto.listing.ca/62-pitt-ave.E4444534.htm#15-3
    https://toronto.listing.ca/clairlea-birchmount.htm
    https://toronto.listing.ca/pitt-ave.htm
    https://toronto.listing.ca/10-navy-wharf-crt-1105.C4516834.htm#15-4
    https://toronto.listing.ca/10-navy-wharf-crt-1105.C4516834.htm#15-4
    https://toronto.listing.ca/10-navy-wharf-crt-1105.C4516834.htm#15-4
    https://toronto.listing.ca/waterfront-communities-c1.htm
    https://toronto.listing.ca/navy-wharf-crt.htm
    https://toronto.listing.ca/42-camden-st-704.C4516966.htm#15-5
    https://toronto.listing.ca/42-camden-st-704.C4516966.htm#15-5
    https://toronto.listing.ca/42-camden-st-704.C4516966.htm#15-5
    https://toronto.listing.ca/camden-st.htm
    https://toronto.listing.ca/2287-lake-shore-blvd-807.W4516945.htm#15-6
    https://toronto.listing.ca/2287-lake-shore-blvd-807.W4516945.htm#15-6
    https://toronto.listing.ca/2287-lake-shore-blvd-807.W4516945.htm#15-6
    https://toronto.listing.ca/mimico.htm
    https://toronto.listing.ca/lake-shore-blvd.htm
    https://toronto.listing.ca/1111-steeles-ave-508.C4516931.htm#15-7
    https://toronto.listing.ca/1111-steeles-ave-508.C4516931.htm#15-7
    https://toronto.listing.ca/1111-steeles-ave-508.C4516931.htm#15-7
    https://toronto.listing.ca/westminster-branson.htm
    https://toronto.listing.ca/steeles-ave.htm
    https://toronto.listing.ca/215-bonis-ave-th18.E4516862.htm#15-8
    https://toronto.listing.ca/215-bonis-ave-th18.E4516862.htm#15-8
    https://toronto.listing.ca/215-bonis-ave-th18.E4516862.htm#15-8
    https://toronto.listing.ca/tam-o-shanter-sullivan.htm
    https://toronto.listing.ca/bonis-ave.htm
    https://toronto.listing.ca/295-adelaide-st-2907.C4516936.htm#15-9
    https://toronto.listing.ca/295-adelaide-st-2907.C4516936.htm#15-9
    https://toronto.listing.ca/295-adelaide-st-2907.C4516936.htm#15-9
    https://toronto.listing.ca/adelaide-st.htm
    https://toronto.listing.ca/25-carlton-st-1105.C4517078.htm#15-a
    https://toronto.listing.ca/25-carlton-st-1105.C4517078.htm#15-a
    https://toronto.listing.ca/25-carlton-st-1105.C4517078.htm#15-a
    https://toronto.listing.ca/church-yonge-corridor.htm
    https://toronto.listing.ca/carlton-st.htm
    https://toronto.listing.ca/256-doris-ave-1202.C4517058.htm#15-b
    https://toronto.listing.ca/256-doris-ave-1202.C4517058.htm#15-b
    https://toronto.listing.ca/256-doris-ave-1202.C4517058.htm#15-b
    https://toronto.listing.ca/willowdale-east.htm
    https://toronto.listing.ca/doris-ave.htm
    https://toronto.listing.ca/3-massey-sq-1104.E4516951.htm#15-c
    https://toronto.listing.ca/3-massey-sq-1104.E4516951.htm#15-c
    https://toronto.listing.ca/3-massey-sq-1104.E4516951.htm#15-c
    https://toronto.listing.ca/crescent-town.htm
    https://toronto.listing.ca/massey-sq.htm
    https://toronto.listing.ca/68-abell-st-538.C4517055.htm#15-d
    https://toronto.listing.ca/68-abell-st-538.C4517055.htm#15-d
    https://toronto.listing.ca/68-abell-st-538.C4517055.htm#15-d
    https://toronto.listing.ca/little-portugal.htm
    https://toronto.listing.ca/abell-st.htm
    https://toronto.listing.ca/16-brookers-lane.W4516947.htm#15-e
    https://toronto.listing.ca/16-brookers-lane.W4516947.htm#15-e
    https://toronto.listing.ca/16-brookers-lane.W4516947.htm#15-e
    https://toronto.listing.ca/brookers-lane.htm
    https://toronto.listing.ca/225-bamburgh-circ-ph-4.E4517006.htm#15-f
    https://toronto.listing.ca/225-bamburgh-circ-ph-4.E4517006.htm#15-f
    https://toronto.listing.ca/225-bamburgh-circ-ph-4.E4517006.htm#15-f
    https://toronto.listing.ca/steeles.htm
    https://toronto.listing.ca/bamburgh-circ.htm
    https://toronto.listing.ca/11-brunel-crt-1709.C4516960.htm#15-g
    https://toronto.listing.ca/11-brunel-crt-1709.C4516960.htm#15-g
    https://toronto.listing.ca/11-brunel-crt-1709.C4516960.htm#15-g
    https://toronto.listing.ca/brunel-crt.htm
    https://toronto.listing.ca/225-bamburgh-circ-1912.E4517080.htm#15-h
    https://toronto.listing.ca/225-bamburgh-circ-1912.E4517080.htm#15-h
    https://toronto.listing.ca/225-bamburgh-circ-1912.E4517080.htm#15-h
    https://toronto.listing.ca/75-st-nicholas-st-2709.C4516987.htm#15-i
    https://toronto.listing.ca/75-st-nicholas-st-2709.C4516987.htm#15-i
    https://toronto.listing.ca/75-st-nicholas-st-2709.C4516987.htm#15-i
    https://toronto.listing.ca/bay-street-corridor.htm
    https://toronto.listing.ca/st-nicholas-st.htm
    https://toronto.listing.ca/17-snowshoe-millway.C4499407.htm#15-j
    https://toronto.listing.ca/17-snowshoe-millway.C4499407.htm#15-j
    https://toronto.listing.ca/17-snowshoe-millway.C4499407.htm#15-j
    https://toronto.listing.ca/st-andrew-windfields.htm
    https://toronto.listing.ca/snowshoe-millway.htm
    https://toronto.listing.ca/5-sheppard-ave-1826.C4517061.htm#15-k
    https://toronto.listing.ca/5-sheppard-ave-1826.C4517061.htm#15-k
    https://toronto.listing.ca/5-sheppard-ave-1826.C4517061.htm#15-k
    https://toronto.listing.ca/sheppard-ave.htm
    https://listing.ca/mls/?.cy.........2..$
    https://listing.ca/mls/?.cy.........3..$
    https://listing.ca/mls/?.cy.........4..$
    https://listing.ca/mls/?.cy.........2..$
    https://listing.ca/team.htm
    mailto:info@listing.ca
    https://twitter.com/ListingCa
    https://www.facebook.com/RealEstateBayRealty/
    


```python
# Print the first 10 rows for sanity check
rows = soup.find_all('tr')
print(rows[:10])
```

    [<tr>
    <td style="vertical-align: top; border-right: solid 1px #ccc; padding-right: 25px;">
    <div style="overflow:hidden;">
    <div id="popup_address"></div>
    <div id="popup_price"></div>
    </div>
    <div style="overflow:hidden;">
    <div id="popup_beds"></div>
    <div style="float:left;font-size:13px;width:55px;">beds</div>
    <div id="popup_baths"></div>
    <div style="float: left; font-size: 13px;">baths</div>
    </div>
    <div id="popup_image_c">
    <img id="popup_image" src=""/>
    </div>
    </td>
    <td style="vertical-align: top; padding-left: 25px;">
    <table>
    <tr>
    <td></td>
    <td id="popup_type" style="font-size: 20px; color: #0654ba; padding-bottom: 20px;"></td>
    </tr>
    <tr>
    <td class="popup_item">First Name:</td>
    <td><input name="first_name" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_first_name"></div></td>
    </tr>
    <tr>
    <td class="popup_item">Last Name:</td>
    <td><input name="last_name" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_last_name"></div></td>
    </tr>
    <tr>
    <td class="popup_item">Email:</td>
    <td><input name="email" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_email"></div></td>
    </tr>
    <tr>
    <td class="popup_item">Phone:</td>
    <td><input name="phone" style="width: 200px; font-size: 13px;" type="text" value=""/><div class="error" id="err_phone"></div></td>
    </tr>
    <tr id="popup_date">
    <td class="popup_item">Appointment Date:</td>
    <td>
    <select id="day" name="day"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option value="14">14</option><option selected="" value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option><option value="21">21</option><option value="22">22</option><option value="23">23</option><option value="24">24</option><option value="25">25</option><option value="26">26</option><option value="27">27</option><option value="28">28</option><option value="29">29</option><option value="30">30</option><option value="31">31</option></select>
    <select id="month" name="month"><option value="1">January</option><option value="2">February</option><option value="3">March</option><option value="4">April</option><option value="5">May</option><option value="6">June</option><option selected="" value="7">July</option><option value="8">August</option><option value="9">September</option><option value="10">October</option><option value="11">November</option><option value="12">December</option></select>
    <select id="year" name="year"><option selected="" value="2019">2019</option><option value="2020">2020</option></select>
    <div class="error" id="err_date"></div>
    </td>
    </tr>
    <tr>
    <td class="popup_item">Message:</td>
    <td>
    <textarea id="message" name="message" rows="5" style="width: 375px; font-size: 13px;"></textarea>
    </td>
    </tr>
    <tr>
    <td class="popup_item">How did you<br/>find us?</td>
    <td>
    <div style="width: 375px; overflow: hidden; padding-bottom:3px;">
    <div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_1" type="checkbox"/>Referred by my Realtor</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_2" type="checkbox"/>Google</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_3" type="checkbox"/>Facebook</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_4" type="checkbox"/>TV - CP24</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_5" type="checkbox"/>TV - CTV News</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_6" type="checkbox"/>TV - CTV Shark Tank</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_7" type="checkbox"/>Radio - Z103.5</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_8" type="checkbox"/>Radio - Chum FM</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_9" type="checkbox"/>Radio - Edge 92</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_10" type="checkbox"/>Word of Mouth</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_11" type="checkbox"/>Other</div>
    </div>
    </td>
    </tr>
    <tr>
    <td></td>
    <td style="padding-top:20px;">
    <div class="button btn2c btnred" onclick="$m.lead.submit();" style="float:none;">Send Request</div>
    <div class="button btn2c" onclick="$m.lead.close();" style="float:none;">Cancel</div>
    </td>
    </tr>
    </table>
    </td>
    </tr>, <tr>
    <td></td>
    <td id="popup_type" style="font-size: 20px; color: #0654ba; padding-bottom: 20px;"></td>
    </tr>, <tr>
    <td class="popup_item">First Name:</td>
    <td><input name="first_name" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_first_name"></div></td>
    </tr>, <tr>
    <td class="popup_item">Last Name:</td>
    <td><input name="last_name" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_last_name"></div></td>
    </tr>, <tr>
    <td class="popup_item">Email:</td>
    <td><input name="email" style="width: 375px; font-size: 13px;" type="text" value=""/><div class="error" id="err_email"></div></td>
    </tr>, <tr>
    <td class="popup_item">Phone:</td>
    <td><input name="phone" style="width: 200px; font-size: 13px;" type="text" value=""/><div class="error" id="err_phone"></div></td>
    </tr>, <tr id="popup_date">
    <td class="popup_item">Appointment Date:</td>
    <td>
    <select id="day" name="day"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option value="14">14</option><option selected="" value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option><option value="21">21</option><option value="22">22</option><option value="23">23</option><option value="24">24</option><option value="25">25</option><option value="26">26</option><option value="27">27</option><option value="28">28</option><option value="29">29</option><option value="30">30</option><option value="31">31</option></select>
    <select id="month" name="month"><option value="1">January</option><option value="2">February</option><option value="3">March</option><option value="4">April</option><option value="5">May</option><option value="6">June</option><option selected="" value="7">July</option><option value="8">August</option><option value="9">September</option><option value="10">October</option><option value="11">November</option><option value="12">December</option></select>
    <select id="year" name="year"><option selected="" value="2019">2019</option><option value="2020">2020</option></select>
    <div class="error" id="err_date"></div>
    </td>
    </tr>, <tr>
    <td class="popup_item">Message:</td>
    <td>
    <textarea id="message" name="message" rows="5" style="width: 375px; font-size: 13px;"></textarea>
    </td>
    </tr>, <tr>
    <td class="popup_item">How did you<br/>find us?</td>
    <td>
    <div style="width: 375px; overflow: hidden; padding-bottom:3px;">
    <div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_1" type="checkbox"/>Referred by my Realtor</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_2" type="checkbox"/>Google</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_3" type="checkbox"/>Facebook</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_4" type="checkbox"/>TV - CP24</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_5" type="checkbox"/>TV - CTV News</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_6" type="checkbox"/>TV - CTV Shark Tank</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_7" type="checkbox"/>Radio - Z103.5</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_8" type="checkbox"/>Radio - Chum FM</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_9" type="checkbox"/>Radio - Edge 92</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_10" type="checkbox"/>Word of Mouth</div><div style="width:50%;float:left;padding-bottom:1px;"><input name="rs_11" type="checkbox"/>Other</div>
    </div>
    </td>
    </tr>, <tr>
    <td></td>
    <td style="padding-top:20px;">
    <div class="button btn2c btnred" onclick="$m.lead.submit();" style="float:none;">Send Request</div>
    <div class="button btn2c" onclick="$m.lead.close();" style="float:none;">Cancel</div>
    </td>
    </tr>]
    


```python
for row in rows:
    row_td = row.find_all('td')
print(row_td)
type(row_td)
```

    [<td></td>, <td style="padding-top:20px;">
    <div class="button btn2c btnred" onclick="$ml.submit();" style="float:none;">Send Request</div>
    <div class="button btn2c" onclick="$ml.close();" style="float:none;">Cancel</div>
    </td>]
    




    bs4.element.ResultSet




```python
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)
```

    [, 
    Send Request
    Cancel
    ]
    


```python
import re

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
print(clean2)
type(clean2)
```

    [, 
    Send Request
    Cancel
    ]
    




    str




```python
df = pd.DataFrame(list_rows)
df.head(10)
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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[\n\n\n\n\n\n\nbeds\n\nbaths\n\n\n\n\n, \n\n\n...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[, ]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[First Name:, ]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[Last Name:, ]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[Email:, ]</td>
    </tr>
    <tr>
      <th>5</th>
      <td>[Phone:, ]</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[Appointment Date:, \n123456789101112131415161...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>[Message:, \n\n]</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[How did youfind us?, \n\nReferred by my Realt...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>[, \nSend Request\nCancel\n]</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = df[0].str.split(',', expand=True)
df1.head(10)
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[\n\n\n\n\n\n\nbeds\n\nbaths\n\n\n\n\n</td>
      <td>\n\n\n\n\n\n\nFirst Name:\n\n\n\nLast Name:\n...</td>
      <td></td>
      <td></td>
      <td>First Name:</td>
      <td></td>
      <td>Last Name:</td>
      <td></td>
      <td>Email:</td>
      <td></td>
      <td>Phone:</td>
      <td></td>
      <td>Appointment Date:</td>
      <td>\n1234567891011121314151617181920212223242526...</td>
      <td>Message:</td>
      <td>\n\n</td>
      <td>How did youfind us?</td>
      <td>\n\nReferred by my RealtorGoogleFacebookTV - ...</td>
      <td></td>
      <td>\nSend Request\nCancel\n]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[First Name:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[Last Name:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[Email:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>[Phone:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[Appointment Date:</td>
      <td>\n1234567891011121314151617181920212223242526...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>[Message:</td>
      <td>\n\n]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[How did youfind us?</td>
      <td>\n\nReferred by my RealtorGoogleFacebookTV - ...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>9</th>
      <td>[</td>
      <td>\nSend Request\nCancel\n]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1[0] = df1[0].str.strip('[')
df1.head(10)
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>\n\n\n\n\n\n\nbeds\n\nbaths\n\n\n\n\n</td>
      <td>\n\n\n\n\n\n\nFirst Name:\n\n\n\nLast Name:\n...</td>
      <td></td>
      <td></td>
      <td>First Name:</td>
      <td></td>
      <td>Last Name:</td>
      <td></td>
      <td>Email:</td>
      <td></td>
      <td>Phone:</td>
      <td></td>
      <td>Appointment Date:</td>
      <td>\n1234567891011121314151617181920212223242526...</td>
      <td>Message:</td>
      <td>\n\n</td>
      <td>How did youfind us?</td>
      <td>\n\nReferred by my RealtorGoogleFacebookTV - ...</td>
      <td></td>
      <td>\nSend Request\nCancel\n]</td>
    </tr>
    <tr>
      <th>1</th>
      <td></td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>First Name:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Last Name:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Email:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Phone:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Appointment Date:</td>
      <td>\n1234567891011121314151617181920212223242526...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Message:</td>
      <td>\n\n]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>8</th>
      <td>How did youfind us?</td>
      <td>\n\nReferred by my RealtorGoogleFacebookTV - ...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>9</th>
      <td></td>
      <td>\nSend Request\nCancel\n]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
col_labels = soup.find_all('th')
```


```python
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
print(all_header)
```

    ['[]']
    


```python
df2 = pd.DataFrame(all_header)
df2.head()
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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[]</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3 = df2[0].str.split(',', expand=True)
df3.head()
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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[]</td>
    </tr>
  </tbody>
</table>
</div>




```python
frames = [df3, df1]

df4 = pd.concat(frames)
df4.head(10)
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[]</td>
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
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>\n\n\n\n\n\n\nbeds\n\nbaths\n\n\n\n\n</td>
      <td>\n\n\n\n\n\n\nFirst Name:\n\n\n\nLast Name:\n...</td>
      <td></td>
      <td></td>
      <td>First Name:</td>
      <td></td>
      <td>Last Name:</td>
      <td></td>
      <td>Email:</td>
      <td></td>
      <td>Phone:</td>
      <td></td>
      <td>Appointment Date:</td>
      <td>\n1234567891011121314151617181920212223242526...</td>
      <td>Message:</td>
      <td>\n\n</td>
      <td>How did youfind us?</td>
      <td>\n\nReferred by my RealtorGoogleFacebookTV - ...</td>
      <td></td>
      <td>\nSend Request\nCancel\n]</td>
    </tr>
    <tr>
      <th>1</th>
      <td></td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>First Name:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Last Name:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Email:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Phone:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Appointment Date:</td>
      <td>\n1234567891011121314151617181920212223242526...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Message:</td>
      <td>\n\n]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>8</th>
      <td>How did youfind us?</td>
      <td>\n\nReferred by my RealtorGoogleFacebookTV - ...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
df5 = df4.rename(columns=df4.iloc[0])
df5.head()
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
      <th>[]</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[]</td>
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
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>\n\n\n\n\n\n\nbeds\n\nbaths\n\n\n\n\n</td>
      <td>\n\n\n\n\n\n\nFirst Name:\n\n\n\nLast Name:\n...</td>
      <td></td>
      <td></td>
      <td>First Name:</td>
      <td></td>
      <td>Last Name:</td>
      <td></td>
      <td>Email:</td>
      <td></td>
      <td>Phone:</td>
      <td></td>
      <td>Appointment Date:</td>
      <td>\n1234567891011121314151617181920212223242526...</td>
      <td>Message:</td>
      <td>\n\n</td>
      <td>How did youfind us?</td>
      <td>\n\nReferred by my RealtorGoogleFacebookTV - ...</td>
      <td></td>
      <td>\nSend Request\nCancel\n]</td>
    </tr>
    <tr>
      <th>1</th>
      <td></td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>First Name:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Last Name:</td>
      <td>]</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




```python
df5.info()
df5.shape
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 21 entries, 0 to 19
    Data columns (total 20 columns):
    []     21 non-null object
    nan    20 non-null object
    nan    2 non-null object
    nan    2 non-null object
    nan    2 non-null object
    nan    2 non-null object
    nan    2 non-null object
    nan    2 non-null object
    nan    2 non-null object
    nan    2 non-null object
    nan    1 non-null object
    nan    1 non-null object
    nan    1 non-null object
    nan    1 non-null object
    nan    1 non-null object
    nan    1 non-null object
    nan    1 non-null object
    nan    1 non-null object
    nan    1 non-null object
    nan    1 non-null object
    dtypes: object(20)
    memory usage: 3.4+ KB
    




    (21, 20)




```python
df6 = df5.dropna(axis=0, how='any')
```


```python
df7 = df6.drop(df6.index[0])
df7.head()
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
      <th>[]</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
      <th>nan</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python

```


```python

```


```python

```


```python

```
