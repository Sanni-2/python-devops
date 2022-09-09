#!/bin/bash
echo -------------- Update source list --------------
sudo apt-get update -y

echo -------------- Install Python ------------------
sudo apt-get install software-properties-common -y


echo --------------- Move into App Folder -----------
cd ../vagrant/app
pwd


# echo -------------------- Run App -------------------
# python3 game.py


