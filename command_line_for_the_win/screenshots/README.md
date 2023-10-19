Marwa’s Project
This project is about using SFTP to upload screenshots to a remote server and then pushing them to GitHub.
To complete this challenge, follow the steps below:

Open your terminal or shell or command prompt on your local machine.
Use the following command to establish a connection to the sandbox environment:sftp username@hostname

Replace username with your sandbox environment username and hostname with the provided hostname. You will be prompted to enter your password. Enter the password provided to you for the sandbox environment.
Make sure you have the directory “screenshots” under “command_line_for_the_win”. Use the cd command to navigate to the directory where you want to upload the screenshots. For example, if you want to navigate to the screenshots directory, use the following command:cd command_line_for_the_win/screenshots


Use the put command followed by the file path of the screenshot on your local machine to upload the screenshots. For example, if your screenshot is located at /path/to/screenshot.png, use the following command:put /path/to/screenshot.png

Make sure to replace /path/to/screenshot.png with the full path to your screenshots.
Once the screenshots are uploaded, you can confirm their presence by using the ls command to list the files in the current directory. For example:ls

This will show a list of files, including the uploaded screenshots.
Finally, you can proceed to push the screenshots to GitHub as per the initial requirements of the project.

That it! You have successfully uploaded screenshots using SFTP and can now push them to GitHub.
