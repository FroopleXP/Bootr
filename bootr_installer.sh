sudo cp install_files/rom_bootr.py /bin/
sudo cp install_files/bootr /bin/
sudo echo "bootr" >> /etc/profile
sudo mkdir /boot/ROMS/_config/
sudo cp install_files/lib_cores.json /boot/ROMS/_config/
sudo rm /opt/retropie/supplementary/splashscreen/retropie-default.png
sudo cp install_files/retropie-default.png /opt/retropie/supplementary/splashscreen/
sudo reboot now
