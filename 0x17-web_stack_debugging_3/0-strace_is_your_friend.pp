# 0-strace_is_your_friend.pp
# This Puppet manifest automates the fix for Apache 500 Internal Server Error
exec { 'fix_apache_error':
  path        => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
  command     => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  refreshonly => true,
}
