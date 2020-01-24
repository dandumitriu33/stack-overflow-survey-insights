import csv


def calculate_language_popularity_percentage_2011():
    with open('../data/developer_survey_2011/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0,
            'Skip': 0
        }
        
        language_counter = {}
        language_cells = ['lang1', 'lang2', 'lang3', 'lang4', 'lang5', 'lang6', 'lang7', 'lang8', 'lang9', 'lang10', 'lang11', 'lang12']

        question = 'Which of the following best describes your occupation?'
        verification_question = 'How would you best describe the industry you work in?'
        for line in csv_reader:
            if line[verification_question] == '' and line[question] == '':
                counts['Skip'] += 1
            elif line[question] == 'Other' or line[question] == "I don't work in tech" or line[question] == '':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
                for language in language_cells:
                    if line[language] != '':
                        try:
                            language_counter[line[language]] += 1
                        except: 
                            language_counter.update({f'{line[language]}': 1})

    total_active_practitioners = counts['Yes']

    for k in list(language_counter.keys()):
        if language_counter[k] < 5:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)


def calculate_language_popularity_percentage_2012():
    with open('../data/developer_survey_2012/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0,
            'Skip': 0
        }
        
        language_counter = {}
        language_cells = ['lang1', 'lang2', 'lang3', 'lang4', 'lang5', 'lang6', 'lang7', 'lang8', 'lang9', 'lang10', 'lang11', 'lang12', 'lang13', 'lang14']

        question = 'Which of the following best describes your occupation?'
        verification_question = 'How would you best describe the industry you currently work in?'
        for line in csv_reader:
            if line[verification_question] == '' and line[question] == '':
                counts['Skip'] += 1
            elif line[question] == 'Other' or line[question] == "I don't work in tech" or line[question] == '':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
                for language in language_cells:
                    if line[language] != '':
                        try:
                            language_counter[line[language]] += 1
                        except: 
                            language_counter.update({f'{line[language]}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    for k in list(language_counter.keys()):
        if language_counter[k] < 5:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)


def calculate_language_popularity_percentage_2013():
    with open('../data/developer_survey_2013/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0,
            'Skip': 0
        }
        
        language_counter = {}
        language_cells = ['lang1', 'lang2', 'lang3', 'lang4', 'lang5', 'lang6', 'lang7', 'lang8', 'lang9', 'lang10', 'lang11', 'lang12', 'lang13', 'lang14']

        question = 'Which of the following best describes your occupation?'
        verification_question = 'How would you best describe the industry you currently work in?'
        for line in csv_reader:
            if line[verification_question] == '' and line[question] == '':
                counts['Skip'] += 1
            elif line[question] == 'Other' or line[question] == "I don't work in tech" or line[question] == '':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
                for language in language_cells:
                    if line[language] != '':
                        try:
                            language_counter[line[language]] += 1
                        except: 
                            language_counter.update({f'{line[language]}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)


def calculate_language_popularity_percentage_2014():
    with open('../data/developer_survey_2014/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0,
            'Skip': 0
        }
        
        language_counter = {}
        language_cells = ['lang1', 'lang2', 'lang3', 'lang4', 'lang5', 'lang6', 'lang7', 'lang8', 'lang9', 'lang10', 'lang11', 'lang12']

        question = 'Which of the following best describes your occupation?'
        verification_question = 'How would you best describe the industry you currently work in?'
        for line in csv_reader:
            if line[verification_question] == '' and line[question] == '':
                counts['Skip'] += 1
            elif line[question] == 'Other' or line[question] == "I don't work in tech" or line[question] == '':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
                for language in language_cells:
                    if line[language] != '':
                        try:
                            language_counter[line[language]] += 1
                        except: 
                            language_counter.update({f'{line[language]}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)



def calculate_language_popularity_percentage_2015():
    with open('../data/developer_survey_2015/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }
        
        language_counter = {}
        language_cells = ['lang1', 'lang2', 'lang3', 'lang4', 'lang5', 'lang6', 'lang7', 'lang8', 'lang9', 'lang10', 
                          'lang11', 'lang12', 'lang13', 'lang14', 'lang15', 'lang16', 'lang17', 'lang18', 'lang19', 'lang20', 
                          'lang21', 'lang22', 'lang23', 'lang24', 'lang25', 'lang26', 'lang27', 'lang28', 'lang29', 'lang30',
                          'lang31', 'lang32', 'lang33', 'lang34', 'lang35', 'lang36', 'lang37', 'lang38', 'lang39', 'lang40',
                          'lang41', 'lang42', 'lang43']

        for line in csv_reader:
            if line['Tabs or Spaces'] == '' or line['Tabs or Spaces'] == 'Huh?':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
                for language in language_cells:
                    if line[language] != '':
                        try:
                            language_counter[line[language]] += 1
                        except: 
                            language_counter.update({f'{line[language]}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)


def calculate_language_popularity_percentage_2016():
    with open('../data/developer_survey_2016/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }
        
        language_counter = {}

        for line in csv_reader:
            if line['self_identification'] != '':
                counts['Yes'] += 1
                languages = line['tech_do'].split(';')
                for language in languages:
                    try:
                        language_counter[language] += 1
                    except: 
                        language_counter.update({f'{language}': 1})
            else:
                counts['No'] += 1

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)


def calculate_language_popularity_percentage_2017():
    with open('../data/developer_survey_2017/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes, I program as a hobby': 0,
            'Yes, both': 0,
            'Yes, I contribute to open source projects': 0,
            'No': 0
        }

        language_counter = {}

        for line in csv_reader:
            counts[line['ProgramHobby']] += 1
            if counts[line['ProgramHobby']] != 'No':   # in ['Yes, I program as a hobby', 'Yes, both', 'Yes, I contribute to open source projects']:
                languages = line['HaveWorkedLanguage'].split(';')
                for unstripped_language in languages:
                    language = unstripped_language.strip()
                    try:
                        language_counter[language] += 1
                    except: 
                        language_counter.update({f'{language}': 1})
    
    # print(language_counter)

    total_active_practitioners = counts['Yes, I program as a hobby'] + counts['Yes, both'] + counts['Yes, I contribute to open source projects']

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)


def calculate_language_popularity_percentage_2018():
    with open('../data/developer_survey_2018/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }

        language_counter = {}

        for line in csv_reader:
            if line['DevType'] == 'Marketing or sales professional' or line['DevType'] == 'None of the above' or line['DevType'] == '':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
                languages = line['LanguageWorkedWith'].split(';')
                for unstripped_language in languages:
                    language = unstripped_language.strip()
                    try:
                        language_counter[language] += 1
                    except: 
                        language_counter.update({f'{language}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)


def calculate_language_popularity_percentage_2019():
    with open('../data/developer_survey_2019/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }

        language_counter = {}

        for line in csv_reader:
            if line['DevType'] == 'NA' or line['DevType'] == '' or line['DevType'] == 'Marketing or sales professional':
                counts['No'] += 1
            else:
                counts['Yes'] += 1
                languages = line['LanguageWorkedWith'].split(';')
                for unstripped_language in languages:
                    language = unstripped_language.strip()
                    try:
                        language_counter[language] += 1
                    except: 
                        language_counter.update({f'{language}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)


if __name__ == "__main__":
    calculate_language_popularity_percentage_2011()
    calculate_language_popularity_percentage_2012()
    calculate_language_popularity_percentage_2013()
    calculate_language_popularity_percentage_2014()
    calculate_language_popularity_percentage_2015()
    calculate_language_popularity_percentage_2016()
    calculate_language_popularity_percentage_2017()
    calculate_language_popularity_percentage_2018()
    calculate_language_popularity_percentage_2019()