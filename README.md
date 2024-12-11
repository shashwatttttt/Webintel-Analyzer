# Webintel-Analyzer
## Overview

WebIntel Analyzer is a Python-based tool designed to analyze and extract comprehensive information from a webpage. It provides insights into the structure, metadata, resources, and technologies used by the website. This tool is perfect for developers, security analysts, and researchers who need detailed web intelligence.

---

### Features:
- Extract webpage metadata (title, meta tags, headers).
- Identify and list links, images, scripts, and stylesheets.
- Analyze and report on technologies used by the website (similar to Wappalyzer).
- Save the extracted information in various formats: JSON, CSV, or TXT.

---

## Installation

### Prerequisites

- Python 3.9 or above.

#### Install required Python libraries:

  - pip install requests beautifulsoup4 wappalyzer-python

#### Clone the Repository

Download or clone the script to your local machine:

- git clone https://github.com/your-repo/WebIntelAnalyzer.git

- cd WebIntelAnalyzer

### Usage

Running the Script

- You can run the script using the following command:

- python WebIntelAnalyzer.py <url> [--format {json,csv,txt}] [--output OUTPUT]

#### Arguments

- url: The URL of the webpage to analyze (required).

- --format: The desired output file format (json, csv, or txt).

- --output: The name of the output file (optional). If not specified, data will only be displayed on the terminal.

## Example

To analyze https://example.com and save the results as output.json:

- python WebIntelAnalyzer.py https://example.com --format json --output output.json

## Interactive Mode

If you don't provide the URL as an argument, the script will prompt you to enter the URL:

- python WebIntelAnalyzer.py
- Please enter the URL of the webpage to analyze: https://example.com

## Sample Output

### Console Output



Title: Example Domain

Headers:
  H1:
    - Example Header 1
  H2:
    - Example Header 2

Links:
  - https://example.com/about
  - https://example.com/contact

Meta Tags:
  description: This is an example meta tag
  keywords: example, demo

Technologies Used:
  Nginx:
    Description: Nginx is a high-performance web server.
    Categories: Web Servers
  jQuery:
    Description: jQuery is a fast, small, and feature-rich JavaScript library.
    Categories: JavaScript Libraries

## Saved Output (JSON)

{
    "Title": "Example Domain",
    "Headers": {
        "H1": ["Example Header 1"],
        "H2": ["Example Header 2"]
    },
    "Links": ["https://example.com/about", "https://example.com/contact"],
    "Meta Tags": {
        "description": "This is an example meta tag",
        "keywords": "example, demo"
    },
    "Technologies Used": {
        "Nginx": {
            "Description": "Nginx is a high-performance web server.",
            "Categories": "Web Servers"
        },
        "jQuery": {
            "Description": "jQuery is a fast, small, and feature-rich JavaScript library.",
            "Categories": "JavaScript Libraries"
        }
    }
}

## Notes

- Ensure you have a stable internet connection as the script fetches data from live webpages.

- If you encounter issues with permissions, run the script as an administrator or use the --user flag while installing dependencies.
---
## Author

- Developed by: Shashwatttttt

- For any queries or contributions, feel free to contact or raise an issue on GitHub.

## License
---
- This project is licensed under the MIT License. See the LICENSE file for details.

