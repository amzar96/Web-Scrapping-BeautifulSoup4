
# coding: utf-8

# In[15]:


import requests
import bs4
from bs4 import BeautifulSoup as soup

url = requests.get('http://shop.abstraxjingga.com/webshaper/store/bestSellers.asp')
soup = soup(url.content, 'html.parser')


# In[2]:


new_arrival = soup.find(id="col1")
#new_arrival = soup.findAll("div", {"class": "newProductsGrid"})
item_name = new_arrival.find_all(class_="prodItemName")
best = item_name[0:3]


# In[3]:


print(best)


# In[4]:


findcat = soup.find(id="col2Left").get_text()


# In[5]:


print(findcat)


# In[6]:


findcat = soup.find(id="col2Left")
find_second_cat = findcat.find(class_="categoryList1 cat-id-82").get_text()


# In[7]:


print(find_second_cat)


# In[16]:

#UPDATE 3 may

new_arrival = soup.findAll("div", {"class": "prodItemName"})
new_arrival2 = soup.findAll("div", {"class": "prodItemPrice"})
    
for x in range (len(new_arrival)):
    name=new_arrival[x].get_text()
    price=new_arrival2[x].get_text()
    print(name+" and price "+price)

