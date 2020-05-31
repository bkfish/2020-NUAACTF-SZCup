<?php
class lemon {
    protected $ClassObj;
    function __construct() {
        $this->ClassObj = new normal();
    }
    function __destruct() {
        $this->ClassObj->action();
    }
}
class normal {
    function action() {
        echo "<img src=\"haha.png\" alt=\"\">";
    }
}
class evil {
    private $data;
    function action() {
        show_source("flag.php");
    }
}
if(isset($_GET['d'])){
	unserialize($_GET['d']);
}
else{
   $stack=new lemon();
}
