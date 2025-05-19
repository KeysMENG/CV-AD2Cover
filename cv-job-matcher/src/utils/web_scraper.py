import requests
from bs4 import BeautifulSoup

def scrape_job_description(url):
    """
    Scrapes job description from the provided URL.
    
    Parameters:
        url (str): The URL of the job listing to scrape.
        
    Returns:
        str: The job description text if found, otherwise an empty string.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Adjust the selector based on the website structure
        job_description = soup.find('div', class_='job-description')
        
        if job_description:
            return job_description.get_text(strip=True)
        else:
            return ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the job description: {e}")
        return ""