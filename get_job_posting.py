def get_job_posting_data(company_name):
    job_url = f"https://api.indeed.com/v1/jobs/{company_name}"
    response = requests.get(job_url)
    return response.json()['job_postings']
