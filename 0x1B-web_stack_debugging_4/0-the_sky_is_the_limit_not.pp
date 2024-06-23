# puppets script 
exec { 'Fix nginx requests that failing':
  command => "/bin/echo ULIMIT='-n 5000' | sudo tee /etc/default/nginx && sudo service nginx restart"
}
