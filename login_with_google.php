<?php

require('http.php');

require('oauth_client.php');

$client = new oauth_client_class;

$client->server = 'Google';

$client->debug = false;

$client->debug_http = true;

$client->redirect_uri = 'http://'.$_SERVER['HTTP_HOST'].dirname(strtok($_SERVER['REQUEST_URI'],'?')).'/login_with_google.php';

$client->client_id = '476455004081-ce0tt1e4jcs2dplituusii2pdv6k85sp.apps.googleusercontent.com';/*Client ID*/

$client->client_secret = 'U5_Gi0YODBoDK5Fk2pyoUuNG';/*Client Secret*/

$client->scope = 'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/plus.me';

$application_line = __LINE__;

if(strlen($client->client_id) == 0 || strlen($client->client_secret) == 0){

 die('Please go to Google APIs console page '.

  'http://code.google.com/apis/console in the API access tab, '.

  'create a new client ID, and in the line '.$application_line.

  ' set the client_id to Client ID and client_secret with Client Secret. '.

  'The callback URL must be '.$client->redirect_uri.' but make sure '.

  'the domain is valid and can be resolved by a public DNS.');

}

if(($success = $client->Initialize())){

 if(($success = $client->Process())){

  if(strlen($client->authorization_error)){

   $client->error = $client->authorization_error;

   $success = false;

  }elseif(strlen($client->access_token)){

   $success = $client->CallAPI('https://www.googleapis.com/oauth2/v1/userinfo', 'GET', array(), array('FailOnAccessError'=>true), $user);

   if($success){

    $email=$user->email;

    $name=$user->name;

    $gender=$user->gender;

    $birthday=date('d/m/Y', strtotime($user->birthday));

    $image=$user->picture;

   }

  }

 }

 $success = $client->Finalize($success);

}

if($client->exit){

 die("Something Happened","<a href='".$client->redirect_uri."'>Try Again</a>");

}

if(!$success){

?>

 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

 <html>

  <head>

   <title>Error</title>

  </head>

  <body>

   <h1>OAuth client error</h1>

   <pre>Error: <?php echo HtmlSpecialChars($client->error); ?></pre>

  </body>

 </html>

<?}?>