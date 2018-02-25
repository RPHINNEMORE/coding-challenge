# Zendesk Coding Challenge 2018 

This project is a CLI based ticket viewer application. It has the following features:
 

 1. View all tickets in a paginated list 
 2. Search for single ticket by a ticket id
 
 ## Project Structure Overview 
 
 This project has been designed with a Model Controller View project structure
 
 * Model: gathers data from Zendesk API and manages pagination 
 * Controller: managers flow of the program and contains core logic
 * View: displays data to the user 
  
 


### Prerequisites


 1. Python 2.7 installed 
 2. Zendesk API - https://developer.zendesk.com/rest_api/docs


### Project Setup  


 Set up virtual env:
1. python -m pip install --user virtualenv
2. cd <project_path>
3. mkdir <project_name>
4. cd <project_name>
5. In terminal virtualenv env
6. source env/bin/activate
7. pip install -r requirements.txt 


### Running Program 

1. cd controller
2. python appController.py
3. follow options listed in CLI

### Running Tests

1. cd tests 
2. python testApp.py -b




