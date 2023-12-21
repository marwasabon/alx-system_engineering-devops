#!/usr/bin/pup
# install flask from pip3.
#package { 'flask':
#ensure   => '2.1.0',
#provider => 'pip3',
#}i
# Installing a flask package

#Using the exec command to ensure that we apt-update

exec {'apt-update':
  command => '/usr/bin/apt-get update'
}

#Install python 3.8.10
package {'python3.8':
  ensure =>  '3.8.10',
}

#Install pip and ensrue that the system is update before doing it
package {'python3-pip':
  ensure  => present,
  require =>  Exec['apt-update']
}

# Install flask and enure this pip is installed first.

package {'flask':
  ensure   => '2.1.0',
  require  => Package['python3-pip'],
  provider => 'pip',
}


# Install Werkzeug 2.1.1
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  =>  Package['python3-pip'],
}
