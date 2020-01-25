key_list = ['JavaScript', 'HTML/CSS', 'SQL', 'Java', 'Python', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 
            'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Swift', 'Kotlin', 'Assembly', 'R', 'VBA', 'Objective-C', 
            'Scala', 'Rust', 'Dart', 'Elixir', 'Clojure', 'F#', 'WebAssembly', 'NA', 'Erlang',
            'JavaScript', 'HTML', 'CSS', 'SQL', 'Java', 'Bash/Shell', 'Python', 'C#', 'PHP', 'NA', 'C++', 'C', 
            'TypeScript', 'Ruby', 'Swift', 'Assembly', 'Go', 'Objective-C', 'VB.NET', 'R', 'VBA', 'Kotlin', 
            'Scala', 'Groovy', 'Perl', 'Visual Basic 6', 'Lua', 'CoffeeScript', 'Delphi/Object Pascal', 'Haskell', 
            'Rust', 'F#', 'Clojure', 'Erlang', 'Cobol', 'Ocaml', 'Julia', 'Hack',
            'JavaScript', 'SQL', 'NA', 'Java', 'C#', 'Python', 'PHP', 'C++', 'C', 'TypeScript', 'Ruby', 'Swift', 
            'Objective-C', 'VB.NET', 'Assembly', 'R', 'Perl', 'VBA', 'Go', 'Scala', 'CoffeeScript', 'Groovy', 
            'Visual Basic 6', 'Lua', 'Haskell', 'F#', 'Rust', 'Clojure', 'Elixir', 'Smalltalk', 'Erlang', 
            'Common Lisp', 'Dart', 'Julia', 'Hack',
            'JavaScript', 'SQL', 'Java', 'C#', 'PHP', 'Python', 'C++', 'SQL Server', 'AngularJS', 'Android', 
            'Node.js', 'C', '', 'LAMP', 'MongoDB', 'Cloud (AWS, GAE, Azure, etc.)', 'iOS', 'WordPress', 'Ruby', 
            'Arduino / Raspberry Pi', 'Visual Basic', 'Objective-C', 'Redis', 'Swift', 'ReactJS', 'CoffeeScript', 
            'Cordova', 'Perl', 'Scala', 'Go', 'R', 'Windows Phone', 'Hadoop', 'SharePoint', 'Haskell', 'Spark', 
            'Cassandra', 'Salesforce', 'Clojure', 'F#', 'Rust', 'Dart',
            'JavaScript', 'SQL', 'Java', 'C#', 'PHP', 'Python', 'C++', 'SQL Server', 'Android', 'C', 'Node.js', 
            'AngularJS', 'Wordpress', 'LAMP', 'iOS', 'C++11', 'Ruby', 'MongoDB', 'Objective-C', 'Visual Basic', 
            'Arduino / Raspberry Pi', 'Cloud (AWS, GAE, Azure, etc.)', 'Redis', 'CoffeeScript', 'R', 'Perl', 
            'Swift', 'Cordova', 'Windows Phone', 'Scala', 'Go', 'Haskell', 'Sharepoint', 'Hadoop', 'Cassandra', 
            'Clojure', 'F#', 'Salesforce', 'Dart', 'Spark', 'Rust', 'Groovy', 'Delphi', 'TypeScript', 'Bash', 
            'Lua', 'Erlang', 'Fortran', 'Powershell', 'PowerShell', 'PL/SQL', 'HTML, CSS', 'ColdFusion', 'HTML', 
            'Django', 'VBA', 'Drupal', 'EmberJS', 'D', 'MySQL', 'OCaml', 'Julia', 'VHDL', 'Ember.js', 'ABAP', 
            'ActionScript', 'React',
            'JavaScript', 'SQL', 'Java', 'C#', 'PHP', 'Python', 'C++', 'C', 'Objective-C', 'Node.js', 'Ruby', 
            'Scala', 'VB.NET', 'Perl', 'Delphi', 'Haskell', 'Groovy', 'Go', 'F#', 'R', 'bash', 'Lua', 'VBA', 
            'ColdFusion', 'VB', 'jQuery', 'Clojure', 'Visual Basic',
            'JavaScript', 'SQL', 'jQuery', 'C#', 'Java', 'PHP', 'Python', 'C++', 'C', 'Objective-C', 'Ruby', 
            'Node.js', 'JQuery', 'VB.NET', 'Perl', 'Delphi', 'Scala', 'Groovy', 'R', 'Clojure', 'perl', 'Haskell', 
            'Bash', 'VB', 'ColdFusion', 'CoffeeScript', 'Lua', 'F#', 'VBA', 'HTML, CSS', 'Visual Basic', 'Powershell', 
            'HTML', 'MongoDB', 'ActionScript', 'ABAP', 'Erlang', 'Dojo',
            'SQL', 'JavaScript', 'CSS', 'C#', 'Java', 'HTML5', 'PHP', 'C++', 'C', 'Python', 'Ruby', 'Objective-C', 
            'Perl', 'VB.NET', 'Delphi', 'Groovy', 'Scala', 'Haskell', 'ActionScript', 'ColdFusion', 'VB', 
            'Visual Basic', 'F#', 'Lua', 'R', 'ActionScript 3', 'VBA', 'PL/SQL', 'shell', 'Clojure', 'Powershell', 'VB6',
            'SQL', 'JavaScript', 'C#', 'CSS', 'Java', 'PHP', 'C++', 'C', 'Python', 'Ruby', 'Perl', 'Objective-C', 'VB.NET', 
            'Delphi', 'VB', 'Haskell', 'Scala', 'ActionScript', 'ColdFusion', 'HTML', 'F#', 'Groovy', 'PowerShell']
wow = set(key_list)
headers = list(wow)
headers.sort()
print(headers)

result = ['', 'ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C', 'Ocaml', 
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'bash', 'iOS', 'jQuery', 'perl', 'shell']

to_compare = ['ABAP', 'ActionScript', 'ActionScript 3', 'Android', 'AngularJS', 'Arduino / Raspberry Pi', 'Assembly', 
            'Bash', 'Bash/Shell', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'C++11', 'CSS', 'Cassandra', 'Clojure', 
            'Cloud (AWS, GAE, Azure, etc.)', 'Cobol', 'CoffeeScript', 'ColdFusion', 'Common Lisp', 'Cordova', 'D', 'Dart', 
            'Delphi', 'Delphi/Object Pascal', 'Django', 'Dojo', 'Drupal', 'Elixir', 'Ember.js', 'EmberJS', 'Erlang', 'F#', 
            'Fortran', 'Go', 'Groovy', 'HTML', 'HTML, CSS', 'HTML/CSS', 'HTML5', 'Hack', 'Hadoop', 'Haskell', 'JQuery', 'Java', 
            'JavaScript', 'Julia', 'Kotlin', 'LAMP', 'Lua', 'MongoDB', 'MySQL', 'NA', 'Node.js', 'OCaml', 'Objective-C', 'Ocaml', 
            'Other(s):', 'PHP', 'PL/SQL', 'Perl', 'PowerShell', 'Powershell', 'Python', 'R', 'React', 'ReactJS', 'Redis', 'Ruby', 
            'Rust', 'SQL', 'SQL Server', 'Salesforce', 'Scala', 'SharePoint', 'Sharepoint', 'Smalltalk', 'Spark', 'Swift', 
            'TypeScript', 'VB', 'VB.NET', 'VB6', 'VBA', 'VHDL', 'Visual Basic', 'Visual Basic 6', 'WebAssembly', 'Windows Phone', 
            'WordPress', 'Wordpress', 'iOS', 'jQuery', 'shell']


temp_dict = {}

for i in to_compare:
    temp_dict[i] = 0

print(temp_dict) 

td={'ABAP': 0, 'ActionScript': 0, 'ActionScript 3': 0, 'Android': 0, 'AngularJS': 0, 'Arduino / Raspberry Pi': 0, 'Assembly': 0, 
    'Bash': 0, 'Bash/Shell': 0, 'Bash/Shell/PowerShell': 0, 'C': 0, 'C#': 0, 'C++': 0, 'C++11': 0, 'CSS': 0, 'Cassandra': 0, 
    'Clojure': 0, 'Cloud (AWS, GAE, Azure, etc.)': 0, 'Cobol': 0, 'CoffeeScript': 0, 'ColdFusion': 0, 'Common Lisp': 0, 'Cordova': 0, 
    'D': 0, 'Dart': 0, 'Delphi': 0, 'Delphi/Object Pascal': 0, 'Django': 0, 'Dojo': 0, 'Drupal': 0, 'Elixir': 0, 'Ember.js': 0, 'EmberJS': 0, 
    'Erlang': 0, 'F#': 0, 'Fortran': 0, 'Go': 0, 'Groovy': 0, 'HTML': 0, 'HTML, CSS': 0, 'HTML/CSS': 0, 'HTML5': 0, 'Hack': 0, 'Hadoop': 0, 
    'Haskell': 0, 'JQuery': 0, 'Java': 0, 'JavaScript': 0, 'Julia': 0, 'Kotlin': 0, 'LAMP': 0, 'Lua': 0, 'MongoDB': 0, 'MySQL': 0, 'NA': 0, 
    'Node.js': 0, 'OCaml': 0, 'Objective-C': 0, 'Ocaml': 0, 'Other(s):': 0, 'PHP': 0, 'PL/SQL': 0, 'Perl': 0, 'PowerShell': 0, 'Powershell': 0, 
    'Python': 0, 'R': 0, 'React': 0, 'ReactJS': 0, 'Redis': 0, 'Ruby': 0, 'Rust': 0, 'SQL': 0, 'SQL Server': 0, 'Salesforce': 0, 'Scala': 0, 
    'SharePoint': 0, 'Sharepoint': 0, 'Smalltalk': 0, 'Spark': 0, 'Swift': 0, 'TypeScript': 0, 'VB': 0, 'VB.NET': 0, 'VB6': 0, 'VBA': 0, 
    'VHDL': 0, 'Visual Basic': 0, 'Visual Basic 6': 0, 'WebAssembly': 0, 'Windows Phone': 0, 'WordPress': 0, 'Wordpress': 0, 'iOS': 0, 
    'jQuery': 0, 'shell': 0}

    # key_list = []
    # for key in sorted_by_developer_number:
    #     key_list.append(key)
    # print(key_list)