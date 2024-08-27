# types of data types in python is similar to javascript
# str, int, float, bool, list, tuple, set,dict,node
# 

# Strings- the are defines by either single quotation or double quotations.
# you can also create a new string by usint he built-in str() construtor function,
print(str("I am a string"))
# if you want to use string interpolation in string use an f- string 
dog_name="Pupy"
print(f"Say hello to my dog{dog_name}")
# n/b backticks in string for pytho are not valid.
price_1 =3 
price_2= 2.5

print(f"Item 1 costs ${price_1:.2f}")
print(f"Item 2 costs ${price_2:.2f}")

price_3= 12.34567
formated_price= f"{price_1:.3f}"
print(formated_price)
