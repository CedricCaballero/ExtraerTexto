import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "http://localhost:8186/web-service-enroll/api/automation-docs/enrollment/query/request-state-events"

payload = {
    "totalElements": 0,
    "pageNumber": 0,
    "size": 252,
    "totalPages": 0,
    "typeEvent": "ASSISTANT",
    "status": "PENDING",
    "requestType": "CREATE"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json=payload, verify=False)

print("Código de estado:", response.status_code)

if response.status_code == 200:
    try:
        print("Respuesta JSON:", response.json())
    except ValueError:
        print("La respuesta no es JSON válida:", response.text)
else:
    print(f"Error {response.status_code}: {response.text}")