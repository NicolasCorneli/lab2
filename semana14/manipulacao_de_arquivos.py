import random

#Using write
def generate_random_numbers(amount):
    my_file = open('random-numbers.txt', 'w')
    
    for i in range(amount):
        random_number = random.randint(0, 100)
        my_file.write(str(random_number))
        my_file.write('\n')
        
    my_file.close()

#Using writelines
def generate_random_numbers_writelines(amount):
    content_list = []
    for i in range(amount):
        random_number = random.randint(0,100)
        content_list.append(str(random_number)+ "\n")
    my_file = open("random-numbers.txt" , "w")
    my_file.writelines(content_list)
    my_file.close()

#Using readline + while
def avg_with_readline():
    my_file = open("random-numbers.txt", "r")
    sum_of_numbers = 0
    lines_count = 0
    #Pega a primeira linha
    line = my_file.readline()
    while line != "":
        lines_count = lines_count + 1
        sum_of_numbers = sum_of_numbers + int(line)
        #Pega a próxima linha
        line = my_file.readline()
    my_file.close()
    
    return sum_of_numbers / lines_count

#Using readline + for        
def avg_with_for():
    my_file = open("random-numbers.txt" , "r")
    sum_of_numbers = 0
    lines_count = 0
    for line in my_file:
        lines_count = lines_count + 1
        sum_of_numbers = sum_of_numbers + int(line)
    
    my_file.close()
    return sum_of_numbers / lines_count

#using readlineS
def avg_with_readlines():
    my_file = open("random-numbers.txt", "r")
    lines_list = my_file.readlines()
    sum_of_numbers = 0
    
    for line in lines_list:
        sum_of_numbers = sum_of_numbers + int(line)
        
    return sum_of_numbers / len(lines_list)
        
    my_file.close()

def main():
    #generate_random_numbers(100)
    #generate_random_numbers_writelines(100)
    #avg_with_readline()
    #avg_with_for()
    #avg_with_readlines()
main()
