
# Sprint 1

## Podcast listeners client base demographic Segmentation

### Motivation
Podcast space is a growing media space. Publishers and advertising agencies have been having a challenge in identifying different segments of listeners within this space. This might be due to the fact the industry is new and data around this industry is scattered and challenging to put together to make a picture of its audience.

### Result
Here we present a research study on podcast listeners data using advanced analytical methods to identify listeners segments. Take Netflix as an example, they are able to segment their user base in a way they can recommend existing content to them or identify what kind of new content to invest in and produce. For us here we attempt to provide something similar. We will provide meaningful insights to help publishers and advertising agencies reach their target audience.

### Research question
What are the various podcast listeners characteristic, trends and demographics segments in the Canadian podcast space?

### Sprint 1
In this sprint we are going to be focusing on exploring our data, conducting data cleaning and getting data to be more readable and ready for exploration

### What is needed
We are going to be using Python as a programing language. We are going to be using the following libararies in Sprint 1:
1. Pandas
2. Numpy

### Summary of Findings
Upon first exploring the data we found that data headers need to be mapped to a dictionary. This was challenging as our raw data set is composed of over 500 columns. So, we had to figure out a way to map both data sets with a function. We used a mapping function to rename all the columns on our raw data set so column names would become more readable.
Second, as we mentioned above, the data is composed of over 500 columns, so we had to do some understanding of the data set and drop columns. Here is what we did:
1.	We dropped all the columns that contain no data what is so ever. This was done by replacing white space with NaN values then dropping all columns of NaNs. With that we were left with 400 columns. Still a lot of columns and a lot of potential of unnecessary data.
2.	We looked at % of NaN on the 400 columns left and then we dropped all columns that contain 50% or less NaN values. This left us with 184 columns. This is more manageable.
3.	After dealing with data set for a period now, we can tell the data is huge and in a very messy complicated format. Data cleaning part is going to be taking longer than expected.
4.	We need to refine our columns mapping from the dictionary to our data set as dictionary column names are split over unknown number of rows which poses a challenge. Either map the 184 data columns manually or figure out a more sophisticated function to map data properly.



```python
import pandas as pd
import numpy as np

# read data to panads 
data = pd.read_csv("C:\\users\\omarh\\downloads\\CSDA 1050 Capstone\\Project\\2018 Data from Jeff\\podcast18.csv") 

# read and convert data schema mapping into pandas
data_schema = pd.read_fwf("C:\\users\\omarh\\downloads\\CSDA 1050 Capstone\\Project\\2018 Data from Jeff\\Dictionary AI058 CdnPodcast 2018 FINALJun16 CLIENT.txt", header = 2)

#dict of mapping drived from data schema file
mapping = {}
# getting unique mapping of varible and lable
data_schema_unique = data_schema.groupby(['Variable', 'Label']).size().reset_index(name='Freq')
# use mapping dict to create a key value pair with varible as key and lable as value
for index, row in data_schema_unique.iterrows():
    if row['Label']:
        mapping[row['Variable']] = row['Label']

# use the mapping dict to rename the varibles of data file with our newly created shchema
data.rename(columns=mapping,inplace=True)

data.head(3);
```


```python
data_schema.head(10)
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
      <th>Variable</th>
      <th>Unnamed: 1</th>
      <th>Position</th>
      <th>Label</th>
      <th>Measurement</th>
      <th>Level</th>
      <th>Role</th>
      <th>Column</th>
      <th>Width</th>
      <th>Alignment</th>
      <th>Print</th>
      <th>Format</th>
      <th>Write</th>
      <th>Format.1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>study</td>
      <td>NaN</td>
      <td>1</td>
      <td>STUDY IDENTIFICATION</td>
      <td>Nominal</td>
      <td>NaN</td>
      <td>Input</td>
      <td>26</td>
      <td>NaN</td>
      <td>Left</td>
      <td>A75</td>
      <td>NaN</td>
      <td>A75</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>id</td>
      <td>NaN</td>
      <td>2</td>
      <td>RESPONDENT ID</td>
      <td>Scale</td>
      <td>NaN</td>
      <td>Input</td>
      <td>10</td>
      <td>NaN</td>
      <td>Right</td>
      <td>F8</td>
      <td>NaN</td>
      <td>F8</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>(99999999)</td>
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
      <th>3</th>
      <td>twave</td>
      <td>NaN</td>
      <td>3</td>
      <td>WAVE (DEFAULT 1)</td>
      <td>Nominal</td>
      <td>NaN</td>
      <td>Input</td>
      <td>10</td>
      <td>NaN</td>
      <td>Right</td>
      <td>F8</td>
      <td>NaN</td>
      <td>F8</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>arfrr</td>
      <td>NaN</td>
      <td>4</td>
      <td>arfrr .REGION ROLLUP</td>
      <td>Nominal</td>
      <td>NaN</td>
      <td>Input</td>
      <td>10</td>
      <td>NaN</td>
      <td>Right</td>
      <td>F1</td>
      <td>NaN</td>
      <td>F1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>arfpr</td>
      <td>NaN</td>
      <td>5</td>
      <td>arfpr .PROVINCE</td>
      <td>Nominal</td>
      <td>NaN</td>
      <td>Input</td>
      <td>10</td>
      <td>NaN</td>
      <td>Right</td>
      <td>F2</td>
      <td>NaN</td>
      <td>F2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>ROLLUP</td>
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
      <th>7</th>
      <td>arfgen</td>
      <td>NaN</td>
      <td>6</td>
      <td>arfgen .GENDER</td>
      <td>Nominal</td>
      <td>NaN</td>
      <td>Input</td>
      <td>10</td>
      <td>NaN</td>
      <td>Right</td>
      <td>F1</td>
      <td>NaN</td>
      <td>F1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>arfagerf</td>
      <td>NaN</td>
      <td>7</td>
      <td>arfagerf .AGE ROLLUP</td>
      <td>Ordinal</td>
      <td>NaN</td>
      <td>Input</td>
      <td>10</td>
      <td>NaN</td>
      <td>Right</td>
      <td>F1</td>
      <td>NaN</td>
      <td>F1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>FINE</td>
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
  </tbody>
</table>
</div>




```python
#data.groupby(['arfpr .PROVINCE','arfgen .GENDER','qs2g .FREQUENCY-']).size().reset_index(name='counts');
```


```python
#data transformation test
#pd.get_dummies(data, columns=['qs2g .FREQUENCY-']);
```


```python
data.describe()
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
      <th>RESPONDENT ID</th>
      <th>WAVE (DEFAULT 1)</th>
      <th>qp10aa .PROPORTION-</th>
      <th>qp10ab .PROPORTION-</th>
      <th>qp10ac .PROPORTION-</th>
      <th>qp10ad .PROPORTION-</th>
      <th>qp10ae .PROPORTION-</th>
      <th>qp10af .PROPORTION-</th>
      <th>qe1ba .%BY MYSELF</th>
      <th>qe1bb .%WITH OTHERS</th>
      <th>...</th>
      <th>qe9ba .PROPORTION-</th>
      <th>qe9bb .PROPORTION-</th>
      <th>qe9bc .PROPORTION-</th>
      <th>qe9bd .PROPORTION-</th>
      <th>qm4a .INTEREST1 IN</th>
      <th>QA1_Advertising_Podcast_1_Code</th>
      <th>&lt;none&gt;</th>
      <th>&lt;none&gt;</th>
      <th>&lt;none&gt;</th>
      <th>FINAL WEIGHT VARIABLE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1.534000e+03</td>
      <td>1534.0</td>
      <td>1534.000000</td>
      <td>1534.000000</td>
      <td>1534.000000</td>
      <td>1534.000000</td>
      <td>1534.000000</td>
      <td>1534.0</td>
      <td>1534.000000</td>
      <td>1534.000000</td>
      <td>...</td>
      <td>1534.000000</td>
      <td>1534.000000</td>
      <td>1534.000000</td>
      <td>1534.0</td>
      <td>1534.0</td>
      <td>1534.000000</td>
      <td>1534.0</td>
      <td>1534.000000</td>
      <td>1534.000000</td>
      <td>1534.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.764778e+06</td>
      <td>201806.0</td>
      <td>40.881356</td>
      <td>48.548240</td>
      <td>5.188396</td>
      <td>1.526728</td>
      <td>3.855280</td>
      <td>100.0</td>
      <td>88.761408</td>
      <td>11.238592</td>
      <td>...</td>
      <td>30.422425</td>
      <td>20.563233</td>
      <td>49.014342</td>
      <td>100.0</td>
      <td>10001.0</td>
      <td>561.456975</td>
      <td>1.0</td>
      <td>332.187744</td>
      <td>450.526076</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>6.124486e+04</td>
      <td>0.0</td>
      <td>36.663634</td>
      <td>38.015034</td>
      <td>13.830739</td>
      <td>6.710703</td>
      <td>12.003584</td>
      <td>0.0</td>
      <td>24.403312</td>
      <td>24.403312</td>
      <td>...</td>
      <td>35.732465</td>
      <td>27.665689</td>
      <td>40.861864</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>477.692169</td>
      <td>0.0</td>
      <td>446.958090</td>
      <td>478.861020</td>
      <td>0.719400</td>
    </tr>
    <tr>
      <th>min</th>
      <td>5.691168e+06</td>
      <td>201806.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>100.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>100.0</td>
      <td>10001.0</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>0.220207</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.701247e+06</td>
      <td>201806.0</td>
      <td>1.000000</td>
      <td>10.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>100.0</td>
      <td>91.250000</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>100.0</td>
      <td>10001.0</td>
      <td>34.000000</td>
      <td>1.0</td>
      <td>24.000000</td>
      <td>34.000000</td>
      <td>0.576557</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.755331e+06</td>
      <td>201806.0</td>
      <td>33.000000</td>
      <td>50.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
      <td>0.000000</td>
      <td>...</td>
      <td>15.000000</td>
      <td>10.000000</td>
      <td>47.000000</td>
      <td>100.0</td>
      <td>10001.0</td>
      <td>997.000000</td>
      <td>1.0</td>
      <td>47.000000</td>
      <td>53.000000</td>
      <td>0.807918</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5.834686e+06</td>
      <td>201806.0</td>
      <td>72.000000</td>
      <td>90.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
      <td>8.750000</td>
      <td>...</td>
      <td>53.000000</td>
      <td>30.000000</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>10001.0</td>
      <td>998.000000</td>
      <td>1.0</td>
      <td>999.000000</td>
      <td>999.000000</td>
      <td>1.260848</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.861023e+06</td>
      <td>201806.0</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>...</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>10001.0</td>
      <td>999.000000</td>
      <td>1.0</td>
      <td>999.000000</td>
      <td>999.000000</td>
      <td>7.626968</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 36 columns</p>
</div>




```python
data.shape
```




    (1534, 584)




```python
#replace all whitespace with NaN values
data.replace(' ', np.nan, inplace=True)
```


```python
data.dropna(axis = 1, how= 'all', inplace = True)
```


```python
data.shape
```




    (1534, 400)




```python
#viewing columns by % of NaN values
print (data.isnull().mean() * 100)
```

    STUDY IDENTIFICATION               0.000000
    RESPONDENT ID                      0.000000
    WAVE (DEFAULT 1)                   0.000000
    arfrr .REGION ROLLUP               0.000000
    arfpr .PROVINCE                    0.000000
    arfgen .GENDER                     0.000000
    arfagerf .AGE ROLLUP               0.000000
    arfracea .RACE1                   58.279009
    arfraceb .RACE2                   86.505867
    arfracec .RACE3                   67.014342
    arfraced .RACE4                   95.371578
    arfracee .RACE5                   58.083442
    arfracef .RACE6                   98.239896
    arfraceg .RACE7                   98.891786
    arfraceh .RACE8                   98.109518
    arfracei .RACE9                   98.370274
    arfracej .RACE10                  96.675359
    arfracek .RACE11                  93.611473
    arfracel .RACE12                  96.936115
    arfracem .RACE13                  99.674055
    arfracen .RACE14                  96.870926
    arfraceo .RACE15                  97.522816
    arfhhs .HOUSEHOLD                  0.000000
    r entirely responsibl              0.000000
    r entirely responsibl              0.000000
    r entirely responsibl              0.000000
    arfkid .KIDS IN HH                 0.000000
    arfeduc .HIGHEST                   0.000000
    lf-employed full-time              0.000000
    k                                  0.000000
                                        ...    
    PanelistCulture                    0.000000
    <none>                             9.517601
    PRIMARY                           10.299870
    V455_A                            10.299870
    QA1_Advertising_Podcast_1_Code     0.000000
    QA1_Advertising_Podcast_2_Code    54.041721
    QA1_Advertising_Podcast_3_Code    59.647979
    QA2c_code_1                       63.168188
    QA2c_code_2                       98.174707
    <none>                             0.000000
    COMPLETED INTERVIEW                0.000000
    qp1c .COMBINED TIME                0.000000
    <none>                            98.109518
    qp5cnm_neth                       99.674055
    qp5dnm_neth                       99.543677
    qp5cdnm_neth                      99.282920
    <none>                             0.000000
    <none>                             0.000000
    <none>                             0.000000
    <none>                             0.000000
    base                               0.000000
    COUNT OF PODCASTS                  0.000000
    <none>                            83.376793
    <none>                            95.371578
    <none>                            99.348110
    <none>                            21.512386
    FINAL WEIGHT VARIABLE              0.000000
    arfgen & AGE WGT CATS              0.000000
    EDUCATION WGT CATS                 0.000000
    REGION WGT CATS                    0.000000
    Length: 400, dtype: float64
    


```python
data.isna().sum();
```


```python
#print(data.isnull().mean() <= 0.5);
```


```python
#drop columns with 50% NaN or more
data = data.loc[:, data.isnull().mean() <= .5]
```


```python
data.shape
```




    (1534, 184)




```python
#verify
print (data.isnull().mean() * 100);
```
