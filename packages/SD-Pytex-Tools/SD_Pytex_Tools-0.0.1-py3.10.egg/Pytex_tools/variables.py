import inspect
from multiprocessing.sharedctypes import Value
import os

class var_saver():
    def __init__(self, variables_file='python_variables.tex', prefix=''):
        """
        Class that allows to store numeric variables and reuse them in Latex document

        Parameters
        ----------
        variables_file : str
            Name / path of the file that will store the variables
        prefix : str
            Prefix for each variable when using in LaTex \prefixcommand
            underscores aren't allowed        
        """
        # Check types
        if not isinstance(variables_file, str):
            raise ValueError("variables_file must be str")
        if not isinstance(prefix, str):
            raise ValueError("prefix must be str")

        self._file_path = variables_file
        self._prefix = prefix

    
    def _store_variable(self, variables):
        """
        Stores the variables on the dictionnary "variable" to the file. Replaces if necessary        
        """
        # If the file doesn't exist, create it
        if not os.path.exists(self._file_path) :
            with open(self._file_path, 'w'):
                f.write('')
        
        with open(self._file_path, 'r') as f:
            content = f.read()
            for name, value in variables.items():
                if "_" in name:
                    raise ValueError("name cannot contain underscore (LaTex compatibility)")
                command = "{" + self._prefix + name + "}"
                try:
                    value_start = content.index(command) + len(command) + 1
                except ValueError as e:
                    # not found
                    content += f"\\newcommand{{{self._prefix + name}}}{{{value}}}\n"
                else:
                    # Replace the value only
                    value_end = content.index("}", value_start)
                    content = content[:value_start] + f"{value}" + content[value_end:]

        with open(self._file_path, 'w') as f:
            f.write(content)

    
    
        



    def save(self, *args):
        # https://stackoverflow.com/a/2749857/8418125
        # Extracts arguments names and their values
        frame = inspect.currentframe()
        frame = inspect.getouterframes(frame)[1]
        string = inspect.getframeinfo(frame[0]).code_context[0].strip()
        args_list = string[string.find('(') + 1:-1].replace(' ', '').split(',')
        
        # variables dictionnary contains the variables names and values
        variables = {}
        for i, value in zip(args_list, args):
            if i.find('=') != -1:
                variables.append(i.split('=')[1].strip())
            else:
                variables[i] = value

        self._store_variable(variables)
        

        


    #def save_as(self, variable, name):
