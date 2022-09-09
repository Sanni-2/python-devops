
# WINDOWS
Vagrant.configure("2") do |config|
  # Provisioning Python App
  config.vm.define "pythonapp" do |pythonapp|
    pythonapp.vm.box = "ubuntu/bionic64"
    pythonapp.vm.network "private_network", ip: "192.168.56.10"
    pythonapp.vm.provider "virtualbox" do |vb|
      pythonapp.vm.synced_folder "app/", "/home/vagrant/app/"
      pythonapp.vm.synced_folder "env/", "/home/vagrant/env"
    end
    pythonapp.vm.provision "shell", path: "env/pythonapp/script.sh"
  end
end


# USE THIS FOR ARM
# Vagrant.configure("2") do |config|
#   # Provisioning Using VmWareFusion
#   config.vm.define "pythonapp" do |pythonapp|
#     pythonapp.vm.box = "spox/ubuntu-arm"
#     pythonapp.vm.network "private_network", ip: "192.168.56.20"
#     pythonapp.vm.provider "vmware_fusion" do |vb|
#       config.vm.synced_folder "app/", "/home/vagrant/app" 
#     end
#     pythonapp.vm.provision "shell", inline: <<-SHELL
#       systemctl disable apt-daily.service
#       systemctl disable apt-daily.timer
#       sudo apt remove unattended-upgrades -y
#     SHELL
#     pythonapp.vm.provision "shell", path: "env/script.sh"
#   end
# end
