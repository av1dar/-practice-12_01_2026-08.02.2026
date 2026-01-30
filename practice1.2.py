def int_to_string(num):

    if num == 0:
        return "0"
    
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num
    
    result = ""
    while num > 0:
        digit = num % 10         
        char = chr(48 + digit)    
        result = char + result    
        num //= 10                
    
 
    if is_negative:
        result = "-" + result
        
    return result

my_num = 567
string_res = int_to_string(my_num)

print("Число:", my_num)
print("Тип результату:", type(string_res))
print("Рядок у лапках:", f"'{string_res}'")