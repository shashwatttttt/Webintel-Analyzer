import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
import json
import csv

# Replace builtwith with a more detailed library
from wappalyzer import Wappalyzer, WebPage

def display_banner():
    banner = """
    ======================================
             WebIntel Analyzer
        Developed by: Shashwatttttt
    ======================================
    """
    print(banner)

def save_to_file(data, file_format, file_name):
    try:
        if file_format == "json":
            with open(file_name, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4)
        elif file_format == "csv":
            with open(file_name, "w", encoding="utf-8", newline='') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in data.items():
                    writer.writerow([key, value])
        elif file_format == "txt":
            with open(file_name, "w", encoding="utf-8") as txt_file:
                for key, value in data.items():
                    txt_file.write(f"{key}: {value}\n")
        print(f"Data saved to {file_name}")
    except Exception as e:
        print(f"Error saving data: {e}")

def analyze_technologies(url):
    try:
        # Use Wappalyzer to detect technologies
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        technologies = wappalyzer.analyze(webpage)

        detailed_tech_info = {}
        for tech in technologies:
            # Fetch more detailed descriptions (mock example)
            detailed_tech_info[tech] = {
                "Description": f"{tech} is a technology detected on this site.",
                "Categories": ", ".join(wappalyzer.categories[tech])
            }
        return detailed_tech_info
    except Exception as e:
        print(f"Error analyzing technologies: {e}")
        return {}

def gather_webpage_info(url, file_format=None, file_name=None):
    try:
        # Fetch the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Gather information
        title = soup.title.string if soup.title else 'No Title Found'
        headers = {f"h{i}": [h.text.strip() for h in soup.find_all(f"h{i}")] for i in range(1, 7)}
        links = [urljoin(url, link['href']) for link in soup.find_all('a', href=True)]
        meta_tags = {meta.get('name', meta.get('property', 'Unnamed')): meta.get('content', '') for meta in
                     soup.find_all('meta')}
        images = [urljoin(url, img['src']) for img in soup.find_all('img', src=True)]
        scripts = [urljoin(url, script['src']) for script in soup.find_all('script', src=True)]
        stylesheets = [urljoin(url, link['href']) for link in soup.find_all('link', rel="stylesheet")]

        # Analyze technologies
        detailed_tech_info = analyze_technologies(url)

        # Organize data for saving
        data = {
            "Title": title,
            "Headers": headers,
            "Links": links,
            "Meta Tags": meta_tags,
            "Images": images,
            "Scripts": scripts,
            "Stylesheets": stylesheets,
            "Technologies Used": detailed_tech_info
        }

        # Display information
        print(f"Title: {title}\n")

        print("Headers:")
        for header_level, header_list in headers.items():
            print(f"  {header_level.upper()}:")
            for header in header_list:
                print(f"    - {header}")

        print("\nLinks:")
        for link in links:
            print(f"  - {link}")

        print("\nMeta Tags:")
        for meta_name, meta_content in meta_tags.items():
            print(f"  {meta_name}: {meta_content}")

        print("\nImages:")
        for image in images:
            print(f"  - {image}")

        print("\nScripts:")
        for script in scripts:
            print(f"  - {script}")

        print("\nStylesheets:")
        for stylesheet in stylesheets:
            print(f"  - {stylesheet}")

        print("\nTechnologies Used:")
        for tech, details in detailed_tech_info.items():
            print(f"  {tech}:")
            print(f"    Description: {details['Description']}")
            print(f"    Categories: {details['Categories']}")

        # Save to file if requested
        if file_format and file_name:
            save_to_file(data, file_format, file_name)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    display_banner()
    parser = argparse.ArgumentParser(description="Webpage Info Gathering Tool")
    parser.add_argument("url", nargs="?", help="URL of the webpage to analyze")
    parser.add_argument("--format", choices=["json", "csv", "txt"], help="Output file format")
    parser.add_argument("--output", help="Output file name")
    args = parser.parse_args()

    # Prompt for URL if not provided as an argument
    url = args.url if args.url else input("Please enter the URL of the webpage to analyze: ")

    gather_webpage_info(url, args.format, args.output)
