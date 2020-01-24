import csv


def calculate_hobbyist_percentage_2011():
    with open('../data/developer_survey_2011/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0,
            'Skip': 0
        }
        
        question = 'Which of the following best describes your occupation?'
        verification_question = 'How would you best describe the industry you work in?'
        for line in csv_reader:
            if line[verification_question] == '' and line[question] == '':
                counts['Skip'] += 1
            elif line[question] == 'Other' or line[question] == "I don't work in tech" or line[question] == '':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
            

    total = counts['Yes'] + counts['No']

    yes_pct = (counts['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)

    print(f"2011 Yes: {yes_pct}%")
    print(f"2011 No: {no_pct}%")

    with open('results/001_above_nonindustry_opinion.csv', 'w', newline='') as f:
        fieldnames=['year', 'n=', 'yes', 'no']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'year':2011, 'n=':total, 'yes':yes_pct, 'no':no_pct})



def calculate_hobbyist_percentage_2012():
    with open('../data/developer_survey_2012/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0,
            'Skip': 0
        }
        
        question = 'Which of the following best describes your occupation?'
        verification_question = 'How would you best describe the industry you currently work in?'
        for line in csv_reader:
            if line[verification_question] == '' and line[question] == '':
                counts['Skip'] += 1
            elif line[question] == 'Other' or line[question] == "I don't work in tech" or line[question] == '':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
            

    total = counts['Yes'] + counts['No']

    yes_pct = (counts['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)

    print(f"2012 Yes: {yes_pct}%")
    print(f"2012 No: {no_pct}%")

    with open('results/001_above_nonindustry_opinion.csv', 'a', newline='') as f:
        fieldnames=['year', 'n=', 'yes', 'no']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'year':2012, 'n=':total, 'yes':yes_pct, 'no':no_pct})


def calculate_hobbyist_percentage_2013():
    with open('../data/developer_survey_2013/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0,
            'Skip': 0
        }
        
        question = 'Which of the following best describes your occupation?'
        verification_question = 'How would you best describe the industry you currently work in?'
        for line in csv_reader:
            if line[verification_question] == '' and line[question] == '':
                counts['Skip'] += 1
            elif line[question] == 'Other' or line[question] == "I don't work in tech" or line[question] == '':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
            

    total = counts['Yes'] + counts['No']

    yes_pct = (counts['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)

    print(f"2013 Yes: {yes_pct}%")
    print(f"2013 No: {no_pct}%")

    with open('results/001_above_nonindustry_opinion.csv', 'a', newline='') as f:
        fieldnames=['year', 'n=', 'yes', 'no']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'year':2013, 'n=':total, 'yes':yes_pct, 'no':no_pct})


def calculate_hobbyist_percentage_2014():
    with open('../data/developer_survey_2014/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0,
            'Skip': 0
        }
        
        question = 'Which of the following best describes your occupation?'
        verification_question = 'How would you best describe the industry you currently work in?'
        for line in csv_reader:
            if line[verification_question] == '' and line[question] == '':
                counts['Skip'] += 1
            elif line[question] == 'Other' or line[question] == "I don't work in tech" or line[question] == '':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
            

    total = counts['Yes'] + counts['No']

    yes_pct = (counts['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)

    print(f"2014 Yes: {yes_pct}%")
    print(f"2014 No: {no_pct}%")

    with open('results/001_above_nonindustry_opinion.csv', 'a', newline='') as f:
        fieldnames=['year', 'n=', 'yes', 'no']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'year':2014, 'n=':total, 'yes':yes_pct, 'no':no_pct})


def calculate_hobbyist_percentage_2015():
    with open('../data/developer_survey_2015/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }
        
        for line in csv_reader:
            if line['Tabs or Spaces'] == '' or line['Tabs or Spaces'] == 'Huh?':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
        

    total = counts['Yes'] + counts['No']

    yes_pct = (counts['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)

    print(f"2015 Yes: {yes_pct}%")
    print(f"2015 No: {no_pct}%")

    with open('results/001_above_nonindustry_opinion.csv', 'a', newline='') as f:
        fieldnames=['year', 'n=', 'yes', 'no']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'year':2015, 'n=':total, 'yes':yes_pct, 'no':no_pct})


def calculate_hobbyist_percentage_2016():
    with open('../data/developer_survey_2016/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }
        
        for line in csv_reader:
            if line['self_identification'] != '':
                counts['Yes'] += 1
            else:
                counts['No'] += 1
        

    total = counts['Yes'] + counts['No']

    yes_pct = (counts['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)

    print(f"2016 Yes: {yes_pct}%")
    print(f"2016 No: {no_pct}%")

    with open('results/001_above_nonindustry_opinion.csv', 'a', newline='') as f:
        fieldnames=['year', 'n=', 'yes', 'no']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'year':2016, 'n=':total, 'yes':yes_pct, 'no':no_pct})


def calculate_hobbyist_percentage_2017():
    with open('../data/developer_survey_2017/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes, I program as a hobby': 0,
            'Yes, both': 0,
            'Yes, I contribute to open source projects': 0,
            'No': 0
        }

        for line in csv_reader:
            counts[line['ProgramHobby']] += 1


    total = counts['Yes, I program as a hobby'] + counts['Yes, both'] + counts['Yes, I contribute to open source projects'] + counts['No']

    yes_pct = ((counts['Yes, I program as a hobby'] + counts['Yes, both'] + counts['Yes, I contribute to open source projects']) / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)

    print(f"2017 Yes: {yes_pct}%")
    print(f"2017 No: {no_pct}%")

    with open('results/001_above_nonindustry_opinion.csv', 'a', newline='') as f:
        fieldnames=['year', 'n=', 'yes', 'no']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'year':2017, 'n=':total, 'yes':yes_pct, 'no':no_pct})


def calculate_hobbyist_percentage_2018():
    with open('../data/developer_survey_2018/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }

        for line in csv_reader:
            counts[line['Hobby']] += 1


    total = counts['Yes'] + counts['No']

    yes_pct = (counts['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)


    print(f"2018 Yes: {yes_pct}%")
    print(f"2018 No: {no_pct}%")

    with open('results/001_above_nonindustry_opinion.csv', 'a', newline='') as f:
        fieldnames=['year', 'n=', 'yes', 'no']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'year':2018, 'n=':total, 'yes':yes_pct, 'no':no_pct})



def calculate_hobbyist_percentage_2019():
    with open('../data/developer_survey_2019/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }

        for line in csv_reader:
            counts[line['Hobbyist']] += 1


    total = counts['Yes'] + counts['No']

    yes_pct = (counts['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)

    print(f"2019 Yes: {yes_pct}%")
    print(f"2019 No: {no_pct}%")

    with open('results/001_above_nonindustry_opinion.csv', 'a', newline='') as f:
        fieldnames=['year', 'n=', 'yes', 'no']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'year':2019, 'n=':total, 'yes':yes_pct, 'no':no_pct})
        

if __name__ == "__main__":
    calculate_hobbyist_percentage_2011()
    calculate_hobbyist_percentage_2012()
    calculate_hobbyist_percentage_2013()
    calculate_hobbyist_percentage_2014()
    calculate_hobbyist_percentage_2015()
    calculate_hobbyist_percentage_2016()
    calculate_hobbyist_percentage_2017()
    calculate_hobbyist_percentage_2018()
    calculate_hobbyist_percentage_2019()