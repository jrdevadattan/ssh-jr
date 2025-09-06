```
          _           _      
  ___ ___| |__       (_)_ __ 
 / __/ __| '_ \ _____| | '__|
 \__ \__ \ | | |_____| | |   
 |___/___/_| |_|    _/ |_|   
                   |__/      
```

A simple Python script for brute-forcing SSH credentials using a wordlist, powered by [`paramiko`](https://pypi.org/project/paramiko/).

## 🛠️ Features


- 🖥️ Prompts for hostname, username, and wordlist path
- 🔑 Attempts SSH login for each password in the wordlist
- ✅ Reports success or failure for each attempt

## 📦 Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/jrdevadattan/ssh-jr.git
    cd ssh-jr
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## 📚 Usage

1. **Prepare your wordlist:**  
   You can find the wordlist resouces below.

2. **Run the script:**

    ```sh
    python main.py
    ```

3. **Follow the prompts:**

    - Enter the target hostname or IP
    - Enter the username
    - Enter the path to your wordlist file

## 💡 Example

```
Enter hostname or IP: 192.168.1.10
Enter username: admin
Enter path to wordlist file: rockyou.txt
```

## 📖 Wordlist Resources

- [SecLists (GitHub)](https://github.com/danielmiessler/SecLists/tree/master/Passwords)
- [Weakpass](https://weakpass.com/)
- [rockyou.txt (SecLists)](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz)

## 🗺️ Future Plans

- ⚡ Add threading to make brute-force faster
- 🚀 Optimize performance for large wordlists
- 📝 More logging and reporting features

## ⚠️ Disclaimer

This tool is for educational and authorized testing purposes only.  
**Do not use it on systems without explicit permission.**

---
