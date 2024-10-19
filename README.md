## Preparation 💼  
You must have a server with **Python 3.10** or higher installed. Also, make sure you have **python-pip** installed.

## Installation 📥  
1. Clone the repository into the desired directory on your server using the command:  
   ```  
   git clone https://github.com/BANedetta/telegram-bot my_catalog  
   ```  
   *(replace `my_catalog` with your directory name)*. If you don't have **GIT** installed, use:  
   ```  
   apt install git  
   ```  
   If you're on **Windows**, download the repository as a **ZIP** and extract it.  

2. Grant execution rights to the **installer** script:  
   ```  
   chmod +x installer.sh  
   ```  
   On **Windows**, skip this step.  

3. Run the **installer**:  
   ```  
   ./installer.sh  
   ```  
   *(on **Windows** run **installer.cmd**)* and wait for the installation to complete.  

4. Configure **config.py** in the **config** directory for your game server. Go to the channel settings and add a chat for discussion, then add the ID _(or username)_ of the chat and channel to **config.py**.

5. Create a **.env** file and fill it out based on the **.env_example** file.  

6. Run the script **start.sh** *(**start.cmd** for **Windows**)*.  


### Important ⚠️  
This bot is useless without a plugin on the game server, so set everything up there first.
