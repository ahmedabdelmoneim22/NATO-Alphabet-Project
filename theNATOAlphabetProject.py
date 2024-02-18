#print("NATOA Project")
#######################
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#Looping through Dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass
import pandas
student_data_frame = pandas.DataFrame(student_dict)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
import pandas
create_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
#letter_List = []
#code_List = []
#for (index,row) in create_dict.iterrows():
#    letter_List.append(row.letter)
#    code_List.append(row.code)
#print(letter_List)
#print(code_List)
#print(create_dict)
dict_phonetic = { row.letter : row.code for (index,row) in create_dict.iterrows() }
print(dict_phonetic)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [dict_phonetic[letter] for letter in word]
print(output_list)
########################################################
########################################################
