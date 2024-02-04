# Author: M58
# Version: 1.0
# Description: This tool is used to fetch the informations of a user from guns.lol
# Usage: python3 main.py -u <username> -f -l -a -i -p -s -w -e

#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import argparse
from art import *
from colorama import Fore, Style
import os
from datetime import datetime

url = "https://guns.lol/_next/data/Nb1vbrVK2F1PILuaPYlB8/"
extention = ".json"

# os.system("cls" if os.name == "nt" else "clear")

print("Guns.lol Informations Fetcher")
print("This tool is used to fetch the informations of a user from guns.lol")

def get_all_links(username):
    """Get all the links of the user

    Args:
        username (str): The username / alias of the user
    """
    print(Fore.GREEN + f"[>] Links of {username}" + Style.RESET_ALL)
    response = requests.get(url + username + extention)
    try : 
        for key, value in response.json()["pageProps"]["data"]["config"]["socials"].items():
            print(Fore.YELLOW + f"   [>] {key.capitalize()}: {value}" + Style.RESET_ALL)
    except KeyError:
        print(Fore.RED + "   [!] Something went wrong, are you sure the username / alias is correct (use -f to check)" + Style.RESET_ALL)

def get_user_premium_info(username):
    """Get the premium informations of the user

    Args:
        username (str): The username / alias of the user
    """
    response = requests.get(url + username + extention)
    try:
        print(Fore.GREEN + f"[>] Premium informations of {username}" + Style.RESET_ALL)
        # {'pageProps': {'data': {'username': 'M58', 'account_created': 1705339859, 'verified': True, 'alias': '/buy', 'config': {'socials': {'telegram': 'https://t.me/NahCringe', 'youtube': 'https://youtube.com/izzamuzzic', 'instagram': 'https://instagram.com/madelyncline', 'custom_url': 'https://root-me.org/M58_'}, 'description': 'Last Year InfoSec Student', 'url': 'https://r2.guns.lol/d2b79686-9e3d-4954-8f18-f2945691a767.gif', 'audio': 'https://r2.guns.lol/f1659bd1-e40e-4b65-acb2-769ecdbef5fa.mp3', 'avatar': 'https://r2.guns.lol/44c09d4d-df62-418e-be3d-9453b6e9df39.jpg', 'color': '#ffffff', 'text_color': '#ffffff', 'bg_color': '#080808', 'gradient_1': '#881c9c', 'gradient_2': '#0d0d0d', 'presence': 'enabled', 'monochrome': False, 'animated_title': True, 'custom_cursor': 'https://r2.guns.lol/3bdd1448-713a-4535-9744-119977d561b0.cur', 'page_views': '101', 'user_badges': ['premium', 'server_booster', 'imagehost_access'], 'custom_badges': [], 'display_name': 'M58', 'transparent_bg': 0, 'profile_gradient': True, 'background_effects': 'tv', 'volume_control': False, 'premium': {'animated_description': True,{'pageProps': {'data': {'username': 'M58', 'account_created': 1705339859, 'verified': True, 'alias': '/buy', 'config': {'socials': {'telegram': 'https://t.me/NahCringe', 'youtube': 'https://youtube.com/izzamuzzic', 'instagram': 'https://instagram.com/madelyncline', 'custom_url': 'https://root-me.org/M58_'}, 'description': 'Last Year InfoSec Student', 'url': 'https://r2.guns.lol/d2b79686-9e3d-4954-8f18-f2945691a767.gif', 'audio': 'https://r2.guns.lol/f1659bd1-e40e-4b65-acb2-769ecdbef5fa.mp3', 'avatar': 'https://r2.guns.lol/44c09d4d-df62-418e-be3d-9453b6e9df39.jpg', 'color': '#ffffff', 'text_color': '#ffffff', 'bg_color': '#080808', 'gradient_1': '#881c9c', 'gradient_2': '#0d0d0d', 'presence': 'enabled', 'monochrome': False, 'animated_title': True, 'custom_cursor': 'https://r2.guns.lol/3bdd1448-713a-4535-9744-119977d561b0.cur', 'page_views': '101', 'user_badges': ['premium', 'server_booster', 'imagehost_access'], 'custom_badges': [], 'display_name': 'M58', 'transparent_bg': 0, 'profile_gradient': True, 'background_effects': 'tv', 'volume_control': False, 'premium': {'animated_description': True,
        # if premium is not enabled, the key is not present
        if response.json()["pageProps"]["data"]["config"]["premium"]:
            print(Fore.YELLOW + f"   [>] Animated description: {response.json()['pageProps']['data']['config']['premium']['animated_description']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] Cursor effects : {response.json()['pageProps']['data']['config']['premium']['cursor_effects']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] Custom cursor: {response.json()['pageProps']['data']['config']['custom_cursor']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] Font used: {response.json()['pageProps']['data']['config']['premium']['font']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] Custom entrance text: '{response.json()['pageProps']['data']['config']['premium']['page_enter_text']}'" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"   [>] The user doesn't have premium" + Style.RESET_ALL)

    except KeyError:
        print(Fore.RED + "   [!] Something went wrong, are you sure the username / alias is correct (use -f to check)" + Style.RESET_ALL)

def get_sources(username):
    """Get the sources of the user

    Args:
        username (str): The username / alias of the user
    """
    response = requests.get(url + username + extention)
    try:
        print(Fore.GREEN + f"[>] Sources of {username}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"   [>] Background image: {response.json()['pageProps']['data']['config']['url']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"   [>] Audio: {response.json()['pageProps']['data']['config']['audio']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"   [>] Avatar: {response.json()['pageProps']['data']['config']['avatar']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"   [>] Custom cursor: {response.json()['pageProps']['data']['config']['custom_cursor']}" + Style.RESET_ALL)
        if response.json()['pageProps']['data']['config']['premium']:
            print(Fore.YELLOW + f"   [>] Discord link: {response.json()['pageProps']['data']['config']['premium']['second_tab']['discord']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"   [>] Discord profil picture: {response.json()['pageProps']['spotify']['avatar']}" + Style.RESET_ALL)
    except KeyError:
        print(Fore.RED + "   [!] Something went wrong, are you sure the username / alias is correct (use -f to check)" + Style.RESET_ALL)

def free_username_alias(username):
    """Check if the username / alias is available

    Args:
        username (str): The username / alias of the user
    """
    response = requests.get(url + username + extention)
    try :
        if response.json()["pageProps"]["data"]["error"] == "User not found":
            print(Fore.GREEN + f"   [>] The username / alias '{username}' is available" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"     [!] The username / alias '{username}' is not available" + Style.RESET_ALL)
    except KeyError:
        try : 
            if response.json()["pageProps"]["__N_REDIRECT"]:
                print(Fore.YELLOW + f"     [~] The alias '{username}' belongs to " + response.json()['pageProps']['__N_REDIRECT'] + Style.RESET_ALL)
        except KeyError:
            print(Fore.RED + f"   [!] '{username}' is not available" + Style.RESET_ALL)


def get_what_user_is_doing(username):
    """Get what the user is doing

    Args:
        username (str): The username / alias of the user
    """
    response = requests.get(url + username + extention)
    try : 
        if response.json()["pageProps"]["data"]["error"] == "User not found":
            print(Fore.RED + f"   [!] The username / alias '{username}' does not exist" + Style.RESET_ALL)
    except KeyError:
        pass
    try:
        spotify_presence = response.json()['pageProps']['spotify'].get('presence')
        if spotify_presence:
            print(Fore.GREEN + f"[>] What {username} is doing" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] Presence: {spotify_presence['name']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] Details: {spotify_presence['details']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] State: {spotify_presence['state']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] Action: {spotify_presence['assets']['large_text']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] Software: {spotify_presence['assets']['small_text']}" + Style.RESET_ALL)
    except KeyError:
        try:
            print(Fore.RED + f"[>] What {username} is doing" + Style.RESET_ALL)
            spotify_data = response.json()['pageProps']['spotify']['spotify']  
            print(Fore.YELLOW + f"   [>] Artist: {spotify_data['artist']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"   [>] Title: {spotify_data['title']}" + Style.RESET_ALL)
        except KeyError:
            print(Fore.RED + "   [!] Something went wrong, are you sure the username / alias is correct (use -f to check)" + Style.RESET_ALL)

def get_user_info(username):
    """Get the informations of the user

    Args:
        username (str): The username / alias of the user
    """
    response = requests.get(url + username + extention)
    try:
        print(Fore.GREEN + f"[>] Informations of {username}" + Style.RESET_ALL)
        # USERNAME AND ALIAS
        print(Fore.YELLOW + f"   [>] Username: {response.json()['pageProps']['data']['username']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"   [>] Alias: {response.json()['pageProps']['data']['alias']}" + Style.RESET_ALL)
        # DESCRIPTION
        print(Fore.YELLOW + f"   [>] Description: {response.json()['pageProps']['data']['config']['description']}" + Style.RESET_ALL)
        # DATE OF CREATION
        created_at = response.json()['pageProps']['data']['account_created']
        created_at_date = datetime.utcfromtimestamp(created_at).strftime('%d-%m-%Y %H:%M:%S')
        print(Fore.YELLOW + f"   [>] Date of creation : {created_at_date}" + Style.RESET_ALL)
        # BADGES
        badges = '\n'.join([f'\t- {badge}' for badge in response.json()['pageProps']['data']['config']['user_badges']])
        print(Fore.YELLOW + f"   [>] Badges: \n{badges}" + Style.RESET_ALL)
        # CUSTOM BADGES ? 
        custom_badges = '\n'.join([f'\t- {badge}' for badge in response.json()['pageProps']['data']['config']['custom_badges']])
        # PROFIL's VISITS
        print(Fore.YELLOW + f"   [>] Profil's visits: {response.json()['pageProps']['data']['config']['page_views']}" + Style.RESET_ALL)
        # UUID
        print(Fore.YELLOW + f"   [>] UUID: {response.json()['pageProps']['data']['uid']}" + Style.RESET_ALL)
        # Discord ID 
        print(Fore.YELLOW + f"   [>] Discord ID: {response.json()['pageProps']['data']['discord_id']}" + Style.RESET_ALL)
    except KeyError:
        print(Fore.RED + "   [!] Something went wrong, are you sure the username / alias is correct (use -f to check)" + Style.RESET_ALL)

def main():
    """Main function of the tool to fetch the informations of a user from guns.lol
    """
    parser = argparse.ArgumentParser(description="Fetch the informations of a user from guns.lol")
    parser.add_argument("-f", "--free", help="See if the username / alias is available", action="store_true")
    parser.add_argument("-l", "--links", help="Get all the links of the user", action="store_true")
    parser.add_argument("-u", "--username", help="The username / alias of the user")
    parser.add_argument("-a", "--all", help="Return the whole json", action="store_true")
    parser.add_argument("-i", "--info", help="Get the informations of the user", action="store_true")
    parser.add_argument("-p", "--premium", help="Get the premium informations of the user", action="store_true")
    parser.add_argument("-s", "--sources", help="Get the sources of the user", action="store_true")
    parser.add_argument("-w", "--what", help="What the user is doing", action="store_true")
    parser.add_argument("-e", "--everything", help="Get everything", action="store_true")
    args = parser.parse_args()

    if args.username:
        username = args.username
        if args.free:
            free_username_alias(username)
        elif args.links:
            get_all_links(username)
        elif args.all:
            response = requests.get(url + username + extention)
            print(response.json())
        elif args.info:
            get_user_info(username)
        elif args.premium:
            get_user_premium_info(username)
        elif args.sources:
            get_sources(username)
        elif args.what:
            get_what_user_is_doing(username)
        elif args.everything:
            get_user_info(username)
            get_user_premium_info(username)
            get_sources(username)
            get_what_user_is_doing(username)
            get_all_links(username)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
