<?php
include 'flag.php';
error_reporting(0);
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    extract($_POST);

    if ($pass == $newpass) {
        echo $flag;
    }
}
highlight_file(__FILE__);
