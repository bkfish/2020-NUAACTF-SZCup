<?php

show_source("index.php");

function filter_nohack($data) {
    return str_replace('flag', '', $data);

}

class A{
    public $username;
    public $password;
    function __construct($a, $b){
        $this->username = $a;
        $this->password = $b;
    }
}
class B{
    public $b = 'gqy';
    function __destruct(){
        $c = 'a'.$this->b;
        echo $c;
    }
}
class C{
    public $c;
    function __toString(){
        //flag.php
        echo file_get_contents($this->c);
       return 'nice';
    }

}

$a = new A($_GET['a'],$_GET['b']);

$b = unserialize(filter_nohack(serialize($a)));