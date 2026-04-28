import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://ashmithabhuvaneshwaran07_db_user:5sxDJYqrcFMQOBmF@ml.2dfjelx.mongodb.net/placement_prediction?appName=ML')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = 1800  # 30 minutes

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    MONGO_URI = 'mongodb://localhost:27017/placement_prediction_test'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
