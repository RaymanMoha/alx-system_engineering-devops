# Change the OS configuration so that it is possible to
# login with the holberton user and open a file without any error message.

exec { 'increase hard open files limit for user holberton':
  command => '/bin/sed -i "s/holberton h.*/holberton hard nofile 3000/" /etc/security/limits.conf'
}

# Increase soft open files limit for user .
exec { 'increase-soft-file-limit-for-holberton-user':
  command => '/bin/sed -i "s/holberton s.*/holberton soft nofile 3000/" /etc/security/limits.conf'
}
