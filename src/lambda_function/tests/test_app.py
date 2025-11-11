import json
from src.lambda_function.app import lambda_handler

def test_valid_division():
    event = {"numerator": 10, "denominator": 2}
    resp = lambda_handler(event, None)
    body = json.loads(resp["body"])
    assert resp["statusCode"] == 200
    assert body["result"] == 5.0

def test_division_by_zero():
    event = {"numerator": 10, "denominator": 0}
    resp = lambda_handler(event, None)
    body = json.loads(resp["body"])
    assert resp["statusCode"] == 400
    assert "Division by zero" in body["error"]

def test_missing_fields():
    event = {"numerator": 10}
    resp = lambda_handler(event, None)
    body = json.loads(resp["body"])
    assert resp["statusCode"] == 400
    assert "must be provided" in body["error"]
