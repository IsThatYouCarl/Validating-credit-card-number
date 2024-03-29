def valid_or_not(card_number):
   card_number_list = []
   for char in card_number:
       if char.isdigit():
           card_number_list.append(char)
       else:
           continue
   if consecutive_numbers(card_number_list) is True and four_in_a_group(card_number) and within_range(card_number_list) is True and card_number_startswit(card_number) is True and sixteen_digits(card_number_list) is True and hyphen(card_number) is True:
       return True
   else:
       return False
       
def hyphen(card_number):   
    for i in range(len(card_number)):
        if not (card_number[i].isdigit()):
            if card_number[i] == '-' and card_number[i-1].isdigit() and card_number[i+1].isdigit():
                continue
            else:
                return False
                break
        else:
            continue          
    return True    
    
def four_in_a_group(card_number): 
    for num in card_number:
        if num.isdigit():
            continue
        if num == '-':
            groups = card_number.split('-')           
            for group in groups:
                if len(group) != 4:
                    return False 
                else:
                    continue
            return True   
    return True
          
def consecutive_numbers(card_number_list):   
    for j in range(len(card_number_list) - 3):
        if card_number_list[j] == card_number_list[j+1] == card_number_list[j+2] == card_number_list[j+3]:
            return False
            break
        else:
            continue
    return True        
          
def within_range(card_number_list):
    for num in card_number_list:      
        if int(num)<0 or int(num)>9:
            return False
            break   
        else:               
            continue       
    return True
            
def card_number_startswit(card_number):
    if int(card_number[0])==4 or int(card_number[0])==5 or int(card_number[0])==6:
        return True
    else:
        return False    
    
def sixteen_digits(card_number_list):    
    if len(card_number_list) != 16:
        return False      
    else:
        return True
        
n = int(input())

for _ in range(n):
    card_number = input().strip()
    if valid_or_not(card_number) is True:
        print('Valid')
    else:
        print('Invalid')