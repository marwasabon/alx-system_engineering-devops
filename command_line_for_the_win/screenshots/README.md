#This is Marwa's project i have logged in using sftp
what i did to make this challenge is :
#1 Open you terminal or shell or command prompt on your local machine.
#2 Use the this  command to establish a connection to the sandbox environment:
sftp username@hostnam
or you can click on the SFTP butoon and copy the full commmand.
#3 Replace username with your sandbox environment username and hostname with the provided hostname.
You will be prompted to enter your password. Enter the password provided to you for the sandbox environment.
#4 make sure you have the directory screeenshots undercommand_line_for_the_win
Use the cd command to navigate to the directory where you want to upload the screenshots. 
For example, if you want to navigate to the screenshots directory, use the following command 
cd screenshots.
#5 Use the put command followed by the file path of the screenshot on your local machine to upload the screenshots. For example, if your screenshot is located at /path/to/screenshot.png, use the following command:
put /path/to/screenshot.png (btw write the full path to your screenshots)
#6 once the screens are loaded confirm with ls command to check if your files existed.
#7 Once the screenshots are transferred, you can proceed to push them to GitHub following the initial requirements.
That's it :)
