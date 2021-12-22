import csv

def main():
    with open('doses.csv', 'r') as doses_csv:
        input_doses = csv.reader(doses_csv)
        list_doses = list(input_doses)
    with open('vaccine_stats.txt', 'w') as output_file:
        with open('vaccine_stats.txt', 'a') as file:
            file.write(f'Total: {total_vaccinations(list_doses)}\n')
            file.write(f'Mean: {mean(list_doses)}\n')
            file.write(f'Median: {median(list_doses)}\n')
            file.write(f'Minimum Date: {minimum(list_doses)[0]}, Doses: {minimum(list_doses)[1]}\n')
            file.write(f'Maximum Date: {maximum(list_doses)[0]}, Doses: {maximum(list_doses)[1]}\n')



def minimum(list_doses): # function solves for the minimum value of the dose.csv list
    min_covid_value = int(list_doses[1][1])
    min_data_set = 0
    for i in range(len(list_doses)):
        if int(list_doses[i][1]) <= min_covid_value:
            min_covid_value = int(list_doses[i][1])
            min_data_set = list_doses[i]

    return tuple(min_data_set)

def maximum(list_doses): # returns maximum value in the dose.csv list
    max_covid_value = 0
    max_data_set = 0
    for i in range(len(list_doses)):
        if int(list_doses[i][1]) > max_covid_value:
            max_covid_value = int(list_doses[i][1])
            max_data_set = list_doses[i]
    return tuple(max_data_set)

def total_vaccinations(list_doses): # returns total vaccinations of dose.csv
    total_vacs = 0
    for i in range(len(list_doses)):
        total_vacs = total_vacs + int(list_doses[i][1])
    return total_vacs

def mean(list_doses):
    data_mean = total_vaccinations((list_doses)) / len(list_doses)
    return round(data_mean, 2)

def median(list_doses):
    dose_values = []
    for i in range(len(list_doses)):
        dose_values.append(int(list_doses[i][1]))
    dose_values.sort()

    if len(list_doses) % 2 == 0:
        number1 = dose_values[int(len(list_doses)/2)]
        number2 = dose_values[int(len(list_doses)/2 - 1)]
        median_value = (number1 + number2) / 2
    else:
        median_value = dose_values[int((len(list_doses) - 1) / 2)]
    return median_value


main()