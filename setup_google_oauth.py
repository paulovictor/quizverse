"""
Script to set up Google OAuth SocialApp in the database.

This script creates or updates the Google OAuth configuration in Django Allauth.

Before running this script, you need to:
1. Create a Google OAuth 2.0 Client ID at https://console.cloud.google.com/
2. Set the following environment variables or pass them as arguments:
   - GOOGLE_CLIENT_ID
   - GOOGLE_CLIENT_SECRET

Run this script with:
    python setup_google_oauth.py
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

def setup_google_oauth(client_id=None, client_secret=None):
    """
    Set up Google OAuth SocialApp.
    
    Args:
        client_id: Google OAuth Client ID (optional, will use env var if not provided)
        client_secret: Google OAuth Client Secret (optional, will use env var if not provided)
    """
    # Get credentials from arguments or environment variables
    client_id = client_id or os.environ.get('GOOGLE_CLIENT_ID')
    client_secret = client_secret or os.environ.get('GOOGLE_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        print("❌ Error: Google OAuth credentials not found!")
        print("\nYou need to provide Google OAuth credentials in one of these ways:")
        print("\n1. Set environment variables:")
        print("   export GOOGLE_CLIENT_ID='your-client-id'")
        print("   export GOOGLE_CLIENT_SECRET='your-client-secret'")
        print("\n2. Or add them to your .env file:")
        print("   GOOGLE_CLIENT_ID=your-client-id")
        print("   GOOGLE_CLIENT_SECRET=your-client-secret")
        print("\n📖 How to get Google OAuth credentials:")
        print("   1. Go to https://console.cloud.google.com/")
        print("   2. Create a new project or select an existing one")
        print("   3. Go to 'APIs & Services' > 'Credentials'")
        print("   4. Click 'Create Credentials' > 'OAuth 2.0 Client ID'")
        print("   5. Configure the consent screen if you haven't already")
        print("   6. Set Application type to 'Web application'")
        print("   7. Add authorized redirect URIs:")
        print("      - http://localhost:8000/accounts/google/login/callback/")
        print("      - http://127.0.0.1:8000/accounts/google/login/callback/")
        print("      - https://yourdomain.com/accounts/google/login/callback/ (for production)")
        print("   8. Copy the Client ID and Client Secret")
        sys.exit(1)
    
    # Get the current site
    site = Site.objects.get_current()
    print(f"📍 Using site: {site.domain} (ID: {site.id})")
    
    # Create or update the Google SocialApp
    social_app, created = SocialApp.objects.get_or_create(
        provider='google',
        defaults={
            'name': 'Google',
            'client_id': client_id,
            'secret': client_secret,
        }
    )
    
    if not created:
        # Update existing app
        social_app.client_id = client_id
        social_app.secret = client_secret
        social_app.save()
        print(f"✅ Updated existing Google OAuth app (ID: {social_app.id})")
    else:
        print(f"✅ Created new Google OAuth app (ID: {social_app.id})")
    
    # Add the site to the social app if not already added
    if site not in social_app.sites.all():
        social_app.sites.add(site)
        print(f"✅ Added site '{site.domain}' to Google OAuth app")
    else:
        print(f"ℹ️  Site '{site.domain}' already linked to Google OAuth app")
    
    print("\n🎉 Google OAuth setup complete!")
    print(f"\n📝 Summary:")
    print(f"   Provider: {social_app.provider}")
    print(f"   Client ID: {client_id[:20]}...")
    print(f"   Sites: {', '.join([s.domain for s in social_app.sites.all()])}")
    print(f"\n🔗 Login URL: http://{site.domain}/accounts/google/login/")
    print("\n⚠️  Remember to configure your authorized redirect URIs in Google Cloud Console:")
    print(f"   - http://{site.domain}/accounts/google/login/callback/")
    
    return social_app

if __name__ == '__main__':
    setup_google_oauth()

