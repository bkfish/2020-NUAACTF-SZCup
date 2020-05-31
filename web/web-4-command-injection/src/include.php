<?php  error_reporting(0);
@$file = $_GET["file"];
if(isset($file)) {
	if (preg_match('/http|data|ftp|input|%00|flag/i', $file) || strstr($file,"..") !== FALSE || strlen($file)>=100) {
		echo "<p> error! </p>";
	} else {
		include($file.'.php');
		setcookie("tips","createfun.php");
	}
} else {
	header('Location:include.php?file=index');
}
?>