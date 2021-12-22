import csv
dict_case = {}

def main():
    with open ('cases_oct_12.csv', 'r') as input_file:
        cases_data = csv.reader(input_file)
        next(cases_data, None)

        for value in cases_data: # taking cases_oct_12.csv data to then organzie into a dictionary which will be called for in the other functions
            dict_case[value[0]] = [(value[1], value[2], value[3], value[4])]
            for elements in cases_data:
                multi_values = elements[1], elements[2], elements[3], elements[4]
                dict_case.setdefault(elements[0], []).append(multi_values)



        with open('basic_information.txt', 'w') as output_file: # writes the output of all data collected in the case.py file.
            with open('basic_information.txt', 'a') as file: # appends the written sentences to a txt file.
                file.write(f'There were {cases_by_location(dict_case)[0]} cases reported in cases in a London, {cases_by_location(dict_case)[1]} reported in Middlesex County and {cases_by_location(dict_case)[2]} from an unknown location.\n')
                file.write(f'Overall:\n')
                file.write(f'{cases_by_gender(dict_case)[1]} case(s) identified as female.\n')
                file.write(f'{cases_by_gender(dict_case)[0]} case(s) identified as male.\n')
                file.write(f'{cases_by_gender(dict_case)[2]} case(s) identified as non-binary\n')
                file.write(f'{cases_by_gender(dict_case)[3]} case(s) identified as trans man.\n')
                file.write(f'{cases_by_gender(dict_case)[4]} case(s) identified as trans woman.\n')
                file.write(f'{cases_by_gender(dict_case)[5]} case(s) identified as unknown/ prefer not to say.\n')
                file.write(f'\nThe most cases occurred on {most_cases(dict_case)[0]} when there were {most_cases(dict_case)[1]} cases.\n')
                file.write('On that date:\n')

                file.write(f'{cases_by_gender_by_date(most_cases(dict_case)[0], dict_case)[1]} case(s) identified as female.\n')
                file.write(f'{cases_by_gender_by_date(most_cases(dict_case)[0], dict_case)[0]} case(s) identified as male.\n')
                file.write(f'{cases_by_gender_by_date(most_cases(dict_case)[0], dict_case)[2]} case(s) identified as non_binary.\n')
                file.write(f'{cases_by_gender_by_date(most_cases(dict_case)[0], dict_case)[3]} case(s) identified as trans man.\n')
                file.write(f'{cases_by_gender_by_date(most_cases(dict_case)[0], dict_case)[4]} case(s) identified as trans woman.\n')
                file.write(f'{cases_by_gender_by_date(most_cases(dict_case)[0], dict_case)[5]} case(s) identified as unknown/ prefer not to say.\n')

def most_cases(dictionary): # solves for the date of which had the most amount of covid cases.
    Largest_case_date = 0, 0
    for key, value in dictionary.items():
        number_of_cases = len(value)
        if Largest_case_date[1] < number_of_cases:
            Largest_case_date = key, number_of_cases
    return Largest_case_date

def cases_by_location(dictionary): # cases by location uses a for statement to extract information from the dictionary then proceeds with if statements
    london_location = 0
    middlesex_county_location = 0
    unknown_location = 0
    for key, value in dictionary.items():
        for i in value:
            if i[2] == "City of London":
                london_location = london_location + 1
            elif i[2] == "Middlesex County":
                middlesex_county_location = middlesex_county_location + 1
            else:
                unknown_location = unknown_location + 1
    return london_location, middlesex_county_location, unknown_location

def cases_by_gender(dictionary): # organizes and counts individual cases based on gender
    male = 0
    female = 0
    non_binary = 0
    trans_man = 0
    trans_woman = 0
    unknown = 0
    for key, value in dictionary.items(): #If statement cycles through all given genders to then categorize
        for i in value:
            if i[0] == "Male":
                male = male +1
            elif i[0] == 'Female':
                female = female +1
            elif i[0] == "Non-binary":
                non_binary = non_binary +1
            elif i[0] == "Trans man":
                trans_man = trans_man +1
            elif i[0] == "Trans woman":
                trans_woman = trans_woman +1
            else:
                unknown = unknown +1
    return [male, female, non_binary, trans_man, trans_woman, unknown]

def cases_by_gender_by_date(date, dictionary): # cycles through dictionary to organize number of genders who got covid
    gender_cases_dict = {}
    for key, value in dictionary.items():
        if date == key:
            gender_cases_dict[key] = value
    return cases_by_gender(gender_cases_dict)












main()