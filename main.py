"""List and Dictionary Comprehensions."""
"""How to Create Lists using List Comprehension."""
"""For Loop."""
numbers = [1 , 2, 3]
new_list = []
# n-every-index-in-List;
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)
# List Comprehension.
numbersA = [1, 2, 3]
new_list = [n+1 for n in numbersA]
print(new_list)
#List-Compreshension.
name = "Angela"
new_list = [letter for letter in name]
print(new_list)
"""
>>Python-Sequences.
1.List[]
2.Range()
3.String""
4.Tuple()
"""
list_range = [num * 2 for num in range(1, 5)]
print(list_range)
################
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
################
#Using-List-Compreshension.
numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers1 = [ pow(num,2) for num in numbers]
print(squared_numbers1)
squared_numbers2 = [ num**2 for num in numbers]
print(squared_numbers2)
result=[num for num in numbers if num % 2 == 0]
print(result)
"""
with open("file1.txt") as file1:
   file_1_data = file1.readlines() # Convert Lines To List;
with open("file2.txt") as file2:
    file_2_data = file2.readlines() # Convert Lines to List;
result = [int(num) for num in file_1_data if num in file_2_data]
print(result)
"""
############
"""
>>How to use Dictionary Comprehension.
>>Dictionary Comprehension.
new_dict = {new_key : new_value for item in list}
"""
student_score = {
    "Alex":89,
    "Beth":98
}
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
import random
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)
print(students_scores.items())#Key&Value.
#passed_students = {student:score for (student,score) in student_score.items() if score>= 60}
#print(passed_students)
#######################
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
"""
#sentence_List = sentence.split()
# #The split() method splits a string into a list.
#print(sentence_List)
"""
""">>Calculate-Length-of-Every-Word"""
result = {key:len(key) for key in sentence.split()}#in one Line of Code.
print(result)
#######################
print("@"*30)
#To convert temp_c into temp_f:
#(temp_c * 9/5) + 32 = temp_f
weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24
}
weather_f={ key :(value * 9/5) + 32  for key,value in weather_c.items()}
#Dictionary Comprehension one Line of Code.
print(weather_f)
print("$"*30)
#How to Iterate over a Pandas DataFrame.
student_dict = {
    "student" : ["Angela","James","Lily"],
    "score" : [56, 76 , 98]
}
#Looping through dictionaries:
#for (key,value) in student_dict.items():
#    print(value)
import pandas
#Create Pandas Data Frame.
student_data_frame = pandas.DataFrame(student_dict)
#Loop through rows of data frame.
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
def DreamS():
    print("Hello World Dreams")
    # {"ColumnName1":["Value1","Value2","Value3"],
    #  "ColumnName2":["Value1","Value2","Value3"]}
    ahmed_dreams = {"work" : ["Data scientist and Ai","Businessman","chief Executive officer","",""],
                    "country" : ["Usa Austin","Usa San Francisco","Australia Melbourne","KSA","UAE"],
                    "live_country" : ["United states of America","the Commonwealth of Australia","","",""]}
    dreams = pandas.DataFrame(ahmed_dreams)#DataFrame;
    print(dreams) # print pandaDataFrame rows&columns;
    work_list = []
    country_list = []
    live_country_list = []
    #Loop on the index & Rows.
    """
    Append every Column in List;
    """
    for (index,row) in dreams.iterrows():
        work_list.append(row.work)
        country_list.append(row.country)
        live_country_list.append(row.live_country)
    print(work_list)
    print(country_list)
    print(live_country_list)
DreamS() # Call the Function;






