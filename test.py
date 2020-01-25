import csv
import utils



def calculate_language_popularity_percentage_2011():
    with open('../data/developer_survey_2011/survey_results_public.csv') as f:
        csv_reader = csv.DictReader(f)

        counts = {
            'Yes': 0,
            'No': 0,
            'Skip': 0
        }
        
        input_dictionary = {}
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
                            input_dictionary[line[language]] += 1
                        except: 
                            input_dictionary.update({f'{line[language]}': 1})

    total_active_practitioners = counts['Yes']

    # remove rare instances

    for k in list(input_dictionary.keys()):
        if input_dictionary[k] < 5:
            del input_dictionary[k]

    # convert to percentage

    for k in list(input_dictionary.keys()):
        percentage = (input_dictionary[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        input_dictionary[k] = percentage

    output_dictionary = utils.map_data_to_spreadsheet_form(input_dictionary)

    utils.write_popular_languages_dictionary_to_file(output_dictionary, 2011)

    # sorted_output_by_percentage = {k: v for k, v in sorted(output_dictionary.items(), key=lambda item: item[1], reverse=True)}

    # print(sorted_output_by_percentage)


    # with open('results/002_language_popularity.csv', 'w', newline='') as f:
    #     fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
    #         'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
    #         'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
    #         'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
    #         'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
    #         'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
    #         'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
    #         'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
    #         'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
    #         'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerow(td) 


calculate_language_popularity_percentage_2011()
