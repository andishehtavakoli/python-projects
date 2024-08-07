# Arab Job Search ETL Project
<img src= 'https://www.iaee.com/wp-content/uploads/2016/05/banner-cc-jobs.jpg'>

This project is designed to scrape data from Gulf Talent, process it, and load it into a PostgreSQL database for analysis. The ETL (Extract, Transform, Load) process ensures that the data is cleaned and organized for easy access.

## Overview

The project involves three main steps:

1. **Extract**: Scraping job listings from Gulf Talent.
2. **Transform**: Cleaning and formatting the scraped data.
3. **Load**: Storing the processed data into a PostgreSQL database named 'arab job search'.

## Requirements

- Python 3.x
- Beautiful Soup (for web scraping)
- psycopg2 (PostgreSQL adapter for Python)

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/yourusername/arab-job-search.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run `extract.py` to perform the extraction process.
2. Use `transform.py` to clean and format the data.
3. Execute `load.py` to load the processed data into the PostgreSQL database.
4. To run the complete ETL process, execute `execute.py`.

## Configuration

Ensure your PostgreSQL database credentials are set in `config.py`:

```python
# Database configuration
DB_NAME = 'arab_job_search'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'
DB_PORT = '5432'
```
## Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.
