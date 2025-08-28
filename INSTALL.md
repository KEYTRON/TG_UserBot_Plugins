# Installation Guide

## Prerequisites

Before installing the UserBot plugins, make sure you have:

1. **Python 3.7+** installed on your system
2. **Telegram API credentials** (API_ID and API_HASH)
3. **UserBot framework** (like @FridayOT, @UniBorg, or similar)

## Step-by-Step Installation

### 1. Get Telegram API Credentials

1. Go to [my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Go to "API Development Tools"
4. Create a new application
5. Note down your `API_ID` and `API_HASH`

### 2. Clone the Repository

```bash
git clone https://github.com/YourUsername/tg-userbot-plugins.git
cd tg-userbot-plugins
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Bot

#### Option A: Using Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your credentials:
   ```env
   API_ID=12345678
   API_HASH=abcdef1234567890abcdef1234567890
   BOT_TOKEN=your_bot_token_here
   ALIVE_NAME=Your Name
   PRIVATE_GROUP_ID=your_group_id
   PLUGIN_CHANNEL=your_channel_id
   ```

#### Option B: Using config.py

Edit `config.py` directly with your information:
```python
YOUR_ID = 123456789  # Your Telegram ID
YOUR_USERNAME = "YourUsername"
YOUR_NAME = "Your Name"
YOUR_GROUP = "YourGroup"
YOUR_GITHUB = "YourGitHubUsername"
```

### 5. Customize Plugins

**⚠️ IMPORTANT: You MUST edit these files before using!**

#### iamyo.py
```python
# Replace these lines:
"Your",
"Name",
"Your Name\n\n❤ @YourUsername ❤"
```

#### repos.py
```python
# Replace repository links:
pm_caption = "`Repositories of` **@YourUsername**\n"
pm_caption += "**GitHub:** `https://github.com/YourUsername`\n\n"
pm_caption += "**Project1:** `https://github.com/YourUsername/Project1`\n"
# ... add your actual repositories
```

#### whoami.py
```python
# Replace personal information:
"I am [Your Name](http://t.me/YourUsername). \n**Skills:** \n**[1] Bash/Shell** \n**[2] Python** \n**[3] HTML** \n**[4] PHP** \n**[5] Git** \n \n`I use Ubuntu, Kali, Android and Windows OS.`\n\n**Telegram Group: **[Your Group](http://t.me/YourGroup) \n **Learn Coding, Programming & Hacking. Feedback for my GitHub Repositories. Report Bugs and More there. Also get Updates in group.**\n\n**Follow on: **\n[GitHub Profile](https://github.com/YourUsername) \n[Twitter Profile](https://twitter.com/YourUsername) \n[Facebook Profile](https://facebook.com/YourUsername) \n[Instagram Profile](https://instagram.com/YourUsername)\n"
```

#### ophack.py
```python
# Replace your Telegram ID:
if idd==YOUR_ID:  # Replace YOUR_ID with your actual Telegram ID
```

#### pmpermit.py
```python
# Configure group IDs in config.py or .env:
PRIVATE_GROUP_ID = 123456789  # Your private group ID
PLUGIN_CHANNEL = 987654321    # Your plugin channel ID
```

### 6. Get Your Telegram ID

To find your Telegram ID:

1. Send a message to [@userinfobot](https://t.me/userinfobot)
2. It will reply with your user ID
3. Use this ID in the configuration files

### 7. Get Group/Channel IDs

To find group or channel IDs:

1. Add [@getidsbot](https://t.me/getidsbot) to your group/channel
2. It will show the chat ID
3. Use this ID in the configuration files

### 8. Install in UserBot

#### For @FridayOT:
1. Copy plugin files to your UserBot's plugins directory
2. Restart the UserBot
3. Test commands

#### For @UniBorg:
1. Copy plugin files to your UserBot's plugins directory
2. Restart the UserBot
3. Test commands

## Testing the Installation

After installation, test these commands:

- `.hacking` - Should show fake hacking animation
- `.iamyo` - Should show your personal info animation
- `.inflag` - Should show Indian flag
- `.inmap` - Should show Indian map
- `.sleep` - Should set sleep status
- `.offline` - Should set offline status

## Troubleshooting

### Common Issues

1. **"Module not found" errors**
   - Make sure all dependencies are installed
   - Check Python version (3.7+ required)

2. **"API_ID/API_HASH invalid"**
   - Verify your Telegram API credentials
   - Make sure you're using the correct values

3. **"Permission denied" errors**
   - Check if you have admin rights in the group
   - Verify group ID configuration

4. **Plugins not responding**
   - Check if UserBot is running
   - Verify plugin files are in the correct directory
   - Check UserBot logs for errors

### Debug Mode

Enable debug logging in your UserBot to see detailed error messages.

## Support

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/YourUsername/tg-userbot-plugins/issues)
2. Join our [Telegram Group](http://t.me/YourGroup)
3. Check the [Wiki](https://github.com/YourUsername/tg-userbot-plugins/wiki)

## Security Notes

- Never share your API credentials
- Keep your `.env` file private
- Don't commit sensitive information to Git
- Use environment variables for production

---

**Remember**: Always edit personal information in plugins before installing!