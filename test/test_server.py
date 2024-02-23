import requests
def test_probe():
    
    res =requests.get("http://127.0.0.1:5000")

    assert res.status_code == 200
def test_random():
    res = requests.get("http://127.0.0.1:5000/random_number")
    assert res.status_code == 200
    assert 100>= int(res.text) >= 0
def test_random_in_range():
    res=requests.get("http://127.0.0.1:5000/random_number",params={"min":0,"max":10})
    assert res.status_code == 200
    assert 10>= int(res.text) >= 0
def test_random_with_max_only():
    res=requests.get("http://127.0.0.1:5000/random_number",params={"max":10})
    assert res.status_code == 200
    assert 10>= int(res.text) >= 0
def test_random_with_min_only():
    res=requests.get("http://127.0.0.1:5000/random_number",params={"min":50})
    assert res.status_code == 200
    assert 100>= int(res.text) >= 50

