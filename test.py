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

calculate_hobbyist_percentage_2011()