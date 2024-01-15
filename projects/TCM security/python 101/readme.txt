-------------------------------------------------------------------------------------
To be able to test script #1 you must run SSH service in your Kali localhost machine.
-------------------------------------------------------------------------------------
Follow these commands:
# enable ssh service
> sudo service ssh start

# check the status of the SSH service
> sudo service ssh status

# disbale ssh service
> sudo systemctl ssh stop


-------------------------------------------------------------------------------------
To be able to test script #2 you must enter a valid sha256 hash.
-------------------------------------------------------------------------------------
Follow these commands:
# create a sha256 hash
> echo -ne 123456 | sha256sum

# run the script
> python3 sha256-cracking.py <sha256sum>
