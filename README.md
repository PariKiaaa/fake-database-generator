# Fake Database Generator

A simple and customizable Python tool that generates an SQLite database filled with fake user information. It allows you to choose the database name, table name, fields, language, and the number of generated records.

This project is useful for testing applications, creating sample databases, practicing SQL queries, and backend/data-handling exercises.

## Features
- Generate an SQLite database with any table name
- Choose your own columns (name, phone, email, age, etc.)
- Supports English, Persian, or both
- Automatically creates unique usernames
- Uses the Faker library to generate realistic data
- Fully interactive command-line interface

## Requirements
Install Faker with:
pip install faker

## Output Location
After completing the setup through the command-line prompts, the script creates an SQLite file with the name you chose (or the current date-time) followed by `.db`.

The file is saved **in the same folder where `dbGenerator.py` is located**.

## Supported Columns
username (Primary Key)  
password  
name  
age  
phone  
gender  
job  
city  
address  
bank  
email  
credit_card  
company  

## Future Improvements
- Develop a **GUI version** for easier usage  
- Add **export options**: CSV and JSON  
- Allow **custom column types** via configuration  
- Support **multi-language datasets** beyond English/Persian

- Export data to CSV or JSON


## Author
Created by PariKia  
GitHub: https://github.com/PariKiaaa
