from django.db import models
from django.contrib.auth.models import User

class About(models.Model):
    image = models.CharField(max_length=191, null=True)
    title = models.CharField(max_length=191, null=False)
    description = models.TextField(blank = True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['image']),
            models.Index(fields=['title']),
            models.Index(fields=['is_published']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class CategoryArticle(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class CategoryFaq(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class CategoryProduct(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class CategoryProject(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Content(models.Model):
    key_name = models.CharField(max_length=64)
    key_value = models.TextField(blank = True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['key_name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    code = models.CharField(max_length=191, null=True)
    token = models.CharField(max_length=191, null=True)
    email_confirmed = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)
    expired_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['code']),
            models.Index(fields=['token']),
            models.Index(fields=['email_confirmed']),
            models.Index(fields=['is_expired']),
            models.Index(fields=['expired_at']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    categories = models.ManyToManyField(CategoryArticle, related_name='categories')
    image = models.CharField(max_length=191, null=True)
    slug = models.CharField(max_length=191, null=False)
    title = models.CharField(max_length=191, null=False)
    content = models.TextField(null=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['image']),
            models.Index(fields=['slug']),
            models.Index(fields=['title']),
            models.Index(fields=['is_published']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
        
class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['article_id']),
            models.Index(fields=['user_id']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]

class Country(models.Model):
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    phone = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=64, null=True)
    zip_code = models.CharField(max_length=64, null=True)
    address1 = models.TextField(null=True)
    address2 = models.TextField(null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['phone']),
            models.Index(fields=['city']),
            models.Index(fields=['zip_code']),
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]

class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=64,null=True)
    website = models.CharField(max_length=64,null=True)
    address = models.TextField(blank = True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['email']),
            models.Index(fields=['phone']),
            models.Index(fields=['website']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Faq(models.Model):
    category = models.ForeignKey(CategoryFaq, on_delete=models.DO_NOTHING, null=False)
    question = models.CharField(max_length=64)
    answer = models.TextField(blank = True)
    sort = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['category_id']),
            models.Index(fields=['question']),
            models.Index(fields=['sort']),
            models.Index(fields=['is_published']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Feature(models.Model):
    icon = models.CharField(max_length=191,null=True)
    title = models.CharField(max_length=191,null=True)
    description = models.TextField(blank = True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['icon']),
            models.Index(fields=['title']),
            models.Index(fields=['is_published']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Message(models.Model):
    full_name = models.CharField(max_length=191,null=True)
    email = models.CharField(max_length=191,null=True)
    phone = models.CharField(max_length=191,null=True)
    message = models.TextField(blank = True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['full_name']),
            models.Index(fields=['email']),
            models.Index(fields=['phone']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    subject = models.CharField(max_length=191,null=True)
    sort_content = models.CharField(max_length=191,null=True)
    full_content = models.TextField(blank = True)
    readed_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['subject']),
            models.Index(fields=['sort_content']),
            models.Index(fields=['readed_at']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Product(models.Model):
    category = models.ForeignKey(CategoryProduct, on_delete=models.DO_NOTHING, null=False)
    name = models.CharField(max_length=191,null=True)
    image = models.CharField(max_length=191,null=True)
    price = models.FloatField(default=0)
    description = models.TextField(blank = True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['category_id']),
            models.Index(fields=['name']),
            models.Index(fields=['image']),
            models.Index(fields=['price']),
            models.Index(fields=['is_published']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Project(models.Model):
    category = models.ForeignKey(CategoryProject, on_delete=models.DO_NOTHING, null=False)
    name = models.CharField(max_length=191,null=True)
    image = models.CharField(max_length=191,null=True)
    description = models.TextField(blank = True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['category_id']),
            models.Index(fields=['name']),
            models.Index(fields=['image']),
            models.Index(fields=['is_published']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]
    
class Team(models.Model):
    name = models.CharField(max_length=191,null=True)
    image = models.CharField(max_length=191,null=True)
    position = models.CharField(max_length=191,null=True)
    description = models.TextField(blank = True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    class Meta():
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['image']),
            models.Index(fields=['position']),
            models.Index(fields=['is_published']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at'])
        ]