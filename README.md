Overview
This project aims to automate the process of gathering trade data from a specific website using Selenium, performing data cleaning on the obtained data, and visualizing insights through a dashboard created in Power BI.

Features
Web Scraping: Utilizes Selenium, a powerful web scraping tool, to navigate through web pages and extract trade data.
Data Cleaning: Implements data cleaning techniques using Python and pandas to prepare the scraped data for analysis.
Power BI Dashboard: Creates an interactive dashboard in Power BI to visualize key trade metrics and trends.
Workflow
Web Scraping: Selenium is employed to automate the extraction of trade data from the target website. This includes selecting various parameters such as product, country, and partner, and exporting the data.
Data Cleaning: The extracted data is then processed using Python and pandas to handle missing values, format columns, and perform necessary transformations to ensure data accuracy and consistency.
Power BI Dashboard Creation: The cleaned data is imported into Power BI, where a visually appealing and interactive dashboard is designed. Key trade metrics such as total exports, imports, trade balance, and trends over time are visualized using various charts and graphs.
Usage
Clone the repository to your local machine.
Install the required dependencies specified in the requirements.txt file.
Run the Python script to perform web scraping and data cleaning.
Open Power BI and import the cleaned data.
Design and customize the dashboard to suit your analytical needs.
Dependencies
Python 3.x
Selenium
pandas
Power BI Desktop
