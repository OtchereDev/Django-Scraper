
from typing import List
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from pathlib import Path
path = Path().absolute()

filters = [
    "location",
    "created_at",
    "tag",
    "company_name"
]


cred = credentials.Certificate(f"{path}/api/firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

batch = db.batch()

def uploadToFireStore(data:List):
    for data_item in data:
        
        doc_ref = db.collection("Jobs").document(data_item["apply_url"].replace("/","").replace(":",""))
        batch.set(doc_ref, data_item)
    batch.commit()
    return True

# db.collection("Jobs").add(data)

def getCompanyNames():
    documents = db.collection('Jobs')
    docs = documents.stream()
    companys = []
    
    for doc in docs:
        company_name = u'{}'.format(doc.to_dict()["Company Name"])
        companys.append(company_name)

    return companys

def getJobTags():
    documents = db.collection('Jobs')
    docs = documents.stream()
    tags = []
    
    for doc in docs:
        tag = doc.to_dict().get("tags")

        if tag:
            tags.extend(tag)

    tags = set(tags)

    return list(tags)

def filterByField(field:str,value:str):
    documents = db.collection('Jobs')
    docs = documents.stream()
    selected = []
    
    for doc in docs:
        if field == "company_name":
            selected_value = doc.to_dict().get("Company Name")

            if value in selected_value:
                selected.append(doc.to_dict())

        elif field == "tag":
            selected_value = doc.to_dict().get("tags")

            if value in selected_value:
                selected.append(doc.to_dict())

        elif field == "location":
            selected_value = doc.to_dict().get("location")

            if value in selected_value:
                selected.append(doc.to_dict())

        elif field == "salary":
            selected_value = doc.to_dict().get("salary")

            if value in selected_value:
                selected.append(doc.to_dict())
        
        elif field == "created_at":
            selected_value = doc.to_dict().get("created_at")

            if value in selected_value:
                selected.append(doc.to_dict())

        else:
            selected.append(doc.to_dict())

    return selected