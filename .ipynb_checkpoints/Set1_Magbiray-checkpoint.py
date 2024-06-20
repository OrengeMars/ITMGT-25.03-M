#!/usr/bin/env python
# coding: utf-8

# Savings

# In[20]:


def savings(gross_pay, tax_rate, expenses):
    
    gross_pay = int(gross_pay)
    tax_rate = float(tax_rate)
    expenses = int(expenses)
    
    net_pay = int(gross_pay * (1 - tax_rate)) - expenses
    
    return net_pay

savings(1000, 0.3, 10)




# In[32]:


def material_waste(total_material, material_units, num_jobs, job_consumption):

    total_material = int(total_material)
    material_units = str(material_units)
    num_jobs = int(num_jobs)
    job_consumption = int(job_consumption)

    remaining_material = str(total_material-(num_jobs*job_consumption))
    remaining_material_string = str(remaining_material) + material_units

    return remaining_material_string

material_waste(10000, "kg", 5, 1000)


# In[35]:


def interest(principal, rate, periods):

    principal = int(principal)
    rate = float(rate)
    periods = int(periods)

    final_amount = int((principal*(rate*periods))+principal)

    return final_amount

interest(10000,.1,12)


# In[ ]:




