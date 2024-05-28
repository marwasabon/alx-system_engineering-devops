#!/usr/bin/env bash
# Update package lists
sudo apt update

# Install MySQL Server
sudo apt install -y mysql-server

# Secure MySQL installation (optional: Configure root password, remove anonymous users, etc.)
# sudo mysql_secure_installation
