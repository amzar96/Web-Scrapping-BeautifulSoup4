
# coding: utf-8

# In[172]:


import requests
import bs4
from bs4 import BeautifulSoup as soup

url = requests.get('http://shop.abstraxjingga.com/webshaper/store/newProducts.asp')
soup = soup(url.content, 'html.parser')


# In[173]:


new_arrival = soup.find(id="col1")
#new_arrival = soup.findAll("div", {"class": "newProductsGrid"})
item_name = new_arrival.find_all(class_="prodItemName")
best = item_name[0:3]


# In[174]:


print(best)


# In[175]:


findcat = soup.find(id="col2Left").get_text()
#ttesting commit

# In[176]:


print(findcat)


# In[177]:


findcat = soup.find(id="col2Left")
find_second_cat = findcat.find(class_="categoryList1 cat-id-82").get_text()


# In[178]:


print(find_second_cat)


# In[218]:


new_arrival = soup.findAll("div", {"class": "prodItemName"})
new_arrival2 = soup.findAll("div", {"class": "prodItemPrice"})
a = new_arrival+new_arrival2


for i in new_arrival:
    itext = i.get_text(" ")
    #print(itext)
    for j in new_arrival2:
        jtext = j.get_text(" ")
        #print(jtext)
    print("Product name : {} and price : {}".format(itext, jtext))

