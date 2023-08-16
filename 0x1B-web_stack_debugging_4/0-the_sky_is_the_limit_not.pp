# Reconfigure nginx to handle more traffic
exec { 'reconfig-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['nginx-restart'],
}

# Restart nginx to apply the changes
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
  refreshonly => true,
}
