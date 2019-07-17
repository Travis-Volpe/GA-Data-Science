'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv
#import pandas as pd
# specify that the delimiter is a tab character
# make sure that the path in Spyder (top right hand corner) is set to to dataset folder
with open('chipotle.tsv', 'rU') as f:
    data = [row for row in csv.reader(f, delimiter='\t')]


#file_nested_list = pd.read_csv(r'chipotle.tsv', delimiter='\t')

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

#'order_id', 'quantity', 'item_name', 'choice_description',
#       'item_price'


header = data[0]
header

data = data[1:]
data


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
#file_nested_list.item_price.mean()

#file_nested_list['item_price'] = file_nested_list.item_price.astype('float')

price = [row[4] for row in data] 
price

price = [row[4].replace('$', '') for row in data]
price

#Couldn't get convert string to float to work
list(map(float, row[4].split("*")))

price_sum = [float(price) for price in row[4].split("*")] 

price_sum = sum([float(row[4][1:]) for row in data]) 
price_sum 

quantity = [row[1] for row in data] 
quantity

quantity_sum = sum([int(row[1][1:]) for row in data]) 
quantity_sum

price_avg = price_sum / quantity_sum
price_avg


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''


#file_nested_list.groupby('choice_description').choice_description.count()

#file_nested_list.groupby('item_name').item_name.count()

# item_name = Canned Soda or Canned Soft Drink
#canned = file_nested_list[(file_nested_list.values  == "Canned Soda")|(file_nested_list.values  == "Canned Soft Drink " ) ]

#canned.groupby('choice_description').choice_description.count()

canned_items = set([row[2] for row in data])
canned_items

canned_items = []
for row in data:
    if 'Canned' in row[2]:
        canned_items.append(row)

sodas = set([row[3][1:-1] for row in data if 'Canned' in row[2]])   
sodas


'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
#burritos = file_nested_list[(file_nested_list.values  == "Burrito")]
#burritos.groupby('choice_description').choice_description.count()
#burritos.groupby('item_name').item_name.count()

#dfToList = burritos['choice_description'].tolist()

#output = []
#for d in dfToList:
#    output.count(d)
#print(output)
#    
#
#burrito_toppings = burritos.groupby('choice_description').sum() 


burritos = 0
for row in data:
    if 'Burrito' in row[2]:
        burritos += 1 
burritos

toppings = 0
for row in data:
    if 'Burrito' in row[2]:
        toppings += (row[3].count(',') + 1)
toppings

avg_tops_per_burrito = toppings / burritos

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''


'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
