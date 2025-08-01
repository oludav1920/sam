<?php
$pass="mysecretpassword";
$hash=password_hash($pass, PASSWORD_BCRYPT);
echo $hash;

?>