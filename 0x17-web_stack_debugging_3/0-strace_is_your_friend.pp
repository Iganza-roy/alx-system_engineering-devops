#fix a typo or error in the WordPress wp-settings.php file where phpp should be php

exec { 'fix-typo':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
