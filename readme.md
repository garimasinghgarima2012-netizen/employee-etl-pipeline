# Employee ETL Pipeline

## Project Overview
This project is an Employee ETL (Extract, Transform, Load) Pipeline developed using Python and MySQL.

The pipeline reads employee data from a JSON file, cleans and transforms the data, and loads it into a MySQL database.

## Features
- Extract employee data from JSON
- Clean names, emails, and departments
- Remove duplicate records
- Convert salary from string to integer
- Validate email addresses using Regex
- Calculate salary increment
- Generate KPI report
- Load data into MySQL
- Update existing employees using ON DUPLICATE KEY UPDATE

## Technologies Used
- Python
- MySQL
- MySQL Connector
- JSON
- Regular Expressions (Regex)

## Project Structure

ETL2.0/
│── employee.json
│── extract.py
│── transform.py
│── load.py
│── connect_db.py
│── main.py

## How to Run

1. Clone the repository
2. Install the required packages
3. Create the MySQL database
4. Run:

python main.py

## Author

Garima Singh