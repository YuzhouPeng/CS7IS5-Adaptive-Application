def final_links(user_model,keywords):
    length=len(user_model)
    keys=0
    if user_model[length-1][1]>0.8:
        keys=7
    elif user_model[length-1][1]>0.7:
        keys=6
    elif user_model[length-1][1]>0.6:
        keys=5
    elif user_model[length-1][1]>0.5:
        keys=4
    elif user_model[length-1][1]>0.4:
        keys=3
    elif user_model[length-1][1]>0.3:
        keys=2
    else:
        keys=1
    
    new_keywords = keywords[:keys]
    multiplier=0
    if user_model[length-2][1]>5:
        multiplier=user_model[2][1]
    else: multiplier = user_model[1][1]
    
    for i in range (len(new_keywords)):
        new_keywords[i][1]=new_keywords[i][1]*multiplier
    
    return(keys,new_keywords)


#I didn't know how to get the data from sql so i created a sample user smodel and key words
sample_usermodel=[['sports',0.78],['music',0.56],['page_number',2],['user',0.33]]
sample_keyword = [['Sachin',0.78],['Cricket',0.66],['Bat',0.53],['Ball',0.51],['Football',0.48],['Rugby',0.33],['Swimming',0.23]]

x = final_links(sample_list,sample_keyword)
print (x)
