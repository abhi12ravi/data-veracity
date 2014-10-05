<?php
require 'src/facebook.php';  // Include facebook SDK file
require 'functions.php';  // Include functions
$facebook = new Facebook(array(
  'appId'  => '366885740127144',   // Facebook App ID 
  'secret' => 'c4c08662da673dbb6af4538b6481ead3',  // Facebook App Secret
  'cookie' => true,	
));
$user = $facebook->getUser();

if ($user) {
  try {
    $user_profile = $facebook->api('/me');
  	    $fbid = $user_profile['id'];                 // To Get Facebook ID
 	    $fbuname = $user_profile['username'];  // To Get Facebook Username
 	    $fbfullname = $user_profile['name']; // To Get Facebook full name
	    $femail = $user_profile['email'];    // To Get Facebook email ID
	/* ---- Session Variables -----*/
	    $_SESSION['FBID'] = $fbid;           
	    $_SESSION['USERNAME'] = $fbuname;
            $_SESSION['FULLNAME'] = $fbfullname;
	    $_SESSION['EMAIL'] =  $femail;
           checkuser($fbid,$fbuname,$fbfullname,$femail);    // To update local DB
  } catch (FacebookApiException $e) {
    error_log($e);
   $user = null;
  }
}
if ($user) {
	header("Location: home5.php");
} else {
 $loginUrl = $facebook->getLoginUrl(array(
		'scope'		=> 'email','user_about_me' // Permissions to request from the user
		));
 header("Location: ".$loginUrl);
}
?>