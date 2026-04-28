import numpy as np
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import pickle
import warnings
import joblib
import os
import sys
from pathlib import Path
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
from auth import log_admin_action

# Load environment variables
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent

# Suppress all sklearn warnings
warnings.filterwarnings('ignore')
os.environ['SKLEARN_ENABLE_TAGS_CHECKING'] = '0'

# Custom warning filter for sklearn
import sklearn
from sklearn import __version__ as sklearn_version

# Monkey patch to suppress monotonic_cst warning
import sklearn.tree._classes as tree_classes
if not hasattr(tree_classes.DecisionTreeClassifier, 'monotonic_cst'):
    tree_classes.DecisionTreeClassifier.monotonic_cst = None

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'placement-prediction-ml-2026-secret')

database_url = os.getenv('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url or f"sqlite:///{(BASE_DIR / 'placement_users.db').as_posix()}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# ============================================================================
# MONGODB CONNECTION
# ============================================================================
MONGO_URI = os.getenv('MONGO_URI')
if MONGO_URI:
    try:
        mongo_client = MongoClient(MONGO_URI)
        mongo_db = mongo_client['placement_prediction']
        user_profiles = mongo_db['user_profiles']
        predictions_collection = mongo_db['predictions']
        print("✓ Connected to MongoDB Atlas successfully")
    except Exception as e:
        print(f"⚠ MongoDB connection failed: {e}")
        mongo_client = None
        mongo_db = None
        user_profiles = None
        predictions_collection = None
else:
    print("⚠ MONGO_URI not found in environment variables")
    mongo_client = None
    mongo_db = None
    user_profiles = None
    predictions_collection = None

# Feature names for models
PLACEMENT_FEATURES = ['CGPA', 'Major Projects', 'Workshops/Certificatios', 'Mini Projects',
                      'Skills', 'Communication Skill Rating', 'Internship', 'Hackathon',
                      '12th Percentage', '10th Percentage', 'backlogs']

SALARY_FEATURES = ['CGPA', 'Major Projects', 'Workshops/Certificatios', 'Mini Projects',
                   'Skills', 'Communication Skill Rating', 'Internship', 'Hackathon',
                   '12th Percentage', '10th Percentage', 'backlogs', 'PlacementStatus']

# ============================================================================
# DATABASE MODELS
# ============================================================================

class User(UserMixin, db.Model):
    """User model for student accounts"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    predictions = db.relationship('Prediction', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Admin(UserMixin, db.Model):
    """Admin model for admin accounts"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Prediction(db.Model):
    """Store user predictions"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cgpa = db.Column(db.Float)
    projects = db.Column(db.Float)
    workshops = db.Column(db.Float)
    mini_projects = db.Column(db.Float)
    skills = db.Column(db.String(200))
    communication_skills = db.Column(db.Float)
    internship = db.Column(db.Integer)
    hackathon = db.Column(db.Integer)
    tw_percentage = db.Column(db.Float)
    te_percentage = db.Column(db.Float)
    backlogs = db.Column(db.Integer)
    placement_result = db.Column(db.String(50))
    salary_result = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ============================================================================
# LOAD ML MODELS
# ============================================================================

def load_models():
    model_path = BASE_DIR / 'model.pkl'
    model1_path = BASE_DIR / 'model1.pkl'

    try:
        model = joblib.load(model_path)
        model1 = joblib.load(model1_path)
    except Exception as e:
        try:
            model = pickle.load(open(model_path, 'rb'))
            model1 = pickle.load(open(model1_path, 'rb'))
        except Exception as e2:
            print(f"Error loading models: {e}, {e2}")
            model = None
            model1 = None
    return model, model1

model, model1 = load_models()

# ============================================================================
# RECOMMENDATIONS FUNCTION
# ============================================================================

def generate_recommendations(cgpa, projects, workshops, mini_projects, skills_count, 
                            communication_skills, internship_num, hackathon_num,
                            tw_percentage, te_percentage, backlogs, placement_result):
    """Generate personalized improvement recommendations based on training data insights"""
    recommendations = []
    
    # CGPA recommendations
    if cgpa < 6.0:
        recommendations.append({
            'title': '📚 Improve CGPA',
            'description': f'Your CGPA is {cgpa}. Target: 7.0+',
            'impact': 'High - CGPA is a key placement factor',
            'action': 'Focus on consistent academic performance'
        })
    elif cgpa < 7.0:
        recommendations.append({
            'title': '📚 Boost CGPA Further',
            'description': f'Your CGPA is {cgpa}. Target: 7.5+',
            'impact': 'Medium - Can improve placement chances',
            'action': 'Aim for excellent grades in remaining semesters'
        })
    
    # Projects recommendations
    if projects < 2:
        recommendations.append({
            'title': '🛠️ Increase Major Projects',
            'description': f'You have {int(projects)} major project(s). Target: 2+',
            'impact': 'High - Demonstrates practical skills',
            'action': 'Work on at least 2 substantial projects'
        })
    
    # Workshops/Certifications recommendations
    if workshops < 2:
        recommendations.append({
            'title': '🎓 Take More Workshops/Certifications',
            'description': f'You have attended {int(workshops)} workshop(s). Target: 2+',
            'impact': 'High - Shows dedication to learning',
            'action': 'Complete online certifications or attend workshops'
        })
    
    # Mini Projects recommendations
    if mini_projects < 1:
        recommendations.append({
            'title': '💡 Start Mini Projects',
            'description': f'You have {int(mini_projects)} mini project(s). Target: 3+',
            'impact': 'High - Shows consistent project work',
            'action': 'Work on small but meaningful projects'
        })
    
    # Skills recommendations
    if skills_count < 3:
        recommendations.append({
            'title': '⚙️ Develop More Technical Skills',
            'description': f'You have {int(skills_count)} skill(s). Target: 4+',
            'impact': 'High - Multiple skills increase employability',
            'action': 'Learn Python, Java, SQL, JavaScript, etc.'
        })
    
    # Communication Skills recommendations
    if communication_skills < 7:
        recommendations.append({
            'title': '🗣️ Improve Communication Skills',
            'description': f'Your communication rating is {communication_skills}/10. Target: 8/10',
            'impact': 'High - Critical for interviews and placements',
            'action': 'Practice public speaking, join Toastmasters'
        })
    
    # Internship recommendations
    if internship_num == 0:
        recommendations.append({
            'title': '💼 Pursue Internship Experience',
            'description': 'You don\'t have internship experience',
            'impact': 'Very High - Industry experience is crucial',
            'action': 'Apply for summer/winter internships'
        })
    
    # Hackathon recommendations
    if hackathon_num == 0:
        recommendations.append({
            'title': '🏆 Participate in Hackathons',
            'description': 'You haven\'t participated in hackathons',
            'impact': 'High - Shows innovation and teamwork',
            'action': 'Join hackathon events on platforms like HackerEarth'
        })
    
    # Board percentage recommendations
    if tw_percentage < 75:
        recommendations.append({
            'title': '📖 Strengthen 12th Board Performance',
            'description': f'Your 12th percentage is {tw_percentage}%. Target: 80%+',
            'impact': 'Medium - Some companies check board scores',
            'action': 'Focus on core subjects and regular practice'
        })
    
    if te_percentage < 75:
        recommendations.append({
            'title': '📖 Strengthen 10th Board Performance',
            'description': f'Your 10th percentage is {te_percentage}%. Target: 80%+',
            'impact': 'Medium - Some companies check board scores',
            'action': 'Focus on core subjects and regular practice'
        })
    
    # Backlogs recommendations
    if backlogs > 0:
        recommendations.append({
            'title': '⚠️ Clear Your Backlogs',
            'description': f'You have {int(backlogs)} backlog(s). Target: 0',
            'impact': 'Very High - Many companies reject candidates with backlogs',
            'action': 'Clear all pending exams immediately'
        })
    
    # Positive recommendations
    if placement_result == 'Placed':
        recommendations.append({
            'title': '🎉 Great Job!',
            'description': 'Your profile is strong for placements',
            'impact': 'You are well-positioned for job offers',
            'action': 'Continue improving and apply to more companies'
        })
    else:
        if len(recommendations) == 0:
            recommendations.append({
                'title': '⚡ Quick Wins Needed',
                'description': 'Focus on improving multiple areas',
                'impact': 'Comprehensive improvement can change placement chances',
                'action': 'Prioritize the recommendations above'
            })
    
    return recommendations

# ============================================================================
# LOGIN MANAGER
# ============================================================================

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ============================================================================
# PUBLIC ROUTES
# ============================================================================

@app.route('/')
def h():
    """Home page"""
    return render_template('home_professional.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

# ============================================================================
# AUTHENTICATION ROUTES
# ============================================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not username or not email or not password:
            flash('All fields are required!', 'danger')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register_professional.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('user_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user, remember=True)
            flash(f'Welcome back, {username}!', 'success')
            return redirect(url_for('user_dashboard'))
        else:
            flash('Invalid username or password!', 'danger')
    
    return render_template('login_professional.html')


@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    """Admin login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and admin.check_password(password):
            session['admin_id'] = admin.id
            session['admin_username'] = admin.username
            # Log successful admin login
            try:
                log_admin_action(mongo_db, str(admin.id), 'admin_login', f'Admin {username} logged in')
            except Exception as e:
                print(f"Warning: Failed to log admin login: {e}")
            flash(f'Welcome Admin, {username}!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            # Log failed login attempt
            try:
                log_admin_action(mongo_db, 'unknown', 'failed_login_attempt', f'Failed login attempt for username: {username}')
            except Exception as e:
                print(f"Warning: Failed to log failed login: {e}")
            flash('Invalid admin credentials!', 'danger')
    
    return render_template('admin_login.html')


@app.route('/logout')
@login_required
def logout():
    """User logout"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('h'))


@app.route('/admin-logout')
def admin_logout():
    """Admin logout"""
    admin_id = session.get('admin_id')
    admin_username = session.get('admin_username')
    
    session.pop('admin_id', None)
    session.pop('admin_username', None)
    
    # Log admin logout
    try:
        if admin_id and admin_username:
            log_admin_action(mongo_db, str(admin_id), 'admin_logout', f'Admin {admin_username} logged out')
    except Exception as e:
        print(f"Warning: Failed to log admin logout: {e}")
    
    flash('Admin logged out.', 'info')
    return redirect(url_for('h'))

# ============================================================================
# USER DASHBOARD & PREDICTION
# ============================================================================

@app.route('/dashboard')
@login_required
def user_dashboard():
    """User dashboard with details from MongoDB"""
    # Get user predictions from SQLite
    user_predictions = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.created_at.desc()).all()
    
    # Try to fetch user details from MongoDB
    user_details = None
    if user_profiles is not None:
        try:
            user_details = user_profiles.find_one({'user_id': current_user.id})
            if not user_details:
                # If not found, create a new profile record
                user_details = {
                    'user_id': current_user.id,
                    'username': current_user.username,
                    'email': current_user.email,
                    'created_at': current_user.created_at,
                    'total_predictions': len(user_predictions),
                    'placed_count': len([p for p in user_predictions if p.placement_result == 'Placed']),
                    'not_placed_count': len([p for p in user_predictions if p.placement_result == 'Not Placed']),
                }
                # Insert the profile into MongoDB
                user_profiles.insert_one(user_details)
        except Exception as e:
            print(f"Error fetching from MongoDB: {e}")
            user_details = None
    
    # Calculate statistics
    stats = {
        'total_predictions': len(user_predictions),
        'placed': len([p for p in user_predictions if p.placement_result == 'Placed']),
        'not_placed': len([p for p in user_predictions if p.placement_result == 'Not Placed']),
        'avg_salary': round(sum([p.salary_result for p in user_predictions if p.salary_result]) / len([p for p in user_predictions if p.salary_result]), 2) if any(p.salary_result for p in user_predictions) else 0
    }
    
    return render_template('user_dashboard.html', 
                         predictions=user_predictions,
                         user_details=user_details,
                         stats=stats)


@app.route('/profile')
@login_required
def profile():
    """User profile page"""
    return render_template('user_profile.html', user=current_user)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Make placement prediction - Public access"""
    # If GET request with no parameters, show the form
    if request.method == 'GET' and not request.args:
        return render_template('index.html')
    
    try:
        # Handle both GET and POST requests
        if request.method == 'POST':
            cgpa = float(request.form.get('cgpa', '0'))
            projects = float(request.form.get('projects', '0'))
            workshops = float(request.form.get('workshops', '0'))
            mini_projects = float(request.form.get('mini_projects', '0'))
            skills = request.form.get('skills', '')
            communication_skills = float(request.form.get('communication_skills', '0'))
            internship = request.form.get('internship', 'No').lower()
            hackathon = request.form.get('hackathon', 'No').lower()
            tw_percentage = float(request.form.get('tw_percentage', '0'))
            te_percentage = float(request.form.get('te_percentage', '0'))
            backlogs = float(request.form.get('backlogs', '0'))
            name = request.form.get('name', 'User')
        else:
            # GET request with parameters
            cgpa = float(request.args.get('cgpa', '0'))
            projects = float(request.args.get('projects', '0'))
            workshops = float(request.args.get('workshops', '0'))
            mini_projects = float(request.args.get('mini_projects', '0'))
            skills = request.args.get('skills', '')
            communication_skills = float(request.args.get('communication_skills', '0'))
            internship = request.args.get('internship', 'No').lower()
            hackathon = request.args.get('hackathon', 'No').lower()
            tw_percentage = float(request.args.get('tw_percentage', '0'))
            te_percentage = float(request.args.get('te_percentage', '0'))
            backlogs = float(request.args.get('backlogs', '0'))
            name = request.args.get('name', 'User')
        
        # Count skills from comma-separated values
        skills_count = len([s for s in skills.split(',') if s.strip()]) if skills.strip() else 0
        
        # Convert internship and hackathon to numeric
        internship_num = 1 if internship in ['yes', 'y', '1', 'true'] else 0
        hackathon_num = 1 if hackathon in ['yes', 'y', '1', 'true'] else 0
        
        # Create DataFrame for placement prediction
        placement_data = pd.DataFrame([[
            cgpa, projects, workshops, mini_projects, skills_count,
            communication_skills, internship_num, hackathon_num,
            tw_percentage, te_percentage, backlogs
        ]], columns=PLACEMENT_FEATURES)
        
        # Predict placement
        output = model.predict(placement_data)[0]
        
        # Convert placement to numeric for salary model
        placement_numeric = 1 if output == 'Placed' else 0
        
        # Create DataFrame for salary prediction
        salary_data = pd.DataFrame([[
            cgpa, projects, workshops, mini_projects, skills_count,
            communication_skills, internship_num, hackathon_num,
            tw_percentage, te_percentage, backlogs, placement_numeric
        ]], columns=SALARY_FEATURES)
        
        # Predict salary
        salary = model1.predict(salary_data)[0]
        
        # Format salary with commas
        salary_str = f"{int(salary):,}"
        
        # Save prediction to database only if user is logged in
        if current_user and current_user.is_authenticated:
            try:
                prediction = Prediction(
                    user_id=current_user.id,
                    cgpa=cgpa,
                    projects=projects,
                    workshops=workshops,
                    mini_projects=mini_projects,
                    skills=skills,
                    communication_skills=communication_skills,
                    internship=internship_num,
                    hackathon=hackathon_num,
                    tw_percentage=tw_percentage,
                    te_percentage=te_percentage,
                    backlogs=int(backlogs),
                    placement_result=output,
                    salary_result=salary
                )
                db.session.add(prediction)
                db.session.commit()
            except Exception as db_error:
                print(f"Warning: Could not save prediction to database: {db_error}")
                db.session.rollback()
        
        if output == 'Placed':
            out = f'Congratulations {name}!! You have high chances of getting placed!!!'
            out2 = f'Your Expected Salary will be INR {salary_str} per annum'
        else:
            out = f'Sorry {name}!! You have low chances of getting placed. All the best!!!!'
            out2 = 'Improve your skills...'
        
        # Generate recommendations
        recommendations = generate_recommendations(cgpa, projects, workshops, mini_projects, 
                                                   skills_count, communication_skills, 
                                                   internship_num, hackathon_num,
                                                   tw_percentage, te_percentage, backlogs, output)
        
        return render_template('output.html', 
                             output=out, 
                             output2=out2,
                             student_name=name,
                             cgpa=cgpa,
                             projects=int(projects),
                             backlogs=int(backlogs),
                             internship='Yes' if internship_num == 1 else 'No',
                             hackathon='Yes' if hackathon_num == 1 else 'No',
                             workshops=int(workshops),
                             mini_projects=int(mini_projects),
                             communication_skills=int(communication_skills),
                             recommendations=recommendations)
        
    except Exception as e:
        print(f"Error in predict: {e}")
        import traceback
        traceback.print_exc()
        flash(f'Prediction error: {str(e)}', 'danger')
        if current_user and current_user.is_authenticated:
            return redirect(url_for('user_dashboard'))
        else:
            return redirect(url_for('h'))


@app.route('/prediction-form')
@login_required
def prediction_form():
    """Prediction form page"""
    return render_template('index.html')

# ============================================================================
# ADMIN DASHBOARD
# ============================================================================

@app.route('/admin-dashboard')
def admin_dashboard():
    """Admin dashboard"""
    if 'admin_id' not in session:
        flash('Please log in as admin!', 'warning')
        return redirect(url_for('admin_login'))
    
    total_users = User.query.count()
    total_predictions = Prediction.query.count()
    recent_predictions = Prediction.query.order_by(Prediction.created_at.desc()).limit(10).all()
    
    # Calculate placement success rate
    placed = Prediction.query.filter(Prediction.placement_result == 'Placed').count()
    placement_rate = (placed / total_predictions * 100) if total_predictions > 0 else 0
    
    # Average salary for placed students
    placed_predictions = Prediction.query.filter(Prediction.placement_result == 'Placed').all()
    avg_salary = sum(p.salary_result for p in placed_predictions) / len(placed_predictions) if placed_predictions else 0
    
    return render_template('admin_dashboard.html', 
                         total_users=total_users,
                         total_predictions=total_predictions,
                         placement_rate=round(placement_rate, 2),
                         avg_salary=int(avg_salary),
                         recent_predictions=recent_predictions)


@app.route('/admin-users')
def admin_users():
    """View all users (admin only)"""
    if 'admin_id' not in session:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('admin_login'))
    
    users = User.query.all()
    return render_template('admin_users.html', users=users)


@app.route('/admin-users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """Delete a user (admin only)"""
    if 'admin_id' not in session:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('admin_login'))
    
    try:
        user = User.query.get(user_id)
        if not user:
            flash('User not found!', 'danger')
            return redirect(url_for('admin_users'))
        
        # Delete all predictions for this user
        Prediction.query.filter_by(user_id=user_id).delete()
        
        # Delete the user
        db.session.delete(user)
        db.session.commit()
        
        flash(f'User "{user.username}" deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting user: {str(e)}', 'danger')
    
    return redirect(url_for('admin_users'))


@app.route('/admin-predictions')
def admin_predictions():
    """View all predictions (admin only)"""
    if 'admin_id' not in session:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('admin_login'))
    
    predictions = Prediction.query.order_by(Prediction.created_at.desc()).all()
    return render_template('admin_predictions.html', predictions=predictions)


@app.route('/admin-predictions/delete/<int:prediction_id>', methods=['POST'])
def delete_prediction(prediction_id):
    """Delete a prediction (admin only)"""
    if 'admin_id' not in session:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('admin_login'))
    
    try:
        prediction = Prediction.query.get(prediction_id)
        if not prediction:
            flash('Prediction not found!', 'danger')
            return redirect(url_for('admin_predictions'))
        
        db.session.delete(prediction)
        db.session.commit()
        
        flash('Prediction deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting prediction: {str(e)}', 'danger')
    
    return redirect(url_for('admin_predictions'))


@app.route('/admin-logs')
def admin_logs():
    """View admin activity logs"""
    if 'admin_id' not in session:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('admin_login'))
    
    try:
        # Get page number from query parameters (default to 1)
        page = request.args.get('page', 1, type=int)
        logs_per_page = 20
        
        # Get admin_logs collection
        admin_logs_collection = mongo_db['admin_logs']
        
        # Get total number of logs
        total_logs = admin_logs_collection.count_documents({})
        
        # Calculate pagination
        total_pages = (total_logs + logs_per_page - 1) // logs_per_page
        skip = (page - 1) * logs_per_page
        
        # Validate page number
        if page < 1:
            page = 1
        if page > total_pages and total_pages > 0:
            page = total_pages
        
        # Fetch logs sorted by timestamp (newest first)
        logs_cursor = admin_logs_collection.find().sort('timestamp', -1).skip(skip).limit(logs_per_page)
        logs = list(logs_cursor)
        
        # Convert ObjectId to string for display if needed
        for log in logs:
            if '_id' in log:
                log['_id'] = str(log['_id'])
        
        return render_template('admin_logs.html', 
                             logs=logs, 
                             total_logs=total_logs,
                             current_page=page,
                             total_pages=total_pages)
    
    except Exception as e:
        error_msg = f"Error fetching logs: {str(e)}"
        return render_template('admin_logs.html', 
                             logs=[], 
                             total_logs=0,
                             current_page=1,
                             total_pages=1,
                             error=error_msg)


@app.route('/admin-profile')
def admin_profile():
    """Admin profile page"""
    if 'admin_id' not in session:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('admin_login'))
    
    # Get admin from database
    admin = Admin.query.get(session['admin_id'])
    
    if not admin:
        flash('Admin not found!', 'danger')
        return redirect(url_for('admin_login'))
    
    return render_template('admin_profile.html', admin=admin)


@app.route('/create-admin', methods=['GET', 'POST'])
def create_admin():
    """Create new admin account"""
    if 'admin_id' not in session:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not username or not email or not password:
            flash('All fields are required!', 'danger')
            return redirect(url_for('create_admin'))
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('create_admin'))
        
        if Admin.query.filter_by(username=username).first():
            flash('Admin username already exists!', 'danger')
            return redirect(url_for('create_admin'))
        
        if Admin.query.filter_by(email=email).first():
            flash('Admin email already registered!', 'danger')
            return redirect(url_for('create_admin'))
        
        # Create new admin
        admin = Admin(username=username, email=email)
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        
        # Log admin creation
        try:
            creator_id = session.get('admin_id')
            creator_username = session.get('admin_username')
            log_admin_action(mongo_db, str(creator_id), 'create_admin', 
                           f'Admin {creator_username} created new admin account: {username}')
        except Exception as e:
            print(f"Warning: Failed to log admin creation: {e}")
        
        flash(f'New admin account "{username}" created successfully!', 'success')
        return redirect(url_for('create_admin'))
    
    return render_template('create_admin.html')

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500

# ============================================================================
# INITIALIZE DATABASE
# ============================================================================

with app.app_context():
    db.create_all()
    
    # Create default admin if not exists
    if not Admin.query.filter_by(username='admin').first():
        admin = Admin(username='admin', email='admin@placement.com')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("Default admin created. Username: admin, Password: admin123")

# ============================================================================
# RUN APP
# ============================================================================

if __name__ == "__main__":
    app.run(debug=True)