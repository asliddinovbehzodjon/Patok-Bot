BASE_URL = "http://127.0.0.1:8000/api/v1"
import requests
import json
def create_worker(name,age,salary,phone,address,contact_time,about,job,aim):
    url = f"{BASE_URL}/worker/"
    rest= requests.post(url=url,data={
        "name":name,
        "age":age,
        "salary":salary,
        "phone":phone,
        "address":address,
        "contact_time":contact_time,
        "about":about,
        "job":job,
        "aim":aim

    })
    return 'Ok'
def create_work(company,job,phone,salary,address,contact_time,work_time,requirements):
    url = f"{BASE_URL}/work/"
    requests.post(url=url,data={
        "company":company,
        "job":job,
        "phone":phone,
        "salary":salary,
        "address":address,
        "contact_time":contact_time,
        "work_time":work_time,
        "requirements":requirements
    })
    return "Ok"