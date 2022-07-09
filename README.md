# Automatic-Youtube-and-Video-Downloader
#### I created this Bot for My Perosnal use . We can Download Youtube Videos and other streamable Videos using this Bot. we can automate this Bot using  Cron job in Linux and Mac os

#### Now we are going to Automate this python sciprt to  run  exactly at every 1:00 am for Everyday.

* #### Step 1 : Run This Commmand to Know the Directory of python3
              
              foo@bar:~$ Which Python3
              usr/bin/python3
              
* #### Step 2: open the Terminal and type this command

          crontab-e
    
* #### Step 3: This will open an editor . Type the below command to run our python script . Then save and Exit
          
          00 01 * * * usr/bin/python3 <path of our python File>
          
          
* #### step 4: Now We have to start the Cron job  by this command

        service crond start
        
* #### Thats all Our Python Script will run every 1:00 am for Everyday . if you Want to stop the cron job use this command
        
        service crond stop
        
> Note : For Debian or Ubuntu Based Distros you have to use Sudo infront of crond commands
