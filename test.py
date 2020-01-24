import csv



def calculate_hobbyist_percentage_2019():
    with open('../data/developer_survey_2019/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0
        }

        for line in csv_reader:
            if line['DevType'] == 'NA' or line['DevType'] == '' or line['DevType'] == 'Marketing or sales professional':
                counts['No'] += 1
            else:
                counts['Yes'] += 1

            # try:
            #     if line['DevType'] not in ['Academic researcher', 'Data or business analyst', 'Data scientist or machine learning specialist',
            #                             'Database administrator', 'Designer', 'Developer, back­end', 'Developer, desktop or enterprise applications',
            #                             'Developer, embedded applications or devices', 'Developer, front­end', 'Developer, full­stack',
            #                             'Developer, game or graphics', 'Developer, mobile', 'Developer, QA or test', 'DevOps specialist',
            #                             'Engineer, data', 'Engineer, site reliability', 'Engineering manager', 'Product manager',
            #                             'Scientist', 'Senior Executive (C­Suite, VP, etc.)', 'Student', 'System administrator']:
            #         counts['No'] +=1
            #     else:
            #         counts['Yes'] += 1
            # except:
            #     for element in line['DevType'].split(';'):
            #         if element not in ['Academic researcher', 'Data or business analyst', 'Data scientist or machine learning specialist',
            #                             'Database administrator', 'Designer', 'Developer, back­end', 'Developer, desktop or enterprise applications',
            #                                 'Developer, embedded applications or devices', 'Developer, front­end', 'Developer, full­stack',
            #                                 'Developer, game or graphics', 'Developer, mobile', 'Developer, QA or test', 'DevOps specialist',
            #                                 'Engineer, data', 'Engineer, site reliability', 'Engineering manager', 'Product manager',
            #                                 'Scientist', 'Senior Executive (C­Suite, VP, etc.)', 'Student', 'System administrator']:
            #             counts['No'] += 1
            #             continue
            #         else:
            #             counts['Yes'] += 1


    total = counts['Yes'] + counts['No']

    yes_pct = (counts['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)

    no_pct = (counts['No'] / total) * 100
    no_pct = round(no_pct, 2)

    print(f"2019 Yes: {yes_pct}%")
    print(f"2019 No: {no_pct}%")



calculate_hobbyist_percentage_2019()











# def calculate_language_popularity_percentage_2017():
#     with open('../data/developer_survey_2017/survey_results_public.csv') as f:
#         csv_reader = csv.DictReader(f)

#         counts = {
#             'Yes, I program as a hobby': 0,
#             'Yes, both': 0,
#             'Yes, I contribute to open source projects': 0,
#             'No': 0
#         }

#         language_counter = {}

#         for line in csv_reader:
#             counts[line['ProgramHobby']] += 1
#             if counts[line['ProgramHobby']] != 'No':   # in ['Yes, I program as a hobby', 'Yes, both', 'Yes, I contribute to open source projects']:
#                 languages = line['HaveWorkedLanguage'].split(';')
#                 for unstripped_language in languages:
#                     language = unstripped_language.strip()
#                     try:
#                         language_counter[language] += 1
#                     except: 
#                         language_counter.update({f'{language}': 1})
    
        


#     # print(language_counter)

#     total_active_practitioners = counts['Yes, I program as a hobby'] + counts['Yes, both'] + counts['Yes, I contribute to open source projects']

#     for k in list(language_counter.keys()):
#         if language_counter[k] < 10:
#             del language_counter[k]


#     for k in list(language_counter.keys()):
#         percentage = (language_counter[k]/total_active_practitioners) * 100
#         percentage = round(percentage, 2)
#         print(percentage)
#         language_counter[k] = percentage

#     sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

#     print(sorted_by_developer_number)

# calculate_language_popularity_percentage_2017()