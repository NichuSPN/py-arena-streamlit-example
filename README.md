# COVID Data Dashboard

This project is a web application built using Streamlit and py-arena, designed to visualize COVID-19 data. It fetches data from the COVID Tracking Project API and displays historical values, metrics for specific dates, and more.

## Features

- **Historical Data Visualization**: View trends in hospitalized cases, deaths, positives, and negatives over time.
- **Date-Specific Metrics**: Select a date to see the COVID-19 metrics for that specific day.
- **User-Friendly Interface**: Built with Streamlit for an interactive and responsive user experience.

## Technologies Used

- **Streamlit**: An open-source app framework for Machine Learning and Data Science projects.
- **py-arena**: An API and Relational Engine for Network Applications, simplifying database interactions.
- **Pandas**: A powerful data manipulation and analysis library for Python.

## Setting Up the Database

To set up the PostgreSQL database and import the COVID-19 data, follow these steps:

1. **Ensure PostgreSQL is Installed**: Make sure you have PostgreSQL installed on your machine. You can download it from [the official PostgreSQL website](https://www.postgresql.org/download/).

2. **Create a Database**: Open your terminal or command prompt and create a new database. You can do this by accessing the PostgreSQL command line interface (psql) and running:
   ```sql
   CREATE DATABASE your_database_name;
   ```

3. **Connect to the Database**: Connect to your newly created database:
   ```bash
   psql -U your_username -d your_database_name
   ```

4. **Run the SQL Script**: Once connected, you can run the `script.sql` file to create the necessary table and import the data. Use the following command:
   ```sql
   \i path/to/project/sql/script.sql
   ```

5. **Verify the Data**: After running the script, you can verify that the data has been imported correctly by running:
   ```sql
   SELECT * FROM corona_history_values LIMIT 10;
   ```

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/nichuspn/py-arena-streamlit-example.git
   cd covid-data-dashboard
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

## Usage

- Open your web browser and navigate to `http://localhost:8501` to view the application.
- Use the date picker to select a specific date and view the corresponding metrics.

## Data Source

This application uses data from the [COVID Tracking Project](https://covidtracking.com/data/api).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.