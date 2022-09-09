==> Dependancies needed to run this environment.

* on an intel machine, VIRTUALBOX will be needed.
* on an M1 machine, VMWAREFUSION will be needed.



-------------------------------------------------------------------------------------------------------------------------
==> Instruction to provision the machine for a M1.
The current state of the files are set up to run for windows, if you need to run it on an M1, follow the step below.

1. go into the vagrant file and comment out the windows part
2. remove the comment for the arm, use the second code to provision.


--------------------------------------------------------------------------------------------------------------------------

==> Instructions to run the game.py

1. SSH into the machine after provisioning; vagrant ssh
2. cd into app folder that contains the game; cd app
3. run python3 game.py

---------------------------------------------------------------------------------------------------------------------------

