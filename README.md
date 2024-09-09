# Sales-Data-ETL-pipeline
Overview
This project is an end-to-end ETL (Extract, Transform, Load) pipeline for e-commerce sales data. The pipeline processes raw sales data, performs transformations to clean and prepare it, and loads the data into a SQLite database. Additionally, it generates visualizations to analyze sales trends.

# Project Features
Data Ingestion: Extracts sales data from CSV files.
Data Transformation: Cleans and processes the data, including handling missing values and adding calculated metrics like Total Sales and Average Order Value (AOV).
Data Loading: Loads the transformed data into a SQLite database for storage and querying.
Data Visualization: Generates visual reports, such as sales by product category and sales by region.

# Technologies Used
Python: Core programming language.
pandas: For data manipulation and transformation.
SQLite: For database storage and querying.
Matplotlib/Seaborn: For data visualization.

# Future Work
Automation: Implementing Apache Airflow to automate the ETL pipeline.
Cloud Deployment: Deploying the pipeline on AWS using S3 for storage and Redshift for scalable data warehousing.

