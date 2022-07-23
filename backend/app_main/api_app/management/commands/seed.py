from datetime import datetime
from unicodedata import category
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from api_app.models import *
from datetime import datetime, timezone
from faker import Faker
from pathlib import Path
from slugify import slugify
import json
import random

class Command(BaseCommand):
    
    STRORAGE_PATH = Path(__file__).resolve().parent.parent.parent.parent
    DEFAULT_ADMIN_USERNAME = "admin"
    DEFAULT_ADMIN_EMAIL = "admin@devel.com"
    DEFAULT_PASSWORD = "5ecReT!"
    
    def createUser(self):
        User.objects.all().delete()
        Person.objects.all().delete()
        for _ in range(100):
            fake = Faker()
            username = fake.name().lower().replace(' ', '')
            number = random.randint(0, 1)
            email = fake.email()
            try:
                user = User.objects.create_user(
                    username = username,
                    email= email,
                    password= self.DEFAULT_PASSWORD,
                    first_name = fake.first_name_male() if number == 0 else fake.first_name_female(),
                    last_name = fake.last_name_male() if number == 0 else fake.last_name_female(),
                    is_staff = True
                )
                Person.objects.create(
                    user = user,
                    phone = fake.phone_number(),
                    city = fake.city(),
                    zip_code = fake.zipcode(),
                    address1 = fake.address(),
                    address2 = fake.address(),
                    status = True,
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
            except:
                print()
        # Set As Administrator
        userAdmin = User.objects.order_by('?').first()
        userAdmin.is_superuser = True
        userAdmin.username = self.DEFAULT_ADMIN_USERNAME
        userAdmin.email = self.DEFAULT_ADMIN_EMAIL
        userAdmin.save()
               
                
    def createCountry(self):
        Country.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/countries.json', 'r') as f:
            my_json_obj = json.load(f)
            countries = my_json_obj["ref_country_codes"]
            for item in countries:
                Country.objects.create(
                    code = item["alpha2"],
                    name = item["country"],
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createContact(self):
        Contact.objects.all().delete()
        for _ in range(100):
            fake = Faker()
            Contact.objects.create(
                name = fake.name(),
                email = fake.email(),
                phone = fake.phone_number(),
                website = fake.url(),
                address = fake.address(),
                created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
            )
            
    def createAbout(self):
        About.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/abouts.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                About.objects.create(
                    title = item["title"],
                    description = item["description"],
                    is_published = True,
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createCategoryArticle(self):
        CategoryArticle.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/category_articles.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                CategoryArticle.objects.create(
                    name = item["name"],
                    description = item["description"],
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createCategoryFaq(self):
        CategoryFaq.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/category_faqs.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                CategoryFaq.objects.create(
                    name = item["name"],
                    description = item["description"],
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createCategoryProduct(self):
        CategoryProduct.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/category_products.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                CategoryProduct.objects.create(
                    name = item["name"],
                    description = item["description"],
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createCategoryProject(self):
        CategoryProject.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/category_projects.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                CategoryProject.objects.create(
                    name = item["name"],
                    description = item["description"],
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createContent(self):
        Content.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/contents.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                Content.objects.create(
                    key_name = item["key_name"],
                    key_value = item["key_value"],
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createFeature(self):
        Feature.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/features.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                Feature.objects.create(
                    icon = item["icon"],
                    title = item["title"],
                    description = item["description"],
                    is_published = True,
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createMessage(self):
        Message.objects.all().delete()
        for _ in range(100):
            fake = Faker()
            Message.objects.create(
                full_name = fake.name(),
                email = fake.email(),
                phone = fake.phone_number(),
                message = fake.text(),
                created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
            )
    
    def createTeam(self):
        Team.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/teams.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                Team.objects.create(
                    name = item["name"],
                    position = item["position"],
                    description = item["description"],
                    is_published = True,
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createNotification(self):
        Notification.objects.all().delete()
        for _ in range(100):
            fake = Faker()
            user = User.objects.order_by('?').first()
            Notification.objects.create(
                user = user,
                subject = fake.sentence(),
                sort_content = fake.sentence(),
                full_content = fake.text(),
                created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
            )
    
    def createProduct(self):
        Product.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/products.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                category = CategoryProduct.objects.order_by('?').first()
                Product.objects.create(
                    category = category,
                    name = item["name"],
                    price = item["price"],
                    description = item["description"],
                    is_published = True,
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createProject(self):
        Project.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/projects.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                category = CategoryProject.objects.order_by('?').first()
                Project.objects.create(
                    category = category,
                    name = item["name"],
                    description = item["description"],
                    is_published = True,
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createFaq(self):
        Faq.objects.all().delete()
        with open(str(self.STRORAGE_PATH)+'/storages/json/faqs.json', 'r') as f:
            my_json_obj = json.load(f)
            items = my_json_obj["RECORDS"]
            for item in items:
                category = CategoryFaq.objects.order_by('?').first()
                Faq.objects.create(
                    category = category,
                    question = item["question"],
                    answer = item["answer"],
                    sort = random.randint(1, 10),
                    is_published = True,
                    created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                    updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
                )
    
    def createArticle(self):
        Article.objects.all().delete()
        for _ in range(100):
            fake = Faker()
            user = User.objects.order_by('?').first()
            category = CategoryArticle.objects.order_by('?').first()
            title = fake.sentence()
            article = Article.objects.create(
                user = user,
                title = title,
                content = fake.text(),
                slug = slugify(title),
                is_published = True,
                created_at = datetime.utcnow().replace(tzinfo=timezone.utc),
                updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
            )
            article.categories.add(category)
            
    
    def handle(self, *args, **kwargs):
        print("\nBegin instalation, please wait...")
        self.createContact()
        self.createCountry()
        self.createUser()
        self.createAbout()
        self.createCategoryArticle()
        self.createCategoryFaq()
        self.createCategoryProduct()
        self.createCategoryProject()
        self.createContent()
        self.createFaq()
        self.createFeature()
        self.createMessage()
        self.createNotification()
        self.createProduct()
        self.createProject()
        self.createTeam()
        self.createArticle()
        print("-----------------------------------------")
        print("Admin Username : "+str(self.DEFAULT_ADMIN_USERNAME))
        print("Admin Email : "+str(self.DEFAULT_ADMIN_EMAIL))
        print("Admin Password : "+str(self.DEFAULT_PASSWORD))
        print("-----------------------------------------")
        print("\nInstalaation has been finished :)\n")