#!/usr/bin/env python3
import requests
import json
import os
import sys
from datetime import datetime

PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[1;91m'
RESET = '\033[0m'

def print_banner():
    banner = f"""{PURPLE}
╔══════════════════════════════════════════════╗
║                                              ║
║          ██╗    ██╗███████╗██╗   ██╗███╗   ██╗          ║
║          ██║    ██║██╔════╝╚██╗ ██╔╝████╗  ██║          ║
║          ██║ █╗ ██║█████╗   ╚████╔╝ ██╔██╗ ██║          ║
║          ██║███╗██║██╔══╝    ╚██╔╝  ██║╚██╗██║          ║
║          ╚███╔███╔╝███████╗   ██║   ██║ ╚████║          ║
║           ╚══╝╚══╝ ╚══════╝   ╚═╝   ╚═╝  ╚═══╝          ║
║                                              ║
╚══════════════════════════════════════════════╝{RESET}

{RED}        FACEBOOK TOKEN GETTER
        
Format: uid|password or email|password{RESET}
    """
    print(banner)

def get_facebook_token(email, password):
    """Get Facebook access token for a single account"""
    session = requests.Session()
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
        response = session.post(
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

def get_accounts_direct_input():
    """Get accounts directly from bulk paste input"""
    print("Paste accounts (one per line), then press Enter twice:\n")
    
    accounts = []
    lines = []
    
    try:
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
    except (KeyboardInterrupt, EOFError):
        if not lines:
            print("\n\n[!] Cancelled by user")
            return None
    
    # Process all lines
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
        
        if '|' not in line:
            print(f"    [!] Skipping invalid format: {line[:30]}...")
            continue
        
        parts = line.split('|', 1)
        if len(parts) == 2 and parts[0].strip() and parts[1].strip():
            accounts.append(line)
        else:
            print(f"    [!] Skipping invalid entry: {line[:30]}...")
    
    print(f"\n[*] Loaded {len(accounts)} valid account(s)")
    return accounts

def process_accounts(accounts):
    """Process list of account strings"""
    total_accounts = len(accounts)
    
    if total_accounts == 0:
        print("\n[!] No accounts to process!")
        return
    
    print(f"\n[*] Processing {total_accounts} account(s)...\n")
    
    successful = 0
    failed = 0
    results = []
    
    for idx, line in enumerate(accounts, 1):
        parts = line.split('|', 1)
        uid = parts[0].strip()
        password = parts[1].strip()
        
        print(f"[{idx}/{total_accounts}] Processing: {uid}...", end=' ')
        
        result = get_facebook_token(uid, password)
        
        if result['success']:
            print(f"{GREEN}✓ SUCCESS{RESET}")
            print(f"{GREEN}    {uid}|{result['token']}{RESET}")
            successful += 1
            results.append({
                'uid': uid,
                'status': 'success',
                'token': result['token'],
                'cookie': result['cookie'],
                'c_user': result['c_user'],
                'datr': result['datr'],
                'appstate': result['appstate']
            })
        else:
            print(f"{RED}✗ FAILED: {result['error']}{RESET}")
            failed += 1
            results.append({
                'uid': uid,
                'status': 'failed',
                'error': result['error']
            })
    
    save_results(results, total_accounts, successful, failed)

def save_results(results, total_accounts, successful, failed):
    """Save results to files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    results_file = f"results_{timestamp}.txt"
    tokens_file = f"tokens_{timestamp}.txt"
    
    with open(results_file, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("WEYN - Facebook Bulk Token Generator Results\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        
        for result in results:
            f.write(f"\n{'='*80}\n")
            f.write(f"UID: {result['uid']}\n")
            f.write(f"Status: {result['status'].upper()}\n")
            
            if result['status'] == 'success':
                f.write(f"\nAccess Token:\n{result['token']}\n")
                f.write(f"\nCookie:\n{result['cookie']}\n")
                f.write(f"\nC_USER: {result['c_user']}\n")
                f.write(f"DATR: {result['datr']}\n")
                f.write(f"\nAppState:\n{json.dumps(result['appstate'], indent=2)}\n")
            else:
                f.write(f"\nError: {result['error']}\n")
            
            f.write(f"{'='*80}\n")
    
    with open(tokens_file, 'w') as f:
        for result in results:
            if result['status'] == 'success':
                f.write(f"{result['uid']}|{result['token']}\n")
    
    print(f"\n{'='*80}")
    print(f"[*] Processing Complete!")
    print(f"[*] Total Accounts: {total_accounts}")
    print(f"[*] Successful: {GREEN}{successful}{RESET}")
    print(f"[*] Failed: {RED}{failed}{RESET}")
    if total_accounts > 0:
        print(f"[*] Success Rate: {(successful/total_accounts*100):.1f}%")
    
    if successful > 0:
        print(f"\n{GREEN}[*] ALL TOKENS (uid|token format):{RESET}")
        print(f"{'='*80}")
        for result in results:
            if result['status'] == 'success':
                print(f"{GREEN}{result['uid']}|{result['token']}{RESET}")
        print(f"{'='*80}")
    
    print(f"\n[*] 📁 Results saved to:")
    print(f"    - {results_file} (detailed)")
    print(f"    - {tokens_file} (tokens only)")
    
    if successful > 0:
        print(f"\n{GREEN}[*] ✅ {successful} token(s) successfully generated!{RESET}")
    
    print(f"{'='*80}\n")

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def show_menu():
    """Show menu options after processing"""
    print("\n" + "="*80)
    print("[1] Generate More Tokens")
    print("[2] Exit")
    print("="*80)
    
    while True:
        try:
            choice = input("\nSelect option: ").strip()
            if choice == "1":
                return True
            elif choice == "2":
                return False
            else:
                print("[!] Invalid option. Enter 1 or 2.")
        except (KeyboardInterrupt, EOFError):
            return False

def main():
    while True:
        clear_screen()
        print_banner()
        
        accounts = get_accounts_direct_input()
        
        if accounts is None:
            print("\n[!] Exiting...")
            break
        
        if len(accounts) == 0:
            print("\n[!] No accounts entered!")
            if not show_menu():
                break
            continue
        
        process_accounts(accounts)
        
        if not show_menu():
            clear_screen()
            print("\nThank you for using FB TOKEN GETTER!\n")
            break

if __name__ == "__main__":
    main()
