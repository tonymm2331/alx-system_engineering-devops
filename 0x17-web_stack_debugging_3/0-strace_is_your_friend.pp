{ 'install_missing_library':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get install -y <missing-library>',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
}

file { '/etc/apache2/sites-available/default':
  ensure  => file,
  content => '<your-configured-content>',
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/apache2/sites-available/default'],
}
