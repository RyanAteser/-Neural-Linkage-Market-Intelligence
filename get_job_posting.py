import requests

def get_job_posting_data(company_name, api_key):
    # Example Indeed API URL structure (this will vary depending on the actual API documentation)
    job_url = f"https://api.indeed.com/v2/job/search?query={company_name}&api_key={api_key}"
    
    try:
        # Fetch the job data from Indeed API
        response = requests.get(job_url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Return job postings if available
        return response.json().get('job_postings', [])
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching job postings: {e}")
        return None

# Example usage (you need to replace 'your_api_key' with a valid Indeed API key)
company_name = "Google"
api_key = "your_api_key"
job_postings = get_job_posting_data(company_name, api_key)

if job_postings:
    print(f"Found {len(job_postings)} job postings for {company_name}:")
    for job in job_postings:
        print(job)
else:
    print("No job postings found.")
