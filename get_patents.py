def get_patent_activity(company_name):
    patent_url = f"https://api.uspto.gov/patents/{company_name}"
    response = requests.get(patent_url)
    return response.json()['patent_count']
