from selenium import webdriver
import sys
from bs4 import BeautifulSoup
import time
import re
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import codecs
import time

keyword = 'transformer+noise'
T = []
for year in range(2017,2018):
        try:
                print 'Downloading --- ' + keyword + ' ---'
                URL = 'https://scholar.google.com.au/scholar?q={0}&hl=en&as_sdt=1%2C5&authuser=1&as_ylo={1}&as_yhi={2}'.format(keyword, year,year)
                driver = webdriver.Firefox()
                driver.get(URL)
                time.sleep(int(sys.argv[-1]))
                a = driver.find_elements_by_class_name("gs_ab_mdw")[1].text.split(' ')[1]
                num = a.split(',')[0]
                for i in a.split(',')[1:]:
                    num = num + i
                T.append([year,int(num)])
                driver.quit()
                print int(num)
                print '-- trend complete--'
        except:
                driver.quit()
                print   '--- download encounter some problem --- '

T = pd.DataFrame(T, columns = ['Year','Quantity'])
T.to_csv(keyword,index = None)