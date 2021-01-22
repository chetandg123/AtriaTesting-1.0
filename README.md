AtriaTesting-1.0
Prerequisites:
  To Run Selenium python scripts ,Install pycharm in your system
  Google Chrome need to be installed in the server or local machine.
  Chrome driver need to be downloaded and placed in the AtriaTesting-1.0/Driver folder
Steps to install the google chrome

  Open the terminal (Ctrl+Alt+t) in the ubuntu
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  sudo apt install ./google-chrome-stable_current_amd64.deb
  Check chrome brower version using command -> google-chrome -version
  	
Steps to Download the chrome driver 
Note: Based on chrome browser version need to download chrome driver 
   https://sites.google.com/a/chromium.org/chromedriver/downloads

Steps to execute the test script
	1.Open the Terminal (Ctrl+Alt+t) in the ubuntu
	2.Clone the Atria Project-1.0 project from github i.e git clone [repository url] 
	2.sudo apt update
	3.sudo apt install python3-pip
	4.Execute the Requirement.txt in the terminal (Requirement.txt file present in the cQubeTesting-1.9 Folder) [mandatory]
	    sudo pip3 install -r Requirement.txt 
