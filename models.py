from pymongo import MongoClient
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from bson.objectid import ObjectId

class Database:
    """MongoDB Database Handler"""
    def __init__(self, mongo_uri):
        self.client = MongoClient(mongo_uri)
        self.db = self.client['placement_prediction']
        
    def get_db(self):
        return self.db

# Collections
class User(UserMixin):
    """User Model"""
    def __init__(self, username, email, password=None, role='user', user_id=None):
        self.id = user_id
        self.username = username
        self.email = email
        self._password = password
        self.role = role
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
    def set_password(self, password):
        self._password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self._password, password)
    
    def to_dict(self):
        data = {
            'username': self.username,
            'email': self.email,
            'password': self._password,
            'role': self.role,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        # Only include _id if it's not None (MongoDB will auto-generate if not provided)
        if self.id is not None:
            data['_id'] = self.id
        return data
    
    @classmethod
    def from_dict(cls, data):
        user = cls(
            username=data.get('username'),
            email=data.get('email'),
            role=data.get('role', 'user'),
            user_id=str(data.get('_id', ''))
        )
        user._password = data.get('password')
        user.created_at = data.get('created_at', datetime.utcnow())
        user.updated_at = data.get('updated_at', datetime.utcnow())
        return user

class PredictionRecord:
    """Prediction Record Model"""
    def __init__(self, user_id, student_name, cgpa, projects, workshops, 
                 mini_projects, skills, communication_skills, internship, 
                 hackathon, tw_percentage, te_percentage, backlogs,
                 placement_prediction, salary_prediction, record_id=None):
        self._id = record_id
        self.user_id = user_id
        self.student_name = student_name
        self.cgpa = cgpa
        self.projects = projects
        self.workshops = workshops
        self.mini_projects = mini_projects
        self.skills = skills
        self.communication_skills = communication_skills
        self.internship = internship
        self.hackathon = hackathon
        self.tw_percentage = tw_percentage
        self.te_percentage = te_percentage
        self.backlogs = backlogs
        self.placement_prediction = placement_prediction
        self.salary_prediction = salary_prediction
        self.created_at = datetime.utcnow()
        
    def to_dict(self):
        data = {
            'user_id': self.user_id,
            'student_name': self.student_name,
            'cgpa': self.cgpa,
            'projects': self.projects,
            'workshops': self.workshops,
            'mini_projects': self.mini_projects,
            'skills': self.skills,
            'communication_skills': self.communication_skills,
            'internship': self.internship,
            'hackathon': self.hackathon,
            'tw_percentage': self.tw_percentage,
            'te_percentage': self.te_percentage,
            'backlogs': self.backlogs,
            'placement_prediction': self.placement_prediction,
            'salary_prediction': self.salary_prediction,
            'created_at': self.created_at
        }
        # Only include _id if it's not None (MongoDB will auto-generate if not provided)
        if self._id is not None:
            data['_id'] = self._id
        return data
    
    @classmethod
    def from_dict(cls, data):
        record = cls(
            user_id=data.get('user_id'),
            student_name=data.get('student_name'),
            cgpa=data.get('cgpa'),
            projects=data.get('projects'),
            workshops=data.get('workshops'),
            mini_projects=data.get('mini_projects'),
            skills=data.get('skills'),
            communication_skills=data.get('communication_skills'),
            internship=data.get('internship'),
            hackathon=data.get('hackathon'),
            tw_percentage=data.get('tw_percentage'),
            te_percentage=data.get('te_percentage'),
            backlogs=data.get('backlogs'),
            placement_prediction=data.get('placement_prediction'),
            salary_prediction=data.get('salary_prediction'),
            record_id=str(data.get('_id', ''))
        )
        record.created_at = data.get('created_at', datetime.utcnow())
        return record

class AdminLog:
    """Admin Activity Log Model"""
    def __init__(self, admin_id, action, details, log_id=None):
        self._id = log_id
        self.admin_id = admin_id
        self.action = action
        self.details = details
        self.timestamp = datetime.utcnow()
        
    def to_dict(self):
        data = {
            'admin_id': self.admin_id,
            'action': self.action,
            'details': self.details,
            'timestamp': self.timestamp
        }
        # Only include _id if it's not None (MongoDB will auto-generate if not provided)
        if self._id is not None:
            data['_id'] = self._id
        return data
