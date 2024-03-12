1
product_list = []
for x in range(0,6):
    name = input('Mehsulun adi:')
    price = int(input('Mehsulun qiymeti:'))
    product = {'name': name,
               'price': price}
        
    product_list.append([product])
print(product_list)

2
stock_list = []
for x in range(0,3):
    number = input('number name')
    stock_price = int(input('Stock price'))
    stock = {
        'name': number
        'price': stock_price
    }
    stock_list.append([stock_list])
print(stock_list)    
    

3
healthcares = []
for x in range(0,5):
    name = input('patient name')
    age = int(input('patient age'))
    healthcare = {
        'name': name,
        'age': age
        }
    healthcares.append([healthcare])
print(healthcares)    

4
education_list = []
for x in range(0,8):
    name = input('Student name:')
    age = int(input('Student age:'))
    college= {'name': name,
               'price': age}
        
    education_list.append([college])
print(education_list)

5
restaurant_food = []
for x in range(0,4):
    name = input('Food name')
    price = float(input('Food price'))
    restaurant = {
        'name': name,
        'price': price
    }
    restaurant_food.append([restaurant])
print(restaurant_food)

6
technologies = []
for x in range(0,4):
    name = input('Creator name')
    age = int(input('Creator age'))
    programming_language = input('Programing languages')
    technology = {
        'name': name,
        'age': age,
        'program': programming_language
    }
    technologies.append([technology])
print(technologies)  

7
time = 40
time_traveled = 2
vcp = time/time_traveled
print(vcp)

8
movies = []
for x in range(0,4):
    name = input('Film name')
    date = int(input('Date of manufacture'))  
    movie = {
        'name': name,
        'date': date
    }
    movies.append([movie])
print(movies)  

9
Real_estate = []
for x in range(0,4):
    square_meter = int(input('Square meter'))
    square_price = int(input('Square price'))
    realty = {
        'meter': 'square',
        'price': 'square'
    }
    Real_estate.append(realty)
print(Real_estate)    

10
E_commerce = []
for x in range(0,7):
    name = input('Product name')
    price = float(input('Product price'))
    commerce = {
        'name': name,
        'price': price
    }
    E_commerce.append(commerce)
print(E_commerce)    

11
agricultures = []
for x in range(0,2):
        vegetable = input('Vegetable name:')
        price = int(input('Vegetable price:'))
        agriculture = {
                'name': vegetable,
                'price': price
        }
        agricultures.append(agriculture)
print(agricultures)        
        
12
telecommunications = []
for x in range(0,6):
        phone = input('Phone name')
        price = int(input('Phone price'))
        telecommunication = {
                'name': phone,
                'price': price
        }
        telecommunications.append(telecommunication)
print(telecommunications)        

13
tourism_industry = []
for x in range(0,1):
    air_ticket = int(input())
    otel = int(input())
    rent_car = int(input())
    sum_price = air_ticket+otel+rent_car
    total_list = {
        'price_ticket': air_ticket,
        'price_otel': otel,
        'price_car': rent_car
         }
    tourism_industry.append(total_list)

print(tourism_industry)

14
construction_industry = []
wood = int(input('Wood price'))
cement = int(input('Cement price'))
sand = int(input('Sand price'))
iron = int(input('Iron price'))
average = sum(construction_industry)/1
construction_industry.append(average)
print(construction_industry)


numbers = [4, 8, 6, 5, 3, 2]
average = sum(numbers) / len(numbers)
print(average)

import statistics
numbers = [1,2,3,4,5]
average = statistics.mean(numbers)
print(average)    

