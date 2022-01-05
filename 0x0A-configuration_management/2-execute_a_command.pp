#execute a command
exec {'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/local/sbin:/usr/local/bin',
}
