<?php
session_start();
include "flag.php";
include "secret.php";

if(isset($_SESSION["user"])){
  if($_SESSION["user"]==="santa_claus ")  echo "".$flag;
	 
}

class secret{

       
         public $yoursecret;
         public $descript;
         public $filename; 
     
              function __toString(){
                  global $secret;
                  $secret1 ="".$secret;
                  return $secret1;
                
              }
              function __destruct(){
                  global $secret;
                   if ("".$this->yoursecret === "".$secret) {
                      $filename=str_replace(".", "", $this->filename);
                      $filename=str_replace("/", "", $this->filename);
                      file_put_contents("/tmp/".$filename, $this->descript);
                      
    		              
                   }   
              }
}
if (isset($_GET['ser'])) unserialize($_GET['ser']);

        

        ?>