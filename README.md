# Facebook Poke Back Automation Script

This project is a simple automation script that logs into Facebook and automatically returns pokes to friends. It uses Selenium WebDriver to control the Chrome browser and performs the required actions seamlessly.

## Table of Contents

- [Facebook Poke Back Automation Script](#facebook-poke-back-automation-script)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
    - [Required Python Packages](#required-python-packages)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Script Overview](#script-overview)
    - [Important Functions](#important-functions)
  - [Author](#author)
  - [License](#license)

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Chrome Browser
- ChromeDriver compatible with your Chrome version

### Required Python Packages

The script uses the following Python packages:

- `selenium`
- `python-dotenv`
- `colorama`

You can install these packages using pip. Refer to the `requirements.txt` file for the complete list of dependencies.

## Installation

1. **Clone the repository** (if applicable):

   ```bash
   git clone https://github.com/NightDev19/facebook-poke-back.git
   cd facebook-poke-back
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory and add your Facebook credentials:
   ```dotenv
   FB_EMAIL=your_facebook_email
   FB_PASS=your_facebook_password
   ```

## Usage

1. Make sure the Chrome browser and ChromeDriver are correctly set up.
2. Ensure your `.env` file contains valid Facebook credentials.
3. Run the script:
   ```bash
   python your_script_name.py
   ```

## Script Overview

This script performs the following tasks:

1. Loads environment variables containing Facebook credentials.
2. Configures Chrome options to disable notifications and set the user agent.
3. Logs into Facebook using the provided credentials.
4. Navigates to the Pokes page.
5. Identifies and clicks on the "Poke Back" buttons to return pokes to friends.
6. Continuously checks for new pokes to return.

### Important Functions

- `delay(seconds)`: Pauses execution for a given number of seconds.
- `scroll_to_element(element)`: Scrolls the page to bring the specified element into view.

## Author

This script was created by **NightDev**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
