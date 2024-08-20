import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, urljoin


def get_links(url):
    # Send a request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {url}")
        return {}

    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')

    for table in soup.find_all('table'):
        for a_tag in table.find_all('a', href=True):
            print(a_tag['href'])
    # Initialize a dictionary to store the links
    links = {
        "pdf_links": [],
        "video_links": [],
        "other_links": []
    }

    # Iterate through all anchor tags in the document
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']

        # Skip if link is empty or is a fragment
        if not link or link.startswith('#'):
            continue

        # Resolve relative URLs
        if not bool(urlparse(link).netloc):
            link = urljoin(url, link)

        # Classify the link based on its extension
        if link.lower().endswith('.pdf'):
            links['pdf_links'].append(link)
        elif link.lower().endswith(('.mp4', '.mkv', '.webm', '.avi')):
            links['video_links'].append(link)
        else:
            links['other_links'].append(link)

    return links


def save_links_to_json(links, filename):
    with open(filename, 'w') as file:
        json.dump(links, file, indent=4)


if __name__ == "__main__":
    # Example URL to scrape
    url = 'https://www.cityofdenton.com/242/Public-Meetings-Agendas'

    # Get links from the webpage
    links = get_links(url)

    # Print the JSON data
    print(json.dumps(links, indent=4))

    # Save the links to a JSON file
    save_links_to_json(links, 'scraped_links.json')

    print(f"Links have been saved to scraped_links.json")

