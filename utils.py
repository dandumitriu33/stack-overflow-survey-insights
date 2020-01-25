import csv


def map_data_to_spreadsheet_form(input_dictionary):
    """ Takes the dictionary of languages and percentage, filters duplicate data
        such as python > Python and maps the values to the 'write to csv dictionary'.
        This process helps with alligning the data into a table where all the years
        will be placed, and later, a chart will be easier to create. 
        It also places the key 'year':0 at the beginning of the dictionary in preparation
        for writing to the csv. It will help with charts. The next function below,
        write_popular_languages_dictionary_to_file(input_dictionary, year) will place the year.

    Args: 
        input_dictionary: dictionary from the yearly functions. They have 
        Language(string): percentage(float, 2 decimals) format

    Returns:
        The dictionary with all the Languages keys, with the percentages of the found 
        keys from input_dictionary, in their proper keys. Languages with no respondents
        this year will have value 0.     
    """
    td={'year':0, 'ABAP': 0, 'ActionScript': 0, 'Assembly': 0, 
        'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'Cassandra': 0, 
        'Clojure': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
        'D': 0, 'Dart': 0, 'Delphi': 0, 'Drupal': 0, 'Elixir': 0,  
        'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML/CSS': 0, 'Hack': 0, 'Hadoop': 0, 
        'Haskell': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MATLAB': 0, 'MongoDB': 0,   
        'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'PHP': 0, 'Perl': 0,  
        'Python': 0, 'R': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'Scala': 0, 
        'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB.NET': 0, 'VBA': 0, 
        'VHDL': 0, 'Visual Basic': 0, 'WebAssembly': 0, 'WordPress': 0, 'iOS': 0
        }

    # adjust for duplicates

    for k in list(input_dictionary.keys()):
        if k in ['vb.net', 'VB.Net', 'VB.net']:
            td['VB.NET'] += input_dictionary[k]
        elif k in ['Objective C', 'objective-c']:
            td['Objective-C'] += input_dictionary[k]
        elif k in ['groovy']:
            td['Groovy'] += input_dictionary[k]
        elif k in ['Matlab']:
            td['MATLAB'] += input_dictionary[k]
        elif k in ['Actionscript', 'Actionscript 3', 'Action Script', 'ActionScript 3']:
            td['ActionScript'] += input_dictionary[k]     
        elif k in ['scala']:
            td['Scala'] += input_dictionary[k]
        elif k in ['Coldfusion']:
            td['ColdFusion'] += input_dictionary[k]
        elif k in ['bash', 'Bash', 'Bash/Shell', 'shell', 'PowerShell', 'Powershell']:
            td['Bash/Shell/PowerShell'] += input_dictionary[k]
        elif k in ['clojure', 'Clojure', 'AngularJS', 'React', 'ReactJS', 'EmberJS', 'Ember.js', 'jQuery', 'JQuery', 'Dojo']:
            td['JavaScript'] += input_dictionary[k]
        elif k in ['perl']:
            td['Perl'] += input_dictionary[k]
        elif k in ['Typescript']:
            td['TypeScript'] += input_dictionary[k]
        elif k in ['CSS', 'HTML', 'HTML, CSS', 'HTML5']:
            td['HTML/CSS'] += input_dictionary[k]
        elif k in ['Delphi/Object Pascal']:
            td['Delphi'] += input_dictionary[k]
        elif k in ['Visual Basic 6', 'VB', 'VB6']:
            td['Visual Basic'] += input_dictionary[k]
        elif k in ['Wordpress']:
            td['WordPress'] += input_dictionary[k]
        elif k in ['Django']:
            td['Python'] += input_dictionary[k]
        elif k in ['PL/SQL', 'MySQL', 'SQL Server']:
            td['SQL'] += input_dictionary[k]
        elif k in ['SharePoint', 'Sharepoint']:
            td['C#'] += input_dictionary[k]
        elif k in ['C++11']:
            td['C++'] += input_dictionary[k]
        elif k in ['Ocaml']:
            td['OCaml'] += input_dictionary[k]
        elif k in ['Cloud (AWS, GAE, Azure, etc.)', 'Android', 'Arduino / Raspberry Pi', 'Windows Phone',
                    'Salesforce', '', 'NA', 'Other(s):']:
            pass
        else:
            try:
                td[k] += input_dictionary[k]
            except ValueError:
                pass

    return td


def write_popular_languages_dictionary_to_file(input_dictionary, year):
    """Writes the dicitionary to the .csv file to prepare for charts.
    If the year is 2011, the process is 'w' in order to write the headers.
    The rest of the years are 'a'.

    Args: 
        input_dictionary: dictionary from the yearly functions. They have 
        Language(string): percentage(float, 2 decimals) format
        year: integer, the year of the dictionary    
    """
    input_dictionary['year'] = year
    if year == 2011:
        with open('results/002_language_popularity.csv', 'w', newline='') as f:
            fieldnames=['year', 'ABAP', 'ActionScript', 'Assembly', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'Cassandra', 
                        'Clojure', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
                        'Delphi', 'Drupal', 'Elixir', 'Erlang', 'F#', 'Fortran', 'Go', 'Groovy', 'HTML/CSS', 'Hack', 
                        'Hadoop', 'Haskell', 'Java', 'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MATLAB', 'MongoDB',
                        'Node.js', 'OCaml', 'Objective-C', 'PHP', 'Perl', 'Python', 'R', 'Redis', 'Ruby', 'Rust', 'SQL', 
                        'Scala', 'Smalltalk', 'Spark', 'Swift', 'TypeScript', 'VB.NET', 'VBA', 'VHDL', 'Visual Basic', 
                        'WebAssembly', 'WordPress', 'iOS']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(input_dictionary)
    elif year != 2011:
        with open('results/002_language_popularity.csv', 'a', newline='') as f:
            fieldnames=['year', 'ABAP', 'ActionScript', 'Assembly', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'Cassandra', 
                        'Clojure', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
                        'Delphi', 'Drupal', 'Elixir', 'Erlang', 'F#', 'Fortran', 'Go', 'Groovy', 'HTML/CSS', 'Hack', 
                        'Hadoop', 'Haskell', 'Java', 'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MATLAB', 'MongoDB',
                        'Node.js', 'OCaml', 'Objective-C', 'PHP', 'Perl', 'Python', 'R', 'Redis', 'Ruby', 'Rust', 'SQL', 
                        'Scala', 'Smalltalk', 'Spark', 'Swift', 'TypeScript', 'VB.NET', 'VBA', 'VHDL', 'Visual Basic', 
                        'WebAssembly', 'WordPress', 'iOS']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(input_dictionary)
