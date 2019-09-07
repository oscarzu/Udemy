# We want the tittle, price, subscribers, reviews, percent of review, length

import csv
import os

udemy_csv= os.path.join(".","resources","web_starter.csv")

title=[]
price=[]
subscribers=[]
reviews=[]
reviews_percent=[]
length=[]

with open(udemy_csv,"r",encoding="UTF-8") as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    # test =next(csvreader) 
    for row in csvreader:
        #Add title
        title.append(row[1])
        #Add Price
        price.append(row[4])
        #Add subscribers
        subscribers.append(row[5])
        #reviews
        reviews.append(row[6])
        #percent of reviews
        percent=round(int(row[6])/int (row[5]),2)
        reviews_percent.append(percent)
        #lenght 
        new_length = (row[9].split(" "))
        length.append(float(new_length[0]))

#print(title)

cleanCsv= zip(title,price,subscribers,reviews,reviews_percent,length)
outputFile= os.path.join("webFinal.csv")

with open(outputFile,"w") as datafile:
    writer= csv.writer(datafile)
    writer.writerow(["Title","Course Price","Subscribers","Reviews","Percent of Reviews","Length of the course"])
    writer.writerows(cleanCsv)
