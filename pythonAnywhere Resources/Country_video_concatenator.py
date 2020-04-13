# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:07:57 2019

@author: Louis Weisz
"""


import pandas as pd
import glob
import re
import numpy as np


path = r'D:\Downloads\Trending-YouTube-Scraper-master\Trending-YouTube-Scraper-master' # use your path
us_files = glob.glob(path + "/*_US_videos.csv")


li = []

'''
Currently the vids are labelled 1-50 in trending rank, 
but it appears the actual list is much longer than this, which
is resuting in duplicate rank values (repeating from 1-50 four times per csv) 
To remedy this, I'm adding a second column called "full_rank" that 
serves uses the index value of each row in a file as a ranking, from 1-200.
THis 
My current theory is that each of these files IS ranked 1-200 in trending, 
but end users only see the top 50. Even if I'm wrong, though, this will still give us
an accurate view of trending rank because the files list the current main trending videos 
first, always. So, we'll be able to see the main trending videos by looking at only those 
with a full_rank value in range 1:50. It also remedies the problem of this "trending_rank"
value not being present in some early files.

I also added the datetime values that I saved in the file names early on 
(bad data practice, I know) to the data table.

'''
#\d*\.\d*\.\d*\.\d*
for filename in us_files:
    df = pd.read_csv(filename, index_col=None, header=0)
                                            #
    datetime = re.search(r'\d*\.\d*\.\d*\.\d*', filename).group(0)  #find the date that I saved in the file name
    df['trending_date'] = datetime                                  #make column "trending_date" and fill it with datetime values
    
    df['full_rank'] = np.arange(len(df)) + 1
    
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True, sort = False)


frame.to_csv( "combined_US_Data.csv", index=False, encoding='utf-8-sig')  #export as a csv

