# Guns.lol Informations Fetcher

## Description

This Python script fetches various information about a user from the guns.lol website. It can retrieve their links, profile information, premium features, sources (background image, audio, avatar), what they're doing, and more.

[My guns.lol profile](https://guns.lol/M58)


## Usage
```Bash
python3 main.py -u <username> [options]
```

## Options
    -f, --free: Check if the username/alias is available.
    -l, --links: Get all the links of the user.
    -a, --all: Return the whole JSON response.
    -i, --info: Get the basic informations of the user.
    -p, --premium: Get the premium informations of the user.
    -s, --sources: Get the sources of the user (background image, audio, avatar).
    -w, --what: Get what the user is currently doing.

## Examples

**Check if an username / alias is available**
```bash
$ python3 main.py -u m58 -f
Guns.lol Informations Fetcher
This tool is used to fetch the informations of a user from guns.lol
   [!] 'm58' is not available
   
$ python3 main.py -u * -f
Guns.lol Informations Fetcher
This tool is used to fetch the informations of a user from guns.lol
     [~] The alias '*' belongs to /cutie
```


**Get all the links of an user:**
```bash
$ python3 main.py -u m58 -l
Guns.lol Informations Fetcher
This tool is used to fetch the informations of a user from guns.lol
[>] Links of m58
   [>] Telegram: https://t.me/NahCringe
   [>] Youtube: https://youtube.com/izzamuzzic
   [>] Instagram: https://instagram.com/madelyncline
   [>] Custom_url: https://root-me.org/M58_
```

**Get informations of an user :**
```bash
python3 main.py -u m58 -i
Guns.lol Informations Fetcher
This tool is used to fetch the informations of a user from guns.lol
[>] Informations of m58
   [>] Username: M58
   [>] Alias: /buy
   [>] Description: Last Year InfoSec Student
   [>] Date of creation : 15-01-2024 17:30:59
   [>] Badges:
        - premium
        - server_booster
        - imagehost_access
   [>] Profil's visits: 102
   [>] UUID: 13355
   [>] Discord ID: 323863341585924107
```

**Get premium informations of an user :**
```bash
python3 main.py -u m58 -p
Guns.lol Informations Fetcher
This tool is used to fetch the informations of a user from guns.lol
[>] Premium informations of m58
   [>] Animated description: True
   [>] Cursor effects : particles
   [>] Custom cursor: https://r2.guns.lol/3bdd1448-713a-4535-9744-119977d561b0.cur
   [>] Font used: drippy
   [>] Custom entrance text: 'Why stalk ?'
```

**Get sources of an user :**
```bash
python3 main.py -u m58 -s
Guns.lol Informations Fetcher
This tool is used to fetch the informations of a user from guns.lol
[>] Sources of m58
   [>] Background image: https://r2.guns.lol/d2b79686-9e3d-4954-8f18-f2945691a767.gif
   [>] Audio: https://r2.guns.lol/f1659bd1-e40e-4b65-acb2-769ecdbef5fa.mp3
   [>] Avatar: https://r2.guns.lol/44c09d4d-df62-418e-be3d-9453b6e9df39.jpg
   [>] Custom cursor: https://r2.guns.lol/3bdd1448-713a-4535-9744-119977d561b0.cur
   [>] Discord link: https://discord.gg/NBCQZBFV7R
   [>] Discord profil picture: https://cdn.discordapp.com/avatars/323863341585924107/8cd0d24b917abb63b4dbc59e4398d522.png?size=1024
```

**Get what the user is currently doing :**
```bash
python3 main.py -u m58 -w
Guns.lol Informations Fetcher
This tool is used to fetch the informations of a user from guns.lol
[>] What m58 is doing
   [>] Presence: currently doing nothing
   [>] Details: In guns-main - 0 problems found
   [>] State: Working on main.py:19:1
   [>] Action: Editing a PYTHON file
   [>] Software: Visual Studio Code
```




## Disclaimer

This script is not affiliated with or endorsed by guns.lol.
Use this script responsibly and ethically. Respect the privacy of other users.
The script's functionality may be affected by changes to the guns.lol website.

## Contributions

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License.
