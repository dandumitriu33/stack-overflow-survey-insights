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

    # remove rare instances

    for k in list(language_counter.keys()):
        if language_counter[k] < 5:
            del language_counter[k]

    # adjust for duplicates

    for k in list(language_counter.keys()):
        if k in ['vb.net', 'VB.Net']:
            language_counter['VB.NET'] += language_counter[k]
            del language_counter[k]
        if k in ['Objective C', 'objective-c']:
            language_counter['Objective-C'] += language_counter[k]
            del language_counter[k]

    # convert to percentage

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)

    td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
        'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
        'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
        'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
        'jQuery': 0, 'shell': 0}

    for k in sorted_by_developer_number:
        if k in td:
            td[k] = sorted_by_developer_number[k]
        if k == 'bash':
            td['Bash'] += sorted_by_developer_number[k]
        if k == 'Ocaml':
            td['Ocaml'] += sorted_by_developer_number[k]
        if k == 'Sharepoint':
            td['Sharepoint'] += sorted_by_developer_number[k]

    with open('results/002_language_popularity.csv', 'w', newline='') as f:
        fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(td) 


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

    # adjust for duplicates

    for k in list(language_counter.keys()):
        if k in ['vb.net', 'VB.Net', 'VB.net']:
            language_counter['VB.NET'] += language_counter[k]
            del language_counter[k]
        if k in ['Objective C', 'objective-c']:
            language_counter['Objective-C'] += language_counter[k]
            del language_counter[k]
        if k in ['groovy']:
            language_counter['Groovy'] += language_counter[k]
            del language_counter[k]
        if k in ['MATLAB', 'Matlab']:
            language_counter['Matlab'] += language_counter[k]
            del language_counter[k]
        if k in ['Actionscript', 'Actionscript 3']:
            language_counter['ActionScript'] += language_counter[k]
            del language_counter[k]
        if k in ['scala']:
            language_counter['Scala'] += language_counter[k]
            del language_counter[k]
        if k in ['Coldfusion']:
            language_counter['ColdFusion'] += language_counter[k]
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)

    td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
        'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
        'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
        'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
        'jQuery': 0, 'shell': 0}

    for k in sorted_by_developer_number:
        if k in td:
            td[k] = sorted_by_developer_number[k]
        if k == 'bash':
            td['Bash'] += sorted_by_developer_number[k]
        if k == 'Ocaml':
            td['Ocaml'] += sorted_by_developer_number[k]
        if k == 'Sharepoint':
            td['Sharepoint'] += sorted_by_developer_number[k]

    with open('results/002_language_popularity.csv', 'a', newline='') as f:
        fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(td) 


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

    # adjust for duplicates

    for k in list(language_counter.keys()):
        if k in ['vb.net', 'VB.Net', 'VB.net']:
            language_counter['VB.NET'] += language_counter[k]
            del language_counter[k]
        if k in ['Objective C', 'objective-c']:
            language_counter['Objective-C'] += language_counter[k]
            del language_counter[k]
        if k in ['groovy']:
            language_counter['Groovy'] += language_counter[k]
            del language_counter[k]
        if k in ['MATLAB', 'Matlab']:
            language_counter['Matlab'] += language_counter[k]
            del language_counter[k]
        if k in ['Actionscript', 'Actionscript 3']:
            language_counter['ActionScript'] += language_counter[k]
            del language_counter[k]
        if k in ['scala']:
            language_counter['Scala'] += language_counter[k]
            del language_counter[k]
        if k in ['Coldfusion']:
            language_counter['ColdFusion'] += language_counter[k]
            del language_counter[k]
        if k in ['bash']:
            language_counter['Bash'] += language_counter[k]
            del language_counter[k]
        if k in ['clojure']:
            language_counter['Clojure'] += language_counter[k]
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)

    td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
        'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
        'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
        'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
        'jQuery': 0, 'shell': 0}

    for k in sorted_by_developer_number:
        if k in td:
            td[k] = sorted_by_developer_number[k]
        if k == 'bash':
            td['Bash'] += sorted_by_developer_number[k]
        if k == 'Ocaml':
            td['Ocaml'] += sorted_by_developer_number[k]
        if k == 'Sharepoint':
            td['Sharepoint'] += sorted_by_developer_number[k]

    with open('results/002_language_popularity.csv', 'a', newline='') as f:
        fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(td) 


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


    # adjust for duplicates

    for k in list(language_counter.keys()):
        if k in ['vb.net', 'VB.Net', 'VB.net']:
            language_counter['VB.NET'] += language_counter[k]
            del language_counter[k]
        if k in ['Objective C', 'objective-c']:
            language_counter['Objective-C'] += language_counter[k]
            del language_counter[k]
        if k in ['groovy']:
            language_counter['Groovy'] += language_counter[k]
            del language_counter[k]
        if k in ['MATLAB', 'Matlab']:
            language_counter['Matlab'] += language_counter[k]
            del language_counter[k]
        if k in ['Actionscript', 'Actionscript 3']:
            language_counter['ActionScript'] += language_counter[k]
            del language_counter[k]
        if k in ['scala']:
            language_counter['Scala'] += language_counter[k]
            del language_counter[k]
        if k in ['Coldfusion']:
            language_counter['ColdFusion'] += language_counter[k]
            del language_counter[k]
        # if k in ['bash']:
        #     language_counter['Bash'] += language_counter[k]
        #     del language_counter[k]
        if k in ['clojure']:
            language_counter['Clojure'] += language_counter[k]
            del language_counter[k]
        if k in ['perl']:
            language_counter['perl'] += language_counter[k]
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)

    td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
        'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
        'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
        'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
        'jQuery': 0, 'shell': 0}

    for k in sorted_by_developer_number:
        if k in td:
            td[k] = sorted_by_developer_number[k]
        if k == 'bash':
            td['Bash'] += sorted_by_developer_number[k]
        if k == 'Ocaml':
            td['Ocaml'] += sorted_by_developer_number[k]
        if k == 'Sharepoint':
            td['Sharepoint'] += sorted_by_developer_number[k]

    with open('results/002_language_popularity.csv', 'a', newline='') as f:
        fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(td) 



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

    # adjust for duplicates

    for k in list(language_counter.keys()):
        if k in ['vb.net', 'VB.Net', 'VB.net']:
            language_counter['VB.NET'] += language_counter[k]
            del language_counter[k]
        if k in ['Objective C', 'objective-c']:
            language_counter['Objective-C'] += language_counter[k]
            del language_counter[k]
        if k in ['groovy']:
            language_counter['Groovy'] += language_counter[k]
            del language_counter[k]
        if k in ['MATLAB', 'Matlab']:
            language_counter['Matlab'] += language_counter[k]
            del language_counter[k]
        if k in ['Actionscript', 'Actionscript 3', 'Action Script']:
            language_counter['ActionScript'] += language_counter[k]
            del language_counter[k]
        if k in ['scala']:
            language_counter['Scala'] += language_counter[k]
            del language_counter[k]
        if k in ['Coldfusion']:
            language_counter['ColdFusion'] += language_counter[k]
            del language_counter[k]
        if k in ['bash']:
            language_counter['Bash'] += language_counter[k]
            del language_counter[k]
        if k in ['clojure']:
            language_counter['Clojure'] += language_counter[k]
            del language_counter[k]
        if k in ['perl']:
            language_counter['perl'] += language_counter[k]
            del language_counter[k]
        if k in ['Typescript']:
            language_counter['TypeScript'] += language_counter[k]
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)

    td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
        'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
        'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
        'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
        'jQuery': 0, 'shell': 0}

    for k in sorted_by_developer_number:
        if k in td:
            td[k] = sorted_by_developer_number[k]
        if k == 'bash':
            td['Bash'] += sorted_by_developer_number[k]
        if k == 'Ocaml':
            td['Ocaml'] += sorted_by_developer_number[k]
        if k == 'Sharepoint':
            td['Sharepoint'] += sorted_by_developer_number[k]

    with open('results/002_language_popularity.csv', 'a', newline='') as f:
        fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(td) 


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

    for k in list(language_counter.keys()):
        if language_counter[k] < 10:
            del language_counter[k]

    # adjust for duplicates

    for k in list(language_counter.keys()):
        if k in ['vb.net', 'VB.Net', 'VB.net']:
            language_counter['VB.NET'] += language_counter[k]
            del language_counter[k]
        if k in ['Objective C', 'objective-c']:
            language_counter['Objective-C'] += language_counter[k]
            del language_counter[k]
        if k in ['groovy']:
            language_counter['Groovy'] += language_counter[k]
            del language_counter[k]
        if k in ['MATLAB', 'Matlab']:
            language_counter['Matlab'] += language_counter[k]
            del language_counter[k]
        if k in ['Actionscript', 'Actionscript 3', 'Action Script']:
            language_counter['ActionScript'] += language_counter[k]
            del language_counter[k]
        if k in ['scala']:
            language_counter['Scala'] += language_counter[k]
            del language_counter[k]
        if k in ['Coldfusion']:
            language_counter['ColdFusion'] += language_counter[k]
            del language_counter[k]
        if k in ['bash']:
            language_counter['Bash'] += language_counter[k]
            del language_counter[k]
        if k in ['clojure']:
            language_counter['Clojure'] += language_counter[k]
            del language_counter[k]
        if k in ['perl']:
            language_counter['perl'] += language_counter[k]
            del language_counter[k]
        if k in ['Typescript']:
            language_counter['TypeScript'] += language_counter[k]
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)

    td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
        'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
        'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
        'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
        'jQuery': 0, 'shell': 0}

    for k in sorted_by_developer_number:
        if k in td:
            td[k] = sorted_by_developer_number[k]
        if k == 'bash':
            td['Bash'] += sorted_by_developer_number[k]
        if k == 'Ocaml':
            td['Ocaml'] += sorted_by_developer_number[k]
        if k == 'Sharepoint':
            td['Sharepoint'] += sorted_by_developer_number[k]

    with open('results/002_language_popularity.csv', 'a', newline='') as f:
        fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(td) 


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

    # adjust for duplicates

    for k in list(language_counter.keys()):
        if k in ['vb.net', 'VB.Net', 'VB.net']:
            language_counter['VB.NET'] += language_counter[k]
            del language_counter[k]
        if k in ['Objective C', 'objective-c']:
            language_counter['Objective-C'] += language_counter[k]
            del language_counter[k]
        if k in ['groovy']:
            language_counter['Groovy'] += language_counter[k]
            del language_counter[k]
        if k in ['MATLAB', 'Matlab']:
            language_counter['Matlab'] += language_counter[k]
            del language_counter[k]
        if k in ['Actionscript', 'Actionscript 3', 'Action Script']:
            language_counter['ActionScript'] += language_counter[k]
            del language_counter[k]
        if k in ['scala']:
            language_counter['Scala'] += language_counter[k]
            del language_counter[k]
        if k in ['Coldfusion']:
            language_counter['ColdFusion'] += language_counter[k]
            del language_counter[k]
        if k in ['bash']:
            language_counter['Bash'] += language_counter[k]
            del language_counter[k]
        if k in ['clojure']:
            language_counter['Clojure'] += language_counter[k]
            del language_counter[k]
        if k in ['perl']:
            language_counter['perl'] += language_counter[k]
            del language_counter[k]
        if k in ['Typescript']:
            language_counter['TypeScript'] += language_counter[k]
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)

    td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
        'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
        'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
        'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
        'jQuery': 0, 'shell': 0}

    for k in sorted_by_developer_number:
        if k in td:
            td[k] = sorted_by_developer_number[k]
        if k == 'bash':
            td['Bash'] += sorted_by_developer_number[k]
        if k == 'Ocaml':
            td['Ocaml'] += sorted_by_developer_number[k]
        if k == 'Sharepoint':
            td['Sharepoint'] += sorted_by_developer_number[k]

    with open('results/002_language_popularity.csv', 'a', newline='') as f:
        fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(td) 


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

    # adjust for duplicates

    for k in list(language_counter.keys()):
        if k in ['vb.net', 'VB.Net', 'VB.net']:
            language_counter['VB.NET'] += language_counter[k]
            del language_counter[k]
        if k in ['Objective C', 'objective-c']:
            language_counter['Objective-C'] += language_counter[k]
            del language_counter[k]
        if k in ['groovy']:
            language_counter['Groovy'] += language_counter[k]
            del language_counter[k]
        if k in ['MATLAB', 'Matlab']:
            language_counter['Matlab'] += language_counter[k]
            del language_counter[k]
        if k in ['Actionscript', 'Actionscript 3', 'Action Script']:
            language_counter['ActionScript'] += language_counter[k]
            del language_counter[k]
        if k in ['scala']:
            language_counter['Scala'] += language_counter[k]
            del language_counter[k]
        if k in ['Coldfusion']:
            language_counter['ColdFusion'] += language_counter[k]
            del language_counter[k]
        if k in ['bash']:
            language_counter['Bash'] += language_counter[k]
            del language_counter[k]
        if k in ['clojure']:
            language_counter['Clojure'] += language_counter[k]
            del language_counter[k]
        if k in ['perl']:
            language_counter['perl'] += language_counter[k]
            del language_counter[k]
        if k in ['Typescript']:
            language_counter['TypeScript'] += language_counter[k]
            del language_counter[k]

    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)

    td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
        'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
        'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
        'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
        'jQuery': 0, 'shell': 0}

    for k in sorted_by_developer_number:
        if k in td:
            td[k] = sorted_by_developer_number[k]
        if k == 'bash':
            td['Bash'] += sorted_by_developer_number[k]
        if k == 'Ocaml':
            td['OCaml'] += sorted_by_developer_number[k]
        if k == 'Sharepoint':
            td['SharePoint'] += sorted_by_developer_number[k]

    with open('results/002_language_popularity.csv', 'a', newline='') as f:
        fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(td) 


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


    # adjust for duplicates

    for k in list(language_counter.keys()):
        if k in ['vb.net', 'VB.Net', 'VB.net']:
            language_counter['VB.NET'] += language_counter[k]
            del language_counter[k]
        if k in ['Objective C', 'objective-c']:
            language_counter['Objective-C'] += language_counter[k]
            del language_counter[k]
        if k in ['groovy']:
            language_counter['Groovy'] += language_counter[k]
            del language_counter[k]
        if k in ['MATLAB', 'Matlab']:
            language_counter['Matlab'] += language_counter[k]
            del language_counter[k]
        if k in ['Actionscript', 'Actionscript 3', 'Action Script']:
            language_counter['ActionScript'] += language_counter[k]
            del language_counter[k]
        if k in ['scala']:
            language_counter['Scala'] += language_counter[k]
            del language_counter[k]
        if k in ['Coldfusion']:
            language_counter['ColdFusion'] += language_counter[k]
            del language_counter[k]
        if k in ['bash']:
            language_counter['Bash'] += language_counter[k]
            del language_counter[k]
        if k in ['clojure']:
            language_counter['Clojure'] += language_counter[k]
            del language_counter[k]
        if k in ['perl']:
            language_counter['perl'] += language_counter[k]
            del language_counter[k]
        if k in ['Typescript']:
            language_counter['TypeScript'] += language_counter[k]
            del language_counter[k]


    for k in list(language_counter.keys()):
        percentage = (language_counter[k]/total_active_practitioners) * 100
        percentage = round(percentage, 2)
        language_counter[k] = percentage

    sorted_by_developer_number = {k: v for k, v in sorted(language_counter.items(), key=lambda item: item[1], reverse=True)}

    print(sorted_by_developer_number)

    td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
        'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
        'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
        'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
        'jQuery': 0, 'shell': 0}

    for k in sorted_by_developer_number:
        if k in td:
            td[k] = sorted_by_developer_number[k]
        if k == 'bash':
            td['Bash'] += sorted_by_developer_number[k]
        if k == 'Ocaml':
            td['Ocaml'] += sorted_by_developer_number[k]
        if k == 'Sharepoint':
            td['Sharepoint'] += sorted_by_developer_number[k]

    with open('results/002_language_popularity.csv', 'a', newline='') as f:
        fieldnames=['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C',  
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(td) 


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