#!/usr/bin/env python
# coding: utf-8

# In[1]:


totalcost = "What is the total cost of a 4 year college?"
monthsavings = "How much money can you save in a month for this college?"
giftscholar = "How much in additional gift money or scholarship will be given to you?"
futureattend="How many more years until you can attend this college?"
surplusmoney= "How much money more money is needed to attend the college?"
print("Please Answer Following Questions for Average Cost of College:")


# In[2]:


co_st= eval(input(totalcost + ":"))
save_money = eval(input(monthsavings + ":"))
additional_money = eval(input(giftscholar + ":"))
future_years = eval(input(futureattend + ":"))
more_money= eval(input(surplusmoney + ":"))


# In[8]:


avg = (co_st + save_money + additional_money + future_years + more_money) 


# In[7]:


print()
print("College Cost Results: ")
print("Question, Amount")
print(totalcost, ',', co_st)
print(monthsavings, ',', save_money)
print(giftscholar, ',', additional_money)
print(surplusmoney,',', more_money)
print("Average", ':', round(avg)


# In[ ]:




