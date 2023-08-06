import pandas as pd
from pathlib import Path
from PyInquirer import prompt

class TransformationWrapper:

    def __init__(self,df,file_obj,package):
        self.df = df
        self.file_obj = file_obj
        self.package = package


    def change_column_name_prompt(self,column_ix,name):
        question={
            'type':'input',
            'name':f"column_{column_ix}",
            'message':f' #{column_ix} Choose the new name for the column  - {name}: - (press enter to make no changes):',
            'default':f"{name}"
        }

        answer = prompt(question)
        return answer[f"column_{column_ix}"]

    def change_column_name(self):
        list_of_columns=self.df.columns.tolist()
        new_list=[]
        for ix,column in enumerate(list_of_columns):
            new_val = self.change_column_name_prompt(ix,column)
            new_list.append(new_val)
        print("Processing column changes...")
        self.df.columns = new_list
        print("The names of the columns have been successfully changed!")

    def change_file_name(self):
        old_path = Path(self.file_obj.path)

        question={
            'type':'input',
            'name':'change_name',
            'message':"Please choose a name for your new file, or press enter to make no changes.",
            'default':f"{old_path.stem}"

        }
        answer= prompt(question)

        new_path = str(old_path.parent)+"/"+answer['change_name']+self.file_obj.dest_extension
        self.file_obj.path=new_path
        print("Your file will have a new name now!")


    def ingest_transformations(self):
        if self.package['confirm_transformations'] is False:
            return self.df

        transformation_map={'Change Column Names':self.change_column_name,
                            'Change File Name':self.change_file_name}

        for action in self.package['transformations']:
            funct_to_call = transformation_map[action]
            funct_to_call()
