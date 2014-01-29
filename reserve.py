
# In[148]:

import pandas as pd
import json


# In[149]:

df = pd.read_csv('data/reserve.csv', encoding='utf-8', sep=';')
df['ID_DEPARTEMENT'] = df['ID_DEPARTEMENT'].apply(lambda code: "%01s"%code)


# In[150]:

df.GROUPE_SIGLE.unique()


# Out[150]:

#     array([u'UMP', u'SRC', nan, u'NI', u'RRDP', u'UDI', u'ECOLO', u'GDR'], dtype=object)

# In[151]:

gp = df.groupby(['ID_DEPARTEMENT', 'GROUPE_SIGLE']).MONTANT_SUBVENTION.sum()


# In[152]:

ss = gp.ix['92']


# In[153]:

geojson = json.load(open('data/departments.json'))


# In[154]:

geojson.keys()


# Out[154]:

#     [u'type', u'features']

# In[155]:

for feat in geojson[u'features']:
    dep = feat['properties']['CODE_DEPT']
    if dep in gp.index.get_level_values(0):
        feat['properties']['montant'] = gp[dep].to_dict()
        feat['properties']['montant']['total'] = gp[dep].sum()
    else:
        feat['properties']['montant'] = {'total': 0}


# In[156]:

json.dump(geojson, open('data/departments_with_reserve.json', 'wb'))


# In[157]:

gp


# Out[157]:

#     ID_DEPARTEMENT  GROUPE_SIGLE
#     01              UMP             589855
#     02              RRDP            134000
#                     SRC             369295
#                     UMP             126800
#     03              RRDP            130000
#                     SRC             260000
#     04              SRC             246660
#     05              RRDP            130000
#                     SRC             130000
#     06              UDI             124000
#                     UMP             824541
#     07              SRC             390000
#     08              SRC             130000
#                     UMP             278539
#     09              SRC             258000
#     ...
#     972             SRC             130000
#     973             GDR             140000
#                     SRC             130000
#     974             GDR             130000
#                     RRDP            130000
#                     SRC             644600
#     975             RRDP            170000
#     976             SRC             260195
#     977             UMP             141500
#     986             SRC             146354
#     987             UDI             305859
#     988             UDI             241404
#     999             ECOLO           120000
#                     SRC             873230
#                     UMP             309200
#     Name: MONTANT_SUBVENTION, Length: 230, dtype: int64

# In[ ]:



