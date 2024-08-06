# LinkedIn Profile Fetcher

## Description

This project fetches LinkedIn profiles for individuals using the RapidAPI LinkedIn API. It is implemented in Python and designed to be run in VS Code.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- VS Code

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/andishehtavakoli/linkedin-profile-fetcher.git
    cd linkdin-app
    ```

2. **Create a Conda environment and activate it:**

    ```bash
    conda create --name linkedin-fetcher python=3.8
    conda activate linkedin-fetcher
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Get your RapidAPI key:**

    Sign up for an account at [RapidAPI](https://rapidapi.com/) and subscribe to the LinkedIn API.

## Usage

1. **Configure your API key:**

    Create a `.env` file in the project root and add your RapidAPI key:

    ```env
    RAPIDAPI_KEY=your_rapidapi_key
    ```

2. **Run the Streamlit app:**

    Open VS Code and run the Streamlit app to fetch LinkedIn profiles.

    ```bash
    streamlit run src/app.py
    ```


## Configuration

- Ensure your `.env` file contains the correct RapidAPI key.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
