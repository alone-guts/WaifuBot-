#!/usr/bin/env python3
"""
Owner Setup Script for TEAMZYRO Bot
Run this script to automatically set yourself as the owner
"""

import os
import sys

def get_user_id():
    """Get user ID from user input"""
    print("🤖 TEAMZYRO Bot Owner Setup")
    print("=" * 40)
    
    while True:
        user_id = input("Enter your Telegram User ID: ").strip()
        
        if user_id.isdigit() and len(user_id) >= 8:
            return user_id
        else:
            print("❌ Invalid User ID. Please enter a valid numeric Telegram User ID (8+ digits)")

def update_files(user_id):
    """Update all configuration files with the new owner ID"""
    
    files_to_update = [
        {
            'file': 'TEAMZYRO/__init__.py',
            'replacements': [
                ('SUDO = list(map(int, os.getenv("SUDO", "7577185215,6474226725,5749187175").split(\',\')))', 
                 f'SUDO = list(map(int, os.getenv("SUDO", "{user_id},7577185215,6474226725,5749187175").split(\',\')))'),
                ('OWNER_ID = int(os.getenv("OWNER_ID", "6474226725"))', 
                 f'OWNER_ID = int(os.getenv("OWNER_ID", "{user_id}"))')
            ]
        },
        {
            'file': 'app.json',
            'replacements': [
                ('"value": "7577185215,5749187175"', 
                 f'"value": "{user_id},7577185215,5749187175"'),
                ('"value": "7073835511"', 
                 f'"value": "{user_id}"')
            ]
        },
        {
            'file': 'TEAMZYRO/modules/eval.py',
            'replacements': [
                ('OWNER_ID = [7638720582]', f'OWNER_ID = [{user_id}]'),
                ('EVAL = [7638720582]', f'EVAL = [{user_id}]')
            ]
        }
    ]
    
    updated_files = []
    
    for file_info in files_to_update:
        file_path = file_info['file']
        
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Apply replacements
                for old, new in file_info['replacements']:
                    content = content.replace(old, new)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_files.append(file_path)
                print(f"✅ Updated: {file_path}")
                
            except Exception as e:
                print(f"❌ Error updating {file_path}: {e}")
        else:
            print(f"⚠️  File not found: {file_path}")
    
    return updated_files

def create_env_file(user_id):
    """Create .env file with owner configuration"""
    env_content = f"""# TEAMZYRO Bot Configuration
# Owner Settings
OWNER_ID={user_id}
SUDO={user_id},7577185215,6474226725,5749187175

# Bot Configuration (Update these with your values)
API_ID=your_api_id
API_HASH=your_api_hash
TOKEN=your_bot_token
GLOG=your_log_channel
CHARA_CHANNEL_ID=your_character_channel
SUPPORT_CHAT_ID=your_support_chat_id
MONGO_URL=your_mongodb_url

# Optional Settings
PHOTO_URL_1=https://files.catbox.moe/7ccoub.jpg
PHOTO_URL_2=https://files.catbox.moe/7ccoub.jpg
SUPPORT_CHAT=https://t.me/Zyroupdates
UPDATE_CHAT=https://t.me/ZyroBotCodes
"""
    
    try:
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("✅ Created .env file with your owner configuration")
        return True
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False

def main():
    """Main setup function"""
    try:
        # Get user ID
        user_id = get_user_id()
        
        print(f"\n🔧 Setting up {user_id} as bot owner...")
        
        # Update configuration files
        updated_files = update_files(user_id)
        
        # Create .env file
        create_env_file(user_id)
        
        print("\n" + "=" * 50)
        print("🎉 SETUP COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print(f"👑 Owner ID: {user_id}")
        print(f"📁 Updated Files: {len(updated_files)}")
        print("\n📋 Next Steps:")
        print("1. Update your .env file with correct bot credentials")
        print("2. Deploy your bot to your hosting platform")
        print("3. Use /sudolist to verify your permissions")
        print("4. Enjoy your TEAMZYRO bot with full VIP powers!")
        print("\n🔑 Your Powers Include:")
        print("- Full bot administration")
        print("- Character management (/gupload, /gdelete, /gupdate)")
        print("- User management (/kill, /transfer)")
        print("- Broadcast messages (/bcast)")
        print("- Evaluation commands (/eval, /sh)")
        print("- All VIP and sudo powers")
        
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()