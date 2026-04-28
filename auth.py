from functools import wraps
from flask import redirect, url_for, session, request, abort
from models import User
from bson.objectid import ObjectId

def login_required(f):
    """Decorator to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator to require admin role"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login', next=request.url))
        if session.get('role') != 'admin':
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return decorated_function

def get_current_user(db):
    """Get current logged-in user"""
    if 'user_id' not in session:
        return None
    try:
        user_data = db['users'].find_one({'_id': ObjectId(session['user_id'])})
        if user_data:
            return User.from_dict(user_data)
    except:
        pass
    return None

def create_user(db, username, email, password, role='user'):
    """Create a new user in database"""
    if db['users'].find_one({'username': username}):
        return {'success': False, 'message': 'Username already exists'}
    
    if db['users'].find_one({'email': email}):
        return {'success': False, 'message': 'Email already exists'}
    
    user = User(username, email, role=role)
    user.set_password(password)
    
    result = db['users'].insert_one(user.to_dict())
    return {'success': True, 'message': 'User created successfully', 'user_id': str(result.inserted_id)}

def authenticate_user(db, username, password):
    """Authenticate user with username and password"""
    user_data = db['users'].find_one({'username': username})
    
    if not user_data:
        return {'success': False, 'message': 'Invalid username or password'}
    
    user = User.from_dict(user_data)
    
    if not user.check_password(password):
        return {'success': False, 'message': 'Invalid username or password'}
    
    return {'success': True, 'user': user}

def log_admin_action(db, admin_id, action, details):
    """Log admin activity"""
    from models import AdminLog
    log = AdminLog(admin_id, action, details)
    db['admin_logs'].insert_one(log.to_dict())
