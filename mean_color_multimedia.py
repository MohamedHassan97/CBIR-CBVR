#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import cv2


# In[76]:







def mean_color(path):

    image=cv2.imread(path)
    average=np.mean(image, axis=(0, 1)) ### de htdek matrix of size 1*3 kol value hya l mean l kol color l 2ola --> R , tanya mean l G 
    average=average.reshape((1,3))
    return average

def similarity_mean_color(query_img_path,list_average):
    
    #x=array_average.shape[0]
    #array_average=array_average.reshape((x,3)) ## 3shan a5le array l average bdl ma hya kda (no.swar,1,3) a5leha (no.swar,3)
    
    avg_query=mean_color(query_img_path)
    cum=[]
    
    for i in range(len(list_average)):
        if(( int(avg_query[0,0]) in range(int((int(list_average[i][0][0]))-(0.7*int(list_average[i][0][0]))), int((0.7*int(list_average[i][0][0]))+(int(list_average[i][0][0])))
           )) and ( int(avg_query[0,1]) in range(int((int(list_average[i][0][1]))-(0.7*int(list_average[i][0][1]))), int((0.7*int(list_average[i][0][1]))+(int(list_average[i][0][1])))
           )) and ( int(avg_query[0,2]) in range(int((int(list_average[i][0][2]))-(0.7*int(list_average[i][0][2]))), int((0.7*int(list_average[i][0][2]))+(int(list_average[i][0][2])))
           ))   ):
            cum.append(i)
            
             
        if(len(cum)==5):
            return cum
        
    return cum
        
        
    


# In[77]:


listt=[*range(200,1000)]
list_cum=[] ######## list have all mean color of all images

for i in range(len(listt)):
        arr=mean_color('C:/Users/AG/Downloads/archive/images/'+str(listt[i])+'.jpg')
        list_cum.append(arr)  


# In[78]:


#################### Testing ############################################



######## code bygrb fekrt l similarity bdelo sora 799 w yrg3 l 5 swar ely 4abho ###############

cum=similarity_mean_color('C:/Users/AG/Downloads/archive/images/799.jpg',list_cum)
list1=[]
for i in range(len(cum)):
    a=cv2.imread('C:/Users/AG/Downloads/archive/images/'+str(cum[i]+200)+'.jpg')
    list1.append(a)
    


# In[79]:


####################### code bydek l 5 swar ely 4abhk ###########################
fig = plt.figure(figsize=(10, 7))
  
# setting values to rows and column variables 
rows = 3
columns = 3
  


  
# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)
  
# showing image
plt.imshow(list1[0])
plt.axis('off')
plt.title("First")
  
# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)
  
# showing image
plt.imshow(list1[1])
plt.axis('off')
plt.title("Second")
  
# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)
  
# showing image
plt.imshow(list1[2])
plt.axis('off')
plt.title("Third")
  
# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 4)
  
# showing image
plt.imshow(list1[3])
plt.axis('off')
plt.title("Fourth")

# Adds a subplot at the 5th position
fig.add_subplot(rows, columns, 5)
  
# showing image
plt.imshow(list1[4])
plt.axis('off')
plt.title("Fifth")


# In[ ]:




