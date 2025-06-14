# Genshin Impact Daily Login Script

A Python script that automates the daily login check-in process for Genshin Impact using the genshin.py library.

## Features

- Automatic daily check-in
- Command-line interface
- Detailed logging
- Cron job/scheduled task compatible
- Error handling

## Prerequisites

1. Python 3.x
2. Required Python package:
   ```bash
   pip install genshin
   ```

## Usage

Run the script from the command line:

```bash
python genshin_daily_login.py <username> <password>
```

Replace `<username>` and `<password>` with your HoYoLAB account credentials.

## Setting up a Cron Job (Linux/Mac)

1. Open your crontab file:
   ```bash
   crontab -e
   ```

2. Add a line to run the script daily (for example, at 8 AM):
   ```bash
   0 8 * * * cd /path/to/script && /usr/bin/python3 genshin_daily_login.py <username> <password>
   ```

## Setting up a Scheduled Task (Windows)

1. Open Task Scheduler
2. Create a new Basic Task
3. Set the trigger to run daily
4. Set the action to start a program:
   - Program/script: `python`
   - Arguments: `genshin_daily_login.py <username> <password>`
   - Start in: `C:\path\to\script`

## Logging

The script creates a log file `genshin_login.log` in the same directory, which contains detailed information about the login process and any errors that might occur.

## Security Note

It's recommended to store your credentials in environment variables or a configuration file rather than directly in the cron job or scheduled task. You can modify the script to read credentials from a config file if needed.

For example, you could create a `config.json` file:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Then modify the script to read from this file instead of using command-line arguments.

## Error Handling

The script handles various scenarios:
- Invalid credentials
- Already claimed daily reward
- Network issues
- API errors

All errors are logged to `genshin_login.log` for troubleshooting.