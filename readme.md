==> Dependancies needed to run this environment.

* on an intel machine, install VIRTUALBOX.
* on a M1 machine, install VMWAREFUSION.

-------------------------------------------------------------------------------------------------------------------------
==> Instruction to provision on an intel machine.

1. Go to the terminal and enter: vagrant up
2. follow the instruction to run the game below.

-------------------------------------------------------------------------------------------------------------------------
==> Instruction to provision on an M1 machine.
The current state of the files are set up to run for windows, if you need to run it on an M1, follow the step below.

1. go into the vagrant file and comment out the windows part
2. remove the comment for the M1, use the second code to provision.
3. In the terminal, run: vagrant up

--------------------------------------------------------------------------------------------------------------------------

==> Instructions to run the game.py

1. SSH into the machine after provisioning; vagrant ssh
2. cd into app folder that contains the game: cd app
3. run python3 game.py

---------------------------------------------------------------------------------------------------------------------------

