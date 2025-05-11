import requests
from urllib.parse import urlparse

def generate_webhook():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": "Jayan Shah",
        "regNo": "0827AL221063",
        "email": "jayanshah220366@acropolis.in"
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error generating webhook: {e}")
        return None

def solve_sql_problem():
    query = """
    SELECT 
        p.AMOUNT AS SALARY,
        e.FIRST_NAME || ' ' || e.LAST_NAME AS NAME,
        (strftime('%Y', 'now') - strftime('%Y', e.DOB)) - 
        (CASE WHEN strftime('%m%d', 'now') < strftime('%m%d', e.DOB) 
              THEN 1 ELSE 0 END) AS AGE,
        d.DEPARTMENT_NAME
    FROM PAYMENTS p
    JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
    JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
    WHERE strftime('%d', p.PAYMENT_TIME) != '01'
    ORDER BY p.AMOUNT DESC
    LIMIT 1
    """
    return query

def submit_solution(webhook_url, access_token, final_query):
    parsed_url = urlparse(webhook_url)
    submission_url = f"https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
    payload = {"finalQuery": final_query}
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(submission_url, json=payload, headers=headers)
        response.raise_for_status()
        print("Solution submitted successfully")
        return response.json()
    except requests.RequestException as e:
        print(f"Error submitting solution: {e}")
        return None

def main():
    webhook_response = generate_webhook()
    if not webhook_response:
        print("Failed to generate webhook")
        return
    webhook_url = webhook_response.get('webhook')
    access_token = webhook_response.get('accessToken')
    if not webhook_url or not access_token:
        print("Failed to retrieve webhook URL or access token")
        return
    final_query = solve_sql_problem()
    submit_solution(webhook_url, access_token, final_query)

if __name__ == "__main__":
    main()