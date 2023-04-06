from flask_sqlalchemy import SQLAlchemy, session
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)

    @validates('name')
    def validate_name(self,key,name):
        names = db.session.query(Author.name).all()
        if not name:
            raise ValueError("Name field is required.")
        elif name in names:
            raise ValueError("Name must be unique.")
        return name
    
    @validates('phone number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("Phone number must be 10 digits.")
        return phone_number

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable = False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)

    @validates('title')
    def validate_title(self,key,title):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in title for substring in clickbait):
            raise ValueError("You must have a title")
        return title

    @validates('content')
    def validate_content(self,key,content):
        if(key == 'content'):
            if len(content) <= 250:
                raise ValueError("Content must be at least 250 characters long.")
            return content
    @validates('summary')
    def validate_summary(self,key,summary):
        if (key == 'summary'):
            if len(summary) >= 250:
                raise ValueError("Summary must be a maximum of 250 characters long.")
            return summary
    @validates('category')
    def validates_category(self,key,category):
        if category != 'Fiction' and category != 'Non-Fiction':
            raise ValueError("Category must be Fiction or Non-Fiction.")
        return category