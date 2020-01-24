import csv


with open('../data/developer_survey_2017/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    language_counter = {}

    for line in csv_reader:
        languages = line['HaveWorkedLanguage'].split(';')
        for unstripped_language in languages:
            language = unstripped_language.strip()
            try:
                language_counter[language] += 1
            except: 
                language_counter.update({f'{language}': 1})
            

print(language_counter)

sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

print(sorted_by_developer_number)        