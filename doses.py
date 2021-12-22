import csv

covid_data_dict = dict()
def main():
    with open('doses_data_oct_12.csv', 'r') as csv_oct_doses:
        csv_doses = csv.reader(csv_oct_doses)
        next(csv_doses, None)
        with open('doses.csv', 'w') as output_file:
            with open('doses.csv', 'a') as file:
                for i in csv_doses:
                    date = i[0]
                    congregate = i[1]
                    other_mobile_clinic = i[2]
                    pharmacies = i[3]
                    primary_care = i[4]
                    mass_immunization = i[5]
                    dose_numbers = [congregate, other_mobile_clinic, pharmacies, primary_care, mass_immunization]
                    covid_data_dict[date] = dose_numbers
                    count_dose_by_date(covid_data_dict)
                    values = count_dose_by_date(covid_data_dict)
                    file.write(values)


def count_dose_by_date(date_list_of_doses):

    for key,value in date_list_of_doses.items():
        for i in range(len(value)):
            if value[i] == "":
                value[i] = 0
        dose_date = key
        congregate = str(value[0]).replace(',', "")
        other_mobile_clinic = str(value[1]).replace(',',"")
        pharmacies = str(value[2]).replace(',',"")
        primary_care = str(value[3]).replace(',',"")
        mass_immunization = str(value[4]).replace(',',"")

        total_weekly_doses = int(congregate) + int(other_mobile_clinic) + int(pharmacies) + int(primary_care) + int(mass_immunization)

    return str(f'{dose_date}, {total_weekly_doses}\n')



main()
