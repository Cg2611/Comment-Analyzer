#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess

# List of packages to install
packages = ["notebook", "PyQt5", "selenium", "beautifulsoup4", "nltk", "wordcloud", "matplotlib"]

# Install packages one by one
for package in packages:
    subprocess.check_call(["pip", "install", package])


# In[ ]:




