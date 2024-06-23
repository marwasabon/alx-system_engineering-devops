# fixing the user having too many files
exec { 'Fixes user too many files open':
  command => "/bin/sed -i 's/holberton.*//g' /etc/security/limits.conf"
}
