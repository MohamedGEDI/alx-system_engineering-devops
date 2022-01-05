#execute a command
exec {'killmenow':
  command => 'pkill -n killmenow',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  oniyif  => 'test `pgrep killmenow | wc -l` -ge 1',
}
