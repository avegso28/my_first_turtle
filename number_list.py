number_list_o = ["0400", "10660", "12285", "12480", "13118", "13832", "14560", "17045", "17521", "17680", "18200", "18718", "19054", "20839", "21359"]
number_list_1 = []
number_list_2 = []
number_list_3 = []
for number in number_list_o:
    number = int(number)
    if (number % 7 == 0) and (number % 13 == 0):
        number_list_3.append(number)
    elif (number % 7 == 0):
        number_list_1.append(number)
    elif (number % 13 == 0):
        number_list_2.append(number)
    else: 
        print("There is something wrong here")
print(number_list_1)
print(number_list_2)
print(number_list_3)