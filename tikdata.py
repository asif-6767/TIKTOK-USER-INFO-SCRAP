#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import requests
import re
import argparse
import urllib.parse
from bs4 import BeautifulSoup

# Color codes for Terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(text="Processing", duration=2):
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{Colors.CYAN}{frames[i % len(frames)]} {text}... ')
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write('\r' + ' ' * 60 + '\r')
    sys.stdout.flush()

def hacker_animation(duration=2):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*"
    for _ in range(12):
        line = ''.join(random.choice(chars) for _ in range(60))
        sys.stdout.write(f'\r{Colors.GREEN}{line}')
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write('\r' + ' ' * 70 + '\r')
    sys.stdout.flush()

def print_banner():
    clear_screen()
    banner = f"""
{Colors.RED}╔══════════════════════════════════════════════════════════════╗
{Colors.RED}║{Colors.YELLOW}  ████████╗██╗██╗  ████████╗ ██████╗ ██╗  ██╗{Colors.RED}          ║
{Colors.RED}║{Colors.YELLOW}  ╚══██╔══╝██║██║  ╚══██╔══╝██╔═══██╗██║ ██╔╝{Colors.RED}          ║
{Colors.RED}║{Colors.YELLOW}     ██║   ██║██║     ██║   ██║   ██║█████╔╝ {Colors.RED}          ║
{Colors.RED}║{Colors.YELLOW}     ██║   ██║██║     ██║   ██║   ██║██╔═██╗ {Colors.RED}          ║
{Colors.RED}║{Colors.YELLOW}     ██║   ██║██║     ██║   ╚██████╔╝██║  ██╗{Colors.RED}          ║
{Colors.RED}║{Colors.YELLOW}     ╚═╝   ╚═╝╚═╝     ╚═╝    ╚═════╝ ╚═╝  ╚═╝{Colors.RED}          ║
{Colors.RED}╠══════════════════════════════════════════════════════════════╣
{Colors.RED}║{Colors.CYAN}        TikTok Public Data Scraper v2.0{Colors.RED}                         ║
{Colors.RED}║{Colors.MAGENTA}        Developed by ᴀꜱɪꜰ ɪꜱʟᴀᴍ{Colors.RED}                              ║
{Colors.RED}╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

def print_menu():
    menu = f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗
{Colors.CYAN}║{Colors.WHITE}  [1] {Colors.GREEN}Username to Information {Colors.YELLOW}👽{Colors.CYAN}                   ║
{Colors.CYAN}║{Colors.WHITE}  [2] {Colors.GREEN}Bulk Username Scraper {Colors.YELLOW}🚀{Colors.CYAN}                    ║
{Colors.CYAN}║{Colors.WHITE}  [3] {Colors.RED}Exit {Colors.YELLOW}👋{Colors.CYAN}                                     ║
{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(menu)

# ========== YOUR ORIGINAL get_user_info FUNCTION (100% WORKING) ==========
def get_user_info(identifier, by_id=False):
    if by_id:
        url = f"https://www.tiktok.com/@{identifier}"
    else:
        if identifier.startswith('@'):
            identifier = identifier[1:]
        url = f"https://www.tiktok.com/@{identifier}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_content = response.text
        
        try:
            soup = BeautifulSoup(html_content, 'lxml')
        except:
            soup = BeautifulSoup(html_content, 'html.parser')
        
        patterns = {
            'user_id': r'"webapp.user-detail":{"userInfo":{"user":{"id":"(\d+)"',
            'unique_id': r'"uniqueId":"(.*?)"',
            'nickname': r'"nickname":"(.*?)"',
            'followers': r'"followerCount":(\d+)',
            'following': r'"followingCount":(\d+)',
            'likes': r'"heartCount":(\d+)',
            'videos': r'"videoCount":(\d+)',
            'signature': r'"signature":"(.*?)"',
            'verified': r'"verified":(true|false)',
            'secUid': r'"secUid":"(.*?)"',
            'commentSetting': r'"commentSetting":(\d+)',
            'privateAccount': r'"privateAccount":(true|false)',
            'region': r'"ttSeller":false,"region":"([^"]*)"',
            'heart': r'"heart":(\d+)',
            'diggCount': r'"diggCount":(\d+)',
            'friendCount': r'"friendCount":(\d+)',
            'profile_pic': r'"avatarLarger":"(.*?)"'
        }
        
        info = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, html_content)
            info[key] = match.group(1) if match else f"No {key} found"
        
        if "profile_pic" in info:
            info['profile_pic'] = info['profile_pic'].replace('\\u002F', '/')
        
        social_links = []
        bio = info.get('signature', "")
        
        # METHOD 1: Extract links with target parameter
        link_urls = re.findall(r'href="(https://www\.tiktok\.com/link/v2\?[^"]*?scene=bio_url[^"]*?target=([^"&]+))"', html_content)
        for full_url, target in link_urls:
            target_decoded = urllib.parse.unquote(target)
            text_pattern = rf'href="{re.escape(full_url)}"[^>]*>.*?<span[^>]*SpanLink[^>]*>([^<]+)</span>'
            text_match = re.search(text_pattern, html_content, re.DOTALL)
            if text_match:
                link_text = text_match.group(1)
            else:
                link_text = target_decoded
            if not any(target_decoded in s for s in social_links):
                social_links.append(f"Link: {link_text} - {target_decoded}")
        
        # METHOD 2: Find all SpanLink classes
        span_links = re.findall(r'<span[^>]*class="[^"]*SpanLink[^"]*">([^<]+)</span>', html_content)
        for span_text in span_links:
            if '.' in span_text and ' ' not in span_text and not any(span_text in s for s in social_links):
                social_links.append(f"Link: {span_text} - {span_text}")
        
        # METHOD 3: Find all target parameters
        all_targets = re.findall(r'scene=bio_url[^"]*?target=([^"&]+)', html_content)
        for target in all_targets:
            target_decoded = urllib.parse.unquote(target)
            if not any(target_decoded in s for s in social_links):
                text_pattern = rf'target={re.escape(target)}[^>]*>.*?<span[^>]*>([^<]+)</span>'
                text_match = re.search(text_pattern, html_content, re.DOTALL)
                if text_match:
                    link_text = text_match.group(1)
                else:
                    link_text = target_decoded
                social_links.append(f"Link: {link_text} - {target_decoded}")
        
        # METHOD 4: Extract bioLink links from JSON
        bio_link_pattern = r'"bioLink":{"link":"([^"]+)","risk":(\d+)}'
        bio_links_matches = re.findall(bio_link_pattern, html_content)
        for link, risk in bio_links_matches:
            clean_link = link.replace('\\u002F', '/')
            if not any(clean_link in s for s in social_links):
                social_links.append(f"💎 **{clean_link}**: `{clean_link}`")
        
        shared_links_pattern = r'"shareUrl":"([^"]+)"'
        shared_links_matches = re.findall(shared_links_pattern, html_content)
        for shared_url in shared_links_matches:
            clean_url = shared_url.replace('\\u002F', '/')
            if not any(clean_url in s for s in social_links):
                social_links.append(f"💎 **{clean_url}**: `{clean_url}`")
        
        share_links_div_pattern = re.compile(r'<div[^>]*class="[^"]*DivShareLinks[^"]*"[^>]*>(.*?)</div>', re.DOTALL)
        for div_match in share_links_div_pattern.finditer(html_content):
            div_content = div_match.group(1)
            div_links = re.finditer(r'<a[^>]*href="[^"]*scene=bio_url[^"]*target=([^"&]+)"[^>]*>.*?<span[^>]*class="[^"]*SpanLink[^"]*">([^<]+)</span>', div_content, re.DOTALL)
            for link_match in div_links:
                target = urllib.parse.unquote(link_match.group(1))
                link_text = link_match.group(2)
                if not any(target in s or link_text in s for s in social_links):
                    social_links.append(f"💎 **{link_text}**: `{target}`")
        
        span_matches = re.findall(r'<span[^>]*class="[^"]*SpanLink[^"]*">([^<]+)</span>', html_content)
        for span_text in span_matches:
            if '.' in span_text and not any(span_text in s for s in social_links):
                social_links.append(f"Link: {span_text} - {span_text}")
        
        biolink_matches = re.findall(r'class="[^"]*ABioLink[^"]*"[^>]*>.*?<span[^>]*class="[^"]*SpanLink[^"]*">([^<]+)</span>', html_content, re.DOTALL)
        for span_text in biolink_matches:
            if not any(span_text in s for s in social_links):
                social_links.append(f"Link: {span_text} - {span_text}")
        
        # METHOD 5: Extract social networks from bio
        ig_pattern = re.search(r'[iI][gG]:\s*@?([a-zA-Z0-9._]+)', bio)
        if ig_pattern:
            instagram_username = ig_pattern.group(1)
            if not any(f"Instagram: @{instagram_username}" in s for s in social_links):
                social_links.append(f"Instagram: @{instagram_username}")
        
        social_patterns = {
            'snapchat': r'([sS][cC]|[sS]napchat):\s*@?([a-zA-Z0-9._]+)',
            'twitter': r'([tT]witter|[xX]):\s*@?([a-zA-Z0-9._]+)',
            'facebook': r'[fF][bB]:\s*@?([a-zA-Z0-9._]+)',
            'youtube': r'([yY][tT]|[yY]outube):\s*@?([a-zA-Z0-9._]+)',
            'telegram': r'[tT]elegram:\s*@?([a-zA-Z0-9._]+)'
        }
        
        for platform, pattern in social_patterns.items():
            match = re.search(pattern, bio)
            if match:
                username = match.group(2) if len(match.groups()) > 1 else match.group(1)
                if platform == 'snapchat':
                    social_link = f"Snapchat: {username}"
                elif platform == 'twitter':
                    social_link = f"Twitter/X: @{username}"
                elif platform == 'facebook':
                    social_link = f"Facebook: {username}"
                elif platform == 'youtube':
                    social_link = f"YouTube: {username}"
                elif platform == 'telegram':
                    social_link = f"Telegram: @{username}"
                if not any(social_link in s for s in social_links):
                    social_links.append(social_link)
        
        email_pattern = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', bio)
        if email_pattern:
            email = email_pattern.group(0)
            if not any(email in s for s in social_links):
                social_links.append(f"Email: {email}")
        
        info['social_links'] = social_links
        return info
    else:
        print(f"{Colors.RED}✗ Error: Unable to fetch profile. Status code: {response.status_code}{Colors.RESET}")
        return None

# ========== DISPLAY FUNCTIONS ==========
def display_user_info(info):
    """Display user information with styling"""
    if not info:
        return
    
    print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.WHITE}                  📊 USER INFORMATION{Colors.CYAN}                        ║{Colors.RESET}")
    print(f"{Colors.CYAN}╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}┌─────────────────────────────────────────────────────────────┐{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.YELLOW} Basic Information{Colors.GREEN}                                              │{Colors.RESET}")
    print(f"{Colors.GREEN}├─────────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} User ID     : {Colors.CYAN}{info.get('user_id', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Username    : {Colors.CYAN}@{info.get('unique_id', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Nickname    : {Colors.CYAN}{info.get('nickname', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Verified    : {Colors.GREEN if info.get('verified') == 'true' else Colors.RED}{info.get('verified', 'N/A')}{Colors.GREEN}                              │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Private     : {Colors.RED if info.get('privateAccount') == 'true' else Colors.GREEN}{info.get('privateAccount', 'N/A')}{Colors.GREEN}                              │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Region      : {Colors.CYAN}{info.get('region', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}└─────────────────────────────────────────────────────────────┘{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}┌─────────────────────────────────────────────────────────────┐{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.YELLOW} Statistics{Colors.GREEN}                                                  │{Colors.RESET}")
    print(f"{Colors.GREEN}├─────────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Followers   : {Colors.CYAN}{info.get('followers', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Following   : {Colors.CYAN}{info.get('following', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Likes       : {Colors.CYAN}{info.get('likes', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Videos      : {Colors.CYAN}{info.get('videos', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Friends     : {Colors.CYAN}{info.get('friendCount', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Heart       : {Colors.CYAN}{info.get('heart', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}│{Colors.WHITE} Digg Count  : {Colors.CYAN}{info.get('diggCount', 'N/A')}{Colors.GREEN}                             │{Colors.RESET}")
    print(f"{Colors.GREEN}└─────────────────────────────────────────────────────────────┘{Colors.RESET}")
    
    bio = info.get('signature', 'No bio available')
    if bio != 'No bio available' and bio != 'No signature found':
        print(f"\n{Colors.GREEN}┌─────────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.GREEN}│{Colors.YELLOW} Biography{Colors.GREEN}                                                  │{Colors.RESET}")
        print(f"{Colors.GREEN}├─────────────────────────────────────────────────────────────┤{Colors.RESET}")
        bio_lines = bio.replace('\\n', '\n').split('\n')
        for line in bio_lines[:5]:
            if len(line) > 50:
                line = line[:47] + '...'
            print(f"{Colors.GREEN}│{Colors.WHITE} {line:<57}{Colors.GREEN}│{Colors.RESET}")
        print(f"{Colors.GREEN}└─────────────────────────────────────────────────────────────┘{Colors.RESET}")
    
    social_links = info.get('social_links', [])
    if social_links:
        print(f"\n{Colors.GREEN}┌─────────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.GREEN}│{Colors.YELLOW} Social Links & Contacts{Colors.GREEN}                                       │{Colors.RESET}")
        print(f"{Colors.GREEN}├─────────────────────────────────────────────────────────────┤{Colors.RESET}")
        for link in social_links[:5]:
            if len(link) > 50:
                link = link[:47] + '...'
            print(f"{Colors.GREEN}│{Colors.CYAN} • {link:<56}{Colors.GREEN}│{Colors.RESET}")
        print(f"{Colors.GREEN}└─────────────────────────────────────────────────────────────┘{Colors.RESET}")
    
    print(f"\n{Colors.CYAN}🔗 Profile URL: {Colors.WHITE}https://www.tiktok.com/@{info.get('unique_id', 'N/A')}{Colors.RESET}")

def download_profile_picture(url, username):
    """Download profile picture"""
    if not url or url == 'No profile_pic found' or not url.startswith('http'):
        print(f"\n{Colors.YELLOW}⚠ No profile picture URL found{Colors.RESET}")
        return
    
    try:
        print(f"\n{Colors.CYAN}┌─────────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.YELLOW} Download Profile Picture{Colors.CYAN}                                        │{Colors.RESET}")
        print(f"{Colors.CYAN}├─────────────────────────────────────────────────────────────┤{Colors.RESET}")
        
        if not os.path.exists('pp_images'):
            os.makedirs('pp_images')
            print(f"{Colors.CYAN}│{Colors.GREEN} ✓ Created pp_images folder{Colors.CYAN}                             │{Colors.RESET}")
        
        loading_animation("Downloading profile picture", 2)
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            filename = f"pp_images/{username}_profile.jpg"
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            file_size = len(response.content) / 1024
            print(f"{Colors.CYAN}│{Colors.GREEN} ✓ Downloaded: {filename}{Colors.CYAN}                        │{Colors.RESET}")
            print(f"{Colors.CYAN}│{Colors.GREEN} ✓ File Size: {file_size:.1f} KB{Colors.CYAN}                           │{Colors.RESET}")
            print(f"{Colors.CYAN}└─────────────────────────────────────────────────────────────┘{Colors.RESET}")
        else:
            print(f"{Colors.CYAN}│{Colors.RED} ✗ Download failed (Status: {response.status_code}){Colors.CYAN}             │{Colors.RESET}")
            print(f"{Colors.CYAN}└─────────────────────────────────────────────────────────────┘{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.CYAN}│{Colors.RED} ✗ Error: {str(e)[:40]}{Colors.CYAN}                            │{Colors.RESET}")
        print(f"{Colors.CYAN}└─────────────────────────────────────────────────────────────┘{Colors.RESET}")

def bulk_scraper():
    """Bulk username scraper"""
    print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.YELLOW}  📝 Bulk Username Scraper{Colors.CYAN}                                         ║{Colors.RESET}")
    print(f"{Colors.CYAN}╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    print(f"\n{Colors.WHITE}Enter usernames (one per line, press Enter twice to finish):{Colors.RESET}")
    
    usernames = []
    while True:
        line = input(f"{Colors.CYAN}> {Colors.WHITE}")
        if not line and usernames:
            break
        if line:
            usernames.append(line.strip())
    
    if not usernames:
        print(f"\n{Colors.YELLOW}No usernames entered.{Colors.RESET}")
        return
    
    print(f"\n{Colors.CYAN}📊 Processing {len(usernames)} usernames...{Colors.RESET}")
    
    results = []
    for i, username in enumerate(usernames, 1):
        print(f"\n{Colors.WHITE}[{i}/{len(usernames)}] Processing @{username}...{Colors.RESET}")
        info = get_user_info(username)
        if info:
            results.append(info)
            print(f"{Colors.GREEN}✓ Success{Colors.RESET}")
        else:
            print(f"{Colors.RED}✗ Failed{Colors.RESET}")
        time.sleep(0.5)
    
    if results:
        filename = f"bulk_results_{int(time.time())}.json"
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n{Colors.GREEN}✓ Results saved to: {filename}{Colors.RESET}")
    
    print(f"\n{Colors.GREEN}✓ Processed {len(results)}/{len(usernames)} profiles successfully{Colors.RESET}")

def main():
    while True:
        try:
            clear_screen()
            hacker_animation(1)
            print_banner()
            print_menu()
            
            choice = input(f"\n{Colors.CYAN}┌─{Colors.WHITE}[{Colors.GREEN}Select Option{Colors.WHITE}]{Colors.CYAN}\n└──╼ {Colors.WHITE}")
            
            if choice == '1':
                clear_screen()
                hacker_animation(1)
                print_banner()
                
                print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.YELLOW}  👽 Username to Information{Colors.CYAN}                                     ║{Colors.RESET}")
                print(f"{Colors.CYAN}╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
                
                print(f"\n{Colors.WHITE}Enter TikTok Username (with or without @):{Colors.RESET}")
                username = input(f"{Colors.CYAN}> {Colors.WHITE}").strip()
                
                if username:
                    info = get_user_info(username)
                    if info:
                        display_user_info(info)
                        
                        print(f"\n{Colors.YELLOW}Download profile picture? (y/n):{Colors.RESET}")
                        download_choice = input(f"{Colors.CYAN}> {Colors.WHITE}").strip().lower()
                        
                        if download_choice == 'y':
                            download_profile_picture(info.get('profile_pic', ''), info.get('unique_id', username))
                        
                        print(f"\n{Colors.GREEN}✓ Done! Press Enter to continue...{Colors.RESET}")
                        input()
                    else:
                        print(f"\n{Colors.RED}✗ Failed to fetch data. Press Enter to continue...{Colors.RESET}")
                        input()
                else:
                    print(f"\n{Colors.YELLOW}⚠ No username entered. Press Enter to continue...{Colors.RESET}")
                    input()
                    
            elif choice == '2':
                clear_screen()
                hacker_animation(1)
                print_banner()
                bulk_scraper()
                print(f"\n{Colors.GREEN}Press Enter to continue...{Colors.RESET}")
                input()
                
            elif choice == '3':
                print(f"\n{Colors.RED}╔══════════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.RED}║{Colors.YELLOW}  👋 Thank you for using TikTok Scraper!{Colors.RED}                         ║{Colors.RESET}")
                print(f"{Colors.RED}║{Colors.MAGENTA}  Developed by ᴀꜱɪꜰ ɪꜱʟᴀᴍ{Colors.RED}                                         ║{Colors.RESET}")
                print(f"{Colors.RED}╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
                loading_animation("Exiting", 1)
                sys.exit(0)
                
            else:
                print(f"\n{Colors.RED}✗ Invalid option! Press Enter to continue...{Colors.RESET}")
                input()
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}⚠ Interrupted by user{Colors.RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"\n{Colors.RED}✗ Error: {str(e)}{Colors.RESET}")
            input(f"{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")

if __name__ == "__main__":
    main()
