
from pprint import pprint

from app.db import BaseModel

class Product(BaseModel):

    SHEET_NAME = "products"

#这里要改
    COLUMNS = ["name", "date", "description", "url"]

#这里要改

    SEEDS = [
        {
            'name': 'Mobile Health Clinics',
            'description': 'Mobile clinics that travel to underserved areas, providing essential medical services ranging from primary care to emergency interventions.',
            'url': 'https://www.wdtn.com/wp-content/uploads/sites/45/2023/01/Mobile-Clinic-Premier-Health.jpg?w=1280'
        },
        {
            'name': 'Health Education Workshops',
            'description': 'Educate communities on preventive healthcare, nutritional best practices, and disease management, empowering individuals to take charge of their health.',
            'url': 'https://operationeyesight.com/wp-content/uploads/2022/09/20220913-CHWs-and-Project-coordinator-conducting-health-education-sesssions-for-local-community.jpg'
        },
        {
            'name': 'Vaccination Drives',
            'description': 'Vaccination drives to prevent the spread of infectious diseases, prioritizing the most vulnerable populations.',
            'url': 'https://cdn1.internationalsos.com/-/jssmedia/images/igo-papua-vaccination-case-study-desktop.jpg?h=1080&iar=0&w=1920&rev=b5576b32588b42d69677b6f8ff09eb70&hash=4BDB4E5F314900433CF6E7A96892D24E'
        },
        {
            'name': 'Community Service',
            'description': 'Collaborating with local organizations and health departments, we enhance our reach and impact, ensuring that resources are utilized efficiently and effectively.',
            'url': 'https://idahofoodbank.org/wp-content/uploads/2022/07/community-health-worker-opt.jpg'
        }
    
           ]



if __name__ == "__main__":

    print("------------")
    print("EXISTING RECORDS:")
    products = Product.all()
    print("FOUND", len(products), "PRODUCTS:")
    if any(products):
        for product in products:
            #breakpoint()
            pprint(dict(product))
    else:
        #if input("Seed products? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Product.seed()
        print("SEEDING RECORDS...")
        Product.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    product = Product.find(1)
    print(product.name)

    print("------------")
    print("FILTERING RECORDS...")
    matches = Product.where(name="Mobile Health Clinics") #要改
    print(len(matches))
    product = matches[0]
    print(product.name)

    print("------------")
    print("CREATING NEW PRODUCT...")
    params = {
        "name": "Community Service", #要改
        "date":"December/05/2026", #要改
        "description":"Collaborating with local organizations and health departments, we enhance our reach and impact, ensuring that resources are utilized efficiently and effectively.",
        "url": "https://idahofoodbank.org/wp-content/uploads/2022/07/community-health-worker-opt.jpg"
    }
    Product.create(params)
