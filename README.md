ps-stats is a simple app for script to receive statistics

default usage run next command from directory, where file is placed:

    python pr-stats.py < user_name >

'user_name' - github's user name
'token' - github's token

App has required option:

    1. < user_name >

    App has additional options:
    
    1. "python pr-stats.py <user_name> (-h |--help)"
    2. "python pr-stats.py <user_name> --version"  get info about current version
    3. "python pr-stats.py <user_name> --prnum"    from which pr collect info
    4. "python pr-stats.py <user_name> --token"    use next token for login
    5. "python pr-stats.py <user_name> --days"     how long (days) opened pr
    6. "python pr-stats.py <user_name> --day"      Day of the week opened
    7. "python pr-stats.py <user_name> --hd"       Hour of the day opened
    8. "python pr-stats.py <user_name> --who"      User who opened