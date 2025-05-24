# API Key Management System

The Ebook Generator now includes a comprehensive API Key Management system that allows you to manage multiple Gemini AI API keys with automatic rotation and backup functionality.

## Features

### 🔑 **Multiple API Key Support**
- Manage unlimited API keys with automatic numbering
- Main key (`GEMINI_API_KEY`) with numbered backups (`GEMINI_API_KEY_1`, `GEMINI_API_KEY_2`, etc.)
- Automatic rotation when adding new keys

### 🔄 **Smart Key Rotation**
- When adding a new API key, the current main key automatically becomes a backup
- Maintains chronological order of API keys
- Prevents loss of existing keys

### 🛡️ **Security Features**
- API keys are masked in displays for security
- Basic validation of API key format
- Safe file handling with error recovery

### 📊 **Management Tools**
- View all API keys with status information
- Remove backup keys (main key protected)
- Promote backup keys to main
- Test API key functionality
- Real-time key count and status

## How to Access

### From Main Menu
1. Run `python run.py`
2. Select **"API Key Management"** from the main menu
3. Use the interactive menu to manage your keys

### Direct Access
```python
from src.utils.api_key_manager import show_api_key_management_menu
show_api_key_management_menu()
```

## Menu Options

### 1. Add New API Key
- **Function**: Adds a new API key and rotates the current main key to backup
- **Process**:
  1. Shows current main key (masked)
  2. Prompts for new API key
  3. Validates the key format
  4. Moves current main key to `GEMINI_API_KEY_X` (next available number)
  5. Sets new key as main `GEMINI_API_KEY`
- **Example**:
  ```
  Current main key: AIzaSyCg********uYys
  Enter new API key: AIzaSyCV********LxS8
  
  This will:
  • Set the new key as the main GEMINI_API_KEY
  • Move current main key to GEMINI_API_KEY_10
  ```

### 2. View All API Keys
- **Function**: Displays detailed information about all API keys
- **Shows**:
  - Key name and status (Main/Backup)
  - First 20 characters of each key
  - Key length
  - Total count statistics

### 3. Remove Backup API Key
- **Function**: Safely removes backup API keys
- **Protection**: Cannot remove the main API key
- **Process**:
  1. Lists all backup keys
  2. Allows selection by number
  3. Confirms deletion
  4. Updates .env file

### 4. Promote Backup Key to Main
- **Function**: Makes a backup key the new main API key
- **Process**:
  1. Lists available backup keys
  2. Allows selection by number
  3. Removes the backup key entry
  4. Sets it as the new main key

### 5. Test Current Main API Key
- **Function**: Tests the current main API key functionality
- **Process**:
  1. Shows masked main key
  2. Initializes Gemini client
  3. Sends test message
  4. Reports success/failure with response preview

## File Structure

### .env File Format
```env
# Gemini AI API Keys
# Main API key
GEMINI_API_KEY=AIzaSyCg********uYys

# Backup API keys
GEMINI_API_KEY_1=AIzaSyCV********LxS8
GEMINI_API_KEY_2=AIzaSyA4********N9Ro
GEMINI_API_KEY_3=AIzaSyA2********rM4s
```

### Automatic File Management
- Creates `.env` file if it doesn't exist
- Maintains proper formatting and comments
- Handles file read/write errors gracefully
- Preserves existing structure

## API Reference

### APIKeyManager Class

```python
from src.utils.api_key_manager import APIKeyManager

# Initialize
api_manager = APIKeyManager()

# Get all API keys
keys = api_manager.get_all_api_keys()

# Add new API key (rotates current main)
success = api_manager.add_new_api_key("new_api_key_here")

# Remove backup key
success = api_manager.remove_api_key("GEMINI_API_KEY_5")

# Promote backup to main
success = api_manager.set_main_api_key("GEMINI_API_KEY_3")

# Get key counts
total, backup = api_manager.get_api_key_count()

# Display keys table
api_manager.display_api_keys()
```

## Best Practices

### 🔐 **Security**
- Never share your API keys
- Use different keys for different projects if needed
- Regularly rotate your API keys
- Keep backup keys for redundancy

### 📈 **Management**
- Add multiple keys to handle rate limits
- Test keys before important generation sessions
- Remove unused or expired keys
- Monitor key usage in Google AI Studio

### 🔄 **Rotation Strategy**
- Add new keys when approaching rate limits
- Keep 3-5 backup keys for reliability
- Promote tested backup keys when main key fails
- Remove old or problematic keys regularly

## Integration with Ebook Generator

The API Key Management system is fully integrated with the Ebook Generator:

- **Automatic Detection**: The system automatically detects and uses all available API keys
- **Rate Limit Handling**: When one key hits rate limits, the system automatically switches to backup keys
- **Seamless Operation**: No interruption to book generation when keys are rotated
- **Status Monitoring**: Real-time monitoring of key usage and availability

## Troubleshooting

### Common Issues

**"Invalid API key format"**
- Ensure the API key is copied correctly
- Check for extra spaces or characters
- Verify the key is from Google AI Studio

**"API key test failed"**
- Check internet connection
- Verify the key is active in Google AI Studio
- Ensure the key has proper permissions

**"No main API key found"**
- Add at least one API key using option 1
- Check that .env file exists and is readable

### Error Recovery
- The system automatically creates .env file if missing
- Failed operations don't affect existing keys
- All changes are confirmed before execution
- Backup keys are preserved during rotation

## Support

For issues with the API Key Management system:
1. Check the troubleshooting section above
2. Verify your .env file format
3. Test individual API keys in Google AI Studio
4. Check file permissions for .env file

The API Key Management system ensures reliable, secure, and efficient management of your Gemini AI API keys for uninterrupted ebook generation!
