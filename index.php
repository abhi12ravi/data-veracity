<?php
session_start(); 
?>
<!doctype html>
<html xmlns:fb="http://www.facebook.com/2008/fbml">
  <head>
    <meta charset="utf-8">
<link href='http://fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>
    <link href="http://fontawesome.io/assets/font-awesome/css/font-awesome.css" rel="stylesheet" media="screen">  
    <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>

    
       <style type="text/css">
    .login-form {
  text-align: center;
  width: 80%;
  margin: 60px auto 0;
}

input[type=email], input[type=password] {
  display: block;
  width: 100%;
  margin: 0 auto;
  outline: none;
  padding-top: 24px;
  padding-bottom: 24px;
}

.login-button {
  width: 100%;
  margin: 0 auto;
}

.forgot-password {
  display: block;
  margin: 8px auto 0 auto;
  font-size: 14px;
}
html {
    font-size: 200px;
}
.unbehaved-element {
    font-size: 2em;
}
@media(max-width: 1580px) {
  html {
    font-size: 18px;
  }
  .unbehaved-element {
    font-size: 1.9em; /* Fine tune unbehaved elements */
  }
}
@media(max-width: 980px) {
  html {
    font-size: 16px;
  }
}
.img-center {
    margin: 0 auto;
}


    </style>
     <link href="css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
     </head>
    <body style="background-image: url('back1.jpg');
    background-repeat: none;
    height: 100%;
    width: 100%">
    <ons-page>
      

      <div class="login-form">
        <br>
        
<h1 align="center" style="font-size: 80px;color: #009966;font-family: 'Oswald', sans-serif;">H.O.P.E</h1>

        <br>


               <a href="fbconfig.php"><img class="img-responsive img-center" src="loginfb.png"></a>
                <br><br>
        
      </div>

    </ons-page>
    <?php if ($_SESSION['FBID']): ?>      <!--  After user login  -->

    <?php endif ?>
<p style="font-size:10px;" align="center">&copy H.O.P.E</p>

  </body>
</head>

</html>