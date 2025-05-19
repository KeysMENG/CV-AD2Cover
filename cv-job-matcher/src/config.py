# Configuration settings for the CV-Job Matcher application

# API keys and other constants
API_KEY = "your_api_key_here"  # Replace with your actual API key if needed

# File paths
CV_UPLOAD_PATH = "uploads/cvs/"
JOB_DESCRIPTION_PATH = "uploads/job_descriptions/"

# Other constants
MAX_CV_SIZE_MB = 5  # Maximum CV file size in MB
SUPPORTED_FILE_FORMATS = ['.pdf', '.docx', '.txt']  # Supported CV file formats

# Web scraping settings
SCRAPING_TIMEOUT = 10  # Timeout for web scraping requests in seconds
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"  # User agent for web requests