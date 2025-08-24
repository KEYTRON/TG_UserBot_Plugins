# Userbot Plugins = 10 Packs
A collection of useful & funny Telegram UserBot Plugins.

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Telegram API credentials (API_ID, API_HASH)
- UserBot framework (like @FridayOT or @UniBorg)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YourUsername/tg-userbot-plugins.git
   cd tg-userbot-plugins
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**
   - Copy `.env.example` to `.env`
   - Edit `.env` with your credentials
   - Update `config.py` with your information

4. **Customize plugins**
   - Edit personal information in plugins
   - Replace placeholders with your data

## 📋 Plugins List

### 🔧 **hacking.py** - Fake Hacking Environment
- **Command:** `.hacking`
- **Description:** Shows fake hacking terminal animation
- **Status:** ✅ Ready to use

### 👤 **iamyo.py** - Personal Info Animation
- **Command:** `.iamyo`
- **Description:** Animated personal information display
- **Status:** ⚠️ **Edit before installing** - Replace personal info

### 🇮🇳 **indianflag.py** - Indian Flag Emoji
- **Command:** `.inflag`
- **Description:** Shows emoji-coded Indian flag
- **Status:** ✅ Ready to use

### 🗺️ **indianmap.py** - Indian Map ASCII
- **Command:** `.inmap`
- **Description:** Shows dot-coded Indian map
- **Status:** ✅ Ready to use

### 🎭 **ophack.py** - Fake Hacking Animation
- **Command:** `.ophack`
- **Description:** Fake hacking animation (reply to user)
- **Status:** ⚠️ **Edit before installing** - Replace personal info

### 📚 **repos.py** - GitHub Repositories
- **Command:** `.repos`
- **Description:** Shows your GitHub repositories
- **Status:** ⚠️ **Edit before installing** - Replace repository links

### 😴 **sleep.py** - Sleep/AFK Status
- **Command:** `.sleep`
- **Description:** Set sleep/AFK status
- **Status:** ✅ Ready to use

### 🚫 **pmpermit.py** - PM Security
- **Commands:** `.a`, `.block`, `.da`, `.listapproved`
- **Description:** Advanced PM permission system
- **Status:** ⚠️ **Edit before installing** - Configure group IDs

### 🆔 **whoami.py** - Personal Information
- **Command:** `.whoami`
- **Description:** Detailed personal information display
- **Status:** ⚠️ **Edit before installing** - Replace personal info

### 🔌 **offline.py** - Offline Status
- **Command:** `.offline`
- **Description:** Set offline/AFK status
- **Status:** ✅ Ready to use

## ⚙️ Configuration

### Environment Variables
Create a `.env` file with:
```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
ALIVE_NAME=Your Name
PRIVATE_GROUP_ID=your_group_id
PLUGIN_CHANNEL=your_channel_id
```

### Personal Information
Edit these files to replace personal information:
- `iamyo.py` - Your name and username
- `repos.py` - Your GitHub repositories
- `whoami.py` - Your personal details
- `ophack.py` - Your Telegram ID
- `config.py` - All personal settings

## 🛠️ Customization Guide

### 1. Replace Personal Information
```python
# In iamyo.py, whoami.py, repos.py
YOUR_NAME = "Your Actual Name"
YOUR_USERNAME = "YourActualUsername"
YOUR_GITHUB = "YourGitHubUsername"
```

### 2. Configure Group IDs
```python
# In pmpermit.py and config.py
PRIVATE_GROUP_ID = 123456789  # Your private group ID
PLUGIN_CHANNEL = 987654321    # Your plugin channel ID
```

### 3. Update API Credentials
```python
# In .env file
API_ID=12345678
API_HASH=abcdef1234567890abcdef1234567890
```

## 📁 Project Structure
```
tg-userbot-plugins/
├── plugins/                 # Plugin files
│   ├── hacking.py
│   ├── iamyo.py
│   ├── indianflag.py
│   ├── indianmap.py
│   ├── ophack.py
│   ├── pmpermit.py
│   ├── repos.py
│   ├── sleep.py
│   ├── whoami.py
│   └── offline.py
├── config.py               # Configuration file
├── requirements.txt        # Python dependencies
├── setup.py               # Installation script
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore file
├── LICENSE               # MIT License
└── README.md             # This file
```

## 🔧 Troubleshooting

### Common Issues
1. **Import errors**: Make sure all dependencies are installed
2. **Permission errors**: Check your Telegram API credentials
3. **Plugin not working**: Verify command syntax and permissions

### Debug Mode
Enable debug logging in your UserBot configuration to see detailed error messages.

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Original plugins by @AbirHasan2005
- UserBot community for support
- Contributors and maintainers

## 📞 Support

- **Telegram Group**: [Join our group](http://t.me/YourGroup)
- **Issues**: [GitHub Issues](https://github.com/YourUsername/tg-userbot-plugins/issues)
- **Documentation**: [Wiki](https://github.com/YourUsername/tg-userbot-plugins/wiki)

---

**⚠️ Important**: Remember to edit personal information in plugins before installing!
