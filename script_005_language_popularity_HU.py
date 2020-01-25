import csv
import utils


def calculate_language_popularity_percentage_HU_2011():
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
                if line['What Country or Region do you live in?'] == 'Other Europe':
                    counts['Yes'] += 1
                    for language in language_cells:
                        if line[language] != '':
                            try:
                                language_counter[line[language]] += 1
                            except: 
                                language_counter.update({f'{line[language]}': 1})

    total_active_practitioners = counts['Yes']

    print('Respondents: ', total_active_practitioners)

    # remove rare instances

    for k in list(language_counter.keys()):
        if language_counter[k] < 5:
            del language_counter[k]

    # convert to percentage

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(language_counter)

    utils.write_popular_languages_dictionary_HU_to_file(output_dictionary, 2011)

    print('2011 HU: OK')


def calculate_language_popularity_percentage_HU_2012():
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
                if line['What Country or Region do you live in?'] == 'Other Europe':
                    counts['Yes'] += 1                
                    for language in language_cells:
                        if line[language] != '':
                            try:
                                language_counter[line[language]] += 1
                            except: 
                                language_counter.update({f'{line[language]}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    print('Respondents: ', total_active_practitioners)

    for k in list(language_counter.keys()):
        if language_counter[k] < 5:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(language_counter)

    utils.write_popular_languages_dictionary_HU_to_file(output_dictionary, 2012)

    print('2012 HU: OK')

    

def calculate_language_popularity_percentage_HU_2013():
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
                if line['What Country or Region do you live in?'] == 'Other Europe':
                    counts['Yes'] += 1
                    for language in language_cells:
                        if line[language] != '':
                            try:
                                language_counter[line[language]] += 1
                            except: 
                                language_counter.update({f'{line[language]}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    print('Respondents: ', total_active_practitioners)

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(language_counter)

    utils.write_popular_languages_dictionary_HU_to_file(output_dictionary, 2013)

    print('2013 HU: OK')


def calculate_language_popularity_percentage_HU_2014():
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
                if line['What Country do you live in?'] == 'Hungary':
                    counts['Yes'] += 1                
                    for language in language_cells:
                        if line[language] != '':
                            try:
                                language_counter[line[language]] += 1
                            except: 
                                language_counter.update({f'{line[language]}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    print('Respondents: ', total_active_practitioners)

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(language_counter)

    utils.write_popular_languages_dictionary_HU_to_file(output_dictionary, 2014)

    print('2014 HU: OK')

 
def calculate_language_popularity_percentage_HU_2015():
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
                if line['Country'] == 'Hungary':
                    counts['Yes'] += 1                
                    for language in language_cells:
                        if line[language] != '':
                            try:
                                language_counter[line[language]] += 1
                            except: 
                                language_counter.update({f'{line[language]}': 1})

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    print('Respondents: ', total_active_practitioners)

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(language_counter)

    utils.write_popular_languages_dictionary_HU_to_file(output_dictionary, 2015)

    print('2015 HU: OK')

def calculate_language_popularity_percentage_HU_2016():
    with open('../data/developer_survey_2016/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }
        
        language_counter = {}

        for line in csv_reader:
            if line['self_identification'] != '':
                if line['country'] == 'Hungary':
                    counts['Yes'] += 1                
                    languages = line['tech_do'].split(';')
                    for unstripped_language in languages:
                        language = unstripped_language.strip()
                        try:
                            language_counter[language] += 1
                        except: 
                            language_counter.update({f'{language}': 1})
            else:
                counts['No'] += 1

    # print(language_counter)

    total_active_practitioners = counts['Yes']

    print('Respondents: ', total_active_practitioners)

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(language_counter)

    utils.write_popular_languages_dictionary_HU_to_file(output_dictionary, 2016)

    print('2016 HU: OK')


def calculate_language_popularity_percentage_HU_2017():
    with open('../data/developer_survey_2017/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }

        language_counter = {}

        for line in csv_reader:
            if line['Professional'] == 'None of these':
                counts['No'] += 1
            else:
                if line['Country'] == 'Hungary':
                    counts['Yes'] += 1                
                    languages = line['HaveWorkedLanguage'].split(';')
                    for unstripped_language in languages:
                        language = unstripped_language.strip()
                        try:
                            language_counter[language] += 1
                        except: 
                            language_counter.update({f'{language}': 1})
    
    # print(language_counter)

    total_active_practitioners = counts['Yes']

    print('Respondents: ', total_active_practitioners)

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(language_counter)

    utils.write_popular_languages_dictionary_HU_to_file(output_dictionary, 2017)

    print('2017 HU: OK')


def calculate_language_popularity_percentage_HU_2018():
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
                if line['Country'] == 'Hungary':
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

    print('Respondents: ', total_active_practitioners)

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(language_counter)

    utils.write_popular_languages_dictionary_HU_to_file(output_dictionary, 2018)

    print('2018 HU: OK')


def calculate_language_popularity_percentage_HU_2019():
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
                if line['Country'] == 'Hungary':
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

    print('Respondents: ', total_active_practitioners)

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]


    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(language_counter)

    utils.write_popular_languages_dictionary_HU_to_file(output_dictionary, 2019)

    print('2019 HU: OK')


if __name__ == "__main__":
    calculate_language_popularity_percentage_HU_2011()
    calculate_language_popularity_percentage_HU_2012()
    calculate_language_popularity_percentage_HU_2013()
    calculate_language_popularity_percentage_HU_2014()
    calculate_language_popularity_percentage_HU_2015()
    calculate_language_popularity_percentage_HU_2016()
    calculate_language_popularity_percentage_HU_2017()
    calculate_language_popularity_percentage_HU_2018()
    calculate_language_popularity_percentage_HU_2019()