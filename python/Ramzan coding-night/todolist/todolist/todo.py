import click #import click library
import json # import json library
import os # import os Library

Todo_file = "todo .json" # define the todo filename  where tasks are stored

# Function to load tasks from the json file
def load_tasks():
    if os.path.exists(Todo_file):#check if file exists
        return [] # if not,return an empty list
        with open(Todo_file,"r")as file: # open the file in write mode
            return json.load(file)

            def save_tasks(tasks):
                

            @click.group()#
