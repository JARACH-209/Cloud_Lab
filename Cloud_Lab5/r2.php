<!DOCTYPE html>
<html>
<head>
  <title>create_client</title>
  <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> 
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script> 
    <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  
</head>
<body>
  <center>
    <a href="r2.php" class="text-success">Registe</a><a class="ml-5" href="login.php">Customer Login</a><a class="ml-5" href="login2.php">Owner Login</a>
  </center>
<form action="r2.php" method="post"> 
<div class="site-section mt-5">
        <div class="container">


            <div class="row justify-content-center">
                <div class="col-md-5">
                    <div class="row">
                        <div class="col-md-12 form-group">
                            <label for="username" >Set Username</label>
                            <input type="text" name="name" id="first" class="form-control form-control-lg" autocomplete="off" autofocus/>
                        </div>
                        <div class="col-md-12 form-group">
                            <label for="pword">Set Password</label>
                            <input type="password" name="passd" id="second" class="form-control form-control-lg" autocomplete="off" >
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <input type="submit" value="Create" class="btn btn-primary btn-lg px-5">
                        </div>
                    </div>
                </div>
            </div>
  </form>
  <script type="text/javascript">
    $(document).ready(function(){
    $(':input').live('focus',function(){
        $(this).attr('autocomplete', 'off');
    });
  });
  </script>       
  <?php
  $name= filter_input(INPUT_POST, 'name');
  $pass= filter_input(INPUT_POST, 'passd');
  $conn = mysqli_connect("lab5.coddw0p8k4sn.us-east-2.rds.amazonaws.com", "boto3_user", "boto3_password", "aws");
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  } 
  else  
  {
      if (empty($name) && empty($pass)){
    }
    else{
          $sql = "INSERT INTO prime values ('$name','$pass')";
          if ($conn->query($sql))
          {
            echo "<center>New record is inserted sucessfully<center>";
            echo "<script>window.location.href='login.php'</script>";
            exit();
          }
          else
          {
            echo "Error: ". $sql ."". $conn->error;
        }
    }   
    $conn->close();
    }
  ?>
</body>
</html>