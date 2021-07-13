'''
This script gets a truncated portion of the dataset for validation(5 lac lines after 10 lac)
'''

import os
file_name = "IndicCorpora/data/en/en.txt"  # PATH TO THE DATASET
text = []
count = 0
with open(file_name) as txt_file:
    for line in txt_file:
        # process the line
        text.append(line)
        count+=1
        if count>=1500000:
            break
text = text[1000000:]
file1 = open("./IndicCorpora/data/en/reduced_data_val.txt","w")
file1.writelines(text)
file1.close()