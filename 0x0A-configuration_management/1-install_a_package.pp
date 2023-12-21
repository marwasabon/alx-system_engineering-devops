# install flask from pip3.
package { 'pip3':
	ensure   => '2.1.0',
	provider => 'flask',
	}
#exec { 'install_flask':
#  command => '/usr/bin/pip3 install Flask==2.1.0',
#  path    => ['/usr/bin'],
#}
