# Deployment Guide for Elle & Olyv Baking Co. Website

## Prerequisites
Before deploying, ensure you have:
1. All project files from the repository
2. A PostgreSQL database (for storing user and order data)
3. The following environment variables:
   - `SESSION_SECRET` - For Flask session security
   - `DATABASE_URL` - Your PostgreSQL database connection string

## Option 1: Heroku Deployment

### Steps:
1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create a new Heroku app:
```bash
heroku create your-app-name
```

3. Add required files:

Create `Procfile`:
```
web: gunicorn main:app
```

4. Set environment variables:
```bash
heroku config:set SESSION_SECRET=your_secret_key
heroku config:set DATABASE_URL=your_database_url
```

5. Deploy:
```bash
git push heroku main
```

## Option 2: DigitalOcean App Platform

1. Create a DigitalOcean account
2. From the control panel, select "Apps" → "Create App"
3. Connect your repository
4. Configure environment variables:
   - Add `SESSION_SECRET`
   - Add `DATABASE_URL`
5. Select deployment branch
6. Deploy your app

## Option 3: AWS Elastic Beanstalk

1. Create an AWS account
2. Install AWS EB CLI
3. Initialize EB project:
```bash
eb init -p python-3.11 your-app-name
```

4. Create `.ebextensions/01_flask.config`:
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: main:app
  aws:elasticbeanstalk:application:environment:
    SESSION_SECRET: your_secret_key
    DATABASE_URL: your_database_url
```

5. Create and deploy:
```bash
eb create your-environment-name
```

## Option 4: PythonAnywhere

1. Create a PythonAnywhere account
2. Upload your code via Git or direct upload
3. Create a new web app:
   - Choose manual configuration
   - Select Python 3.11

4. Configure virtual environment:
```bash
mkvirtualenv --python=/usr/bin/python3.11 myenv
pip install -r requirements.txt
```

5. Set up WSGI file:
```python
import sys
path = '/home/yourusername/your-app-directory'
if path not in sys.path:
    sys.path.append(path)

import os
os.environ['SESSION_SECRET'] = 'your_secret_key'
os.environ['DATABASE_URL'] = 'your_database_url'

from main import app as application
```

6. Configure web app settings in PythonAnywhere dashboard

## General Deployment Tips

1. Security Considerations:
   - Always use HTTPS
   - Keep secret keys secure
   - Use environment variables for sensitive data
   - Enable CSRF protection

2. Database Migration:
   - Backup your local database
   - Create new database in production
   - Run migrations on production database

3. Static Files:
   - Configure static file serving
   - Consider using a CDN for images and assets

4. Domain Setup:
   - Purchase a domain name
   - Configure DNS settings
   - Set up SSL certificate

5. Monitoring:
   - Set up error logging
   - Monitor server resources
   - Configure health checks

## Troubleshooting

Common issues and solutions:

1. Database Connection:
   - Verify DATABASE_URL format
   - Check database credentials
   - Ensure database is accessible from host

2. Static Files Not Loading:
   - Check static file configuration
   - Verify file permissions
   - Clear browser cache

3. Application Errors:
   - Check application logs
   - Verify environment variables
   - Test database connectivity

4. Performance Issues:
   - Enable caching
   - Optimize database queries
   - Configure proper scaling

Remember to always test your deployment in a staging environment before going live with production traffic.
