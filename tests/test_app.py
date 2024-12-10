import json


def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    
def test_courses(client):
    res = client.get('/courses')
    assert res.status_code == 200
    result = json.loads(res.data) 
    assert result["courses"][0]["name"] == "Women in Tech"
    assert result["courses"][0]["location"] == "Manchester"
    assert result["courses"][1]["name"] == "Cyber Security Track Day"
    assert result["courses"][1]["location"] == "Manchester"

def test_add_new_course(client):
    post_dict = {"name": "test_name", "location": "test_location"}
    res = client.post('/courses', json= post_dict)
    assert res.status_code == 200
    result = json.loads(res.data) 
    assert len(result["courses"]) == 3


 
   