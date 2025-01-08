# Twitter Automation Bot

This Python-based Twitter automation bot allows you to schedule daily tweets and automatically update your Twitter bio. The bot uses Safari WebDriver for web automation.

## Features

- Automated daily tweets at specified times (default: 2:20 PM)
- Automatic bio updates at midnight
- Safari WebDriver integration
- Error handling and logging
- Modular code structure

## Prerequisites

- Python 3.7+
- Safari browser
- macOS
- Twitter/X account

## Project Structure
```
twitter_bot/
│
├── main.py
├── modules/
│   ├── __init__.py
│   ├── driver_manager.py
│   ├── login_handler.py
│   ├── tweet_manager.py
│   └── profile_manager.py
├── config.py
└── requirements.txt
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/twitter_bot.git
cd twitter_bot
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Configure Safari for automation
- Open Safari
- Go to Safari > Preferences > Advanced
- Check "Show Develop menu in menu bar"
- Go to Develop > Allow Remote Automation

## Configuration

1. Open `config.py`
2. Replace placeholder credentials with your Twitter/X login details:
```python
USERNAME = "your_username"
PASSWORD = "your_password"
```

## Usage

Run the bot:
```bash
python main.py
```

The bot will:
- Login to your Twitter account
- Schedule tweets for required time daily
- Update your bio at midnight
- Keep running until interrupted (Ctrl+C)

## Module Descriptions

- `driver_manager.py`: Handles Safari WebDriver setup and configuration
- `login_handler.py`: Manages Twitter authentication
- `tweet_manager.py`: Handles tweet creation and posting
- `profile_manager.py`: Manages profile bio updates
- `config.py`: Stores configuration settings
- `main.py`: Main script orchestrating the automation

## Important Notes

- This automation uses web scraping and is not an official Twitter API implementation
- Use responsibly and be aware of Twitter's terms of service
- Keep your credentials secure and never commit them to version control
- The bot requires your computer to be running to execute scheduled tasks

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Disclaimer

This bot is for educational purposes only. Use at your own risk. The authors are not responsible for any account suspensions or other issues that may arise from using this automation tool.
