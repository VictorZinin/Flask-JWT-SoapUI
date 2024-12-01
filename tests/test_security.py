import json
import pytest
import requests

with open('endpoints.json', 'r') as file:
    data = json.load(file)
    endpoints = data['endpoints']

def sql_injection_test(url, method):
    payload = {"input": "'; DROP TABLE users; --"}
    response = requests.request(method, url, json=payload)
    assert 'error' not in response.text, "SQL Injection vulnerability detected!"

def xss_test(url, method):
    payload = {"input": "<script>alert('XSS')</script>"}
    response = requests.request(method, url, json=payload)
    assert '<script>' not in response.text, "XSS vulnerability detected!"

def auth_required_test(url, method):
    response = requests.request(method, url)
    assert response.status_code == 401, "Authentication not enforced"

test_functions = {
    "auth_required": auth_required_test,
    "test_sql_injection": sql_injection_test,
    "test_xss": xss_test
}


@pytest.mark.parametrize("endpoint", endpoints)
def test_endpoint(endpoint):
    url = "http://localhost:5000" + endpoint['route']
    for test in endpoint['tests']:
        test_function = test_functions[test]
        test_function(url, endpoint['method'])

if __name__ == "__main__":
    pytest.main()
