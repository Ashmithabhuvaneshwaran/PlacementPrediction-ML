#!/usr/bin/env python
"""
Placement Prediction ML - Complete Setup & Run Script
This script sets up and starts the entire application
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        sys.exit(1)
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")

def check_dependencies():
    """Check if all required packages are installed"""
    required_packages = [
        'flask', 'scikit-learn', 'pandas', 'numpy', 
        'joblib', 'matplotlib', 'seaborn'
    ]
    
    print("\nChecking dependencies...")
    missing = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} - MISSING")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️  Installing missing packages: {', '.join(missing)}")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q'] + missing)
        print("✓ Dependencies installed")
    else:
        print("✓ All dependencies installed")

def check_models():
    """Verify that trained models exist"""
    print("\nChecking models...")
    
    model_files = ['model.pkl', 'model1.pkl']
    models_ok = True
    
    for model_file in model_files:
        if os.path.exists(model_file):
            size = os.path.getsize(model_file)
            print(f"  ✓ {model_file} ({size:,} bytes)")
        else:
            print(f"  ✗ {model_file} - MISSING")
            models_ok = False
    
    if not models_ok:
        print("\n⚠️  Training models...")
        subprocess.check_call([sys.executable, 'retrain_models.py'])
        print("✓ Models trained successfully")
    
    return models_ok

def check_data_files():
    """Verify that data files exist"""
    print("\nChecking data files...")
    
    data_files = ['Placement_Prediction_data.csv', 'Salary_prediction_data.csv']
    
    for data_file in data_files:
        if os.path.exists(data_file):
            print(f"  ✓ {data_file}")
        else:
            print(f"  ✗ {data_file} - MISSING")
            return False
    
    return True

def check_templates():
    """Verify that template files exist"""
    print("\nChecking templates...")
    
    required_templates = ['home.html', 'about.html', 'index.html', 'output.html']
    templates_dir = 'templates'
    
    if not os.path.exists(templates_dir):
        print(f"  ✗ templates/ directory - MISSING")
        return False
    
    for template in required_templates:
        path = os.path.join(templates_dir, template)
        if os.path.exists(path):
            print(f"  ✓ {template}")
        else:
            print(f"  ✗ {template} - MISSING")
            return False
    
    return True

def verify_app():
    """Run model verification"""
    print("\nVerifying model functionality...")
    
    try:
        import joblib
        import pandas as pd
        import numpy as np
        
        model = joblib.load('model.pkl')
        model1 = joblib.load('model1.pkl')
        
        print(f"  ✓ Placement Model: {model.n_features_in_} features")
        print(f"  ✓ Salary Model: {model1.n_features_in_} features")
        
        # Test with sample data
        test_data = pd.DataFrame([[8.5, 3, 2, 2, 3, 4.0, 1, 1, 80, 85, 0]], 
                                 columns=['CGPA', 'Major Projects', 'Workshops/Certificatios', 
                                         'Mini Projects', 'Skills', 'Communication Skill Rating',
                                         'Internship', 'Hackathon', '12th Percentage', 
                                         '10th Percentage', 'backlogs'])
        
        pred = model.predict(test_data)
        print(f"  ✓ Sample prediction: {pred[0]}")
        
        return True
    except Exception as e:
        print(f"  ✗ Verification failed: {e}")
        return False

def start_flask_app():
    """Start the Flask development server"""
    print("\n" + "="*60)
    print("STARTING FLASK APPLICATION")
    print("="*60)
    
    print("\n✓ Flask server starting on http://127.0.0.1:5000")
    print("✓ Opening browser...")
    
    # Give the server a moment to start
    time.sleep(2)
    
    try:
        webbrowser.open('http://127.0.0.1:5000')
    except:
        print("  ⚠️  Could not open browser automatically")
        print("  Open http://127.0.0.1:5000 manually in your browser")
    
    print("\n" + "="*60)
    print("APPLICATION DETAILS")
    print("="*60)
    print(f"URL: http://127.0.0.1:5000")
    print(f"Host: 127.0.0.1")
    print(f"Port: 5000")
    print(f"Debug Mode: ON")
    print("\nPress CTRL+C to stop the server")
    print("="*60 + "\n")
    
    # Start Flask app
    try:
        from app import app
        app.run(debug=True, use_reloader=True)
    except KeyboardInterrupt:
        print("\n\n✓ Server stopped")

def main():
    """Main setup and run function"""
    print("="*60)
    print("PLACEMENT PREDICTION ML - SETUP & RUN")
    print("="*60)
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Run checks
    check_python_version()
    check_dependencies()
    
    if not check_data_files():
        print("\n❌ Required data files are missing!")
        sys.exit(1)
    
    if not check_templates():
        print("\n❌ Required template files are missing!")
        sys.exit(1)
    
    check_models()
    
    if not verify_app():
        print("\n⚠️  App verification failed, but attempting to start anyway...")
    
    print("\n✓ All checks passed!")
    print("="*60)
    
    # Start the application
    start_flask_app()

if __name__ == '__main__':
    main()
