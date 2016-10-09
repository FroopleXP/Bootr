sudo git pull origin master
sudo rm /bin/rom_bootr.py
sudo cp install_files/rom_bootr.py /bin/
sudo rm /boot/ROMS/_config/lib_cores.json
sudo cp install_files/lib_cores.json /boot/ROMS/_config/
sudo reboot now
