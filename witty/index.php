<?php
error_reporting(0);
function connect($data){
  $host = "127.0.0.1";
  $port = 2000;

  $output=$data;

  $socket1 = socket_create(AF_INET, SOCK_STREAM,0) or die("Could not create socket\n");

  socket_connect ($socket1 , $host,$port ) ;

  socket_write($socket1, $output, strlen ($output)) or die("Python Server is not runniing....\nPlease start pythonn server first...");

  socket_close($socket1);
  // echo '<script type="text/javascript">location.href = "inde.php";</script>';
}

function imgshow($path,$id){
    echo '<img src="'.$path.'" id="'.$id.'" height="220" width="360">';
}

function textshow($text,$id){
  // echo $text;
  
  echo  '<label for="textarea">'.($id-1).'.</label>';
  echo  '<textarea name="'.$id.'" rows="4" cols="50" class="edit">'.$text.'</textarea>';
}

function edit_box(){
      // Execute the python script with the JSON data
      $result = file_get_contents("data.json");
      //print($result);
     // Decode the result

    $resultData = json_decode($result, true);
    // This will contain: array('status' => 'Yes!')
    // var_dump($resultData);
    // imgshow($resultData[1][1],0);
    // echo $resultData[1][1];
      for($i=2;$i<sizeof($resultData);$i++){
        // echo $resultData[$i][1]+'<br>';
        if($resultData[$i][0]=='img'){
          imgshow($resultData[$i],$i);
        }
        else{
          textshow($resultData[$i],$i);
        }

      }
}
function transcript(){
  echo readfile("f1.txt");
}
?>

<?php
    $result = file_get_contents("data.json");
    $resultData = json_decode($result, true);
  if(isset($_POST['edit']))  
  {
    
    connect("sdf");
    // echo '<script language="javascript">';
    // // echo 'alert("Wait for 10 seconds....")';
    // echo '</script>';
      $result = file_get_contents("data.json");
      print($result);
     // Decode the result

    $resultData = json_decode($result, true);
    for($i=2;$i<sizeof($resultData);$i++){
        // echo $resultData[$i][1]+'<br>';
        if($resultData[$i]=='img'){
          // imgshow($resultData[$i][1],$i);
        }
        else{
          echo $resultData[$i]=$_POST[$i];
        }

      }
      echo $resultData;
      $fp = fopen('data.json', 'w');
      fwrite($fp, json_encode($resultData));
      fclose($fp);
      echo '<script type="text/javascript">location.href = "redirect.php";</script>';
}
 if(isset($_POST['url'])) {
      $url = $_POST["url"];
      $resultData =array("first",$url);
      // $resultData = $url;
      $fp = fopen('data.json', 'w');
      fwrite($fp, json_encode($resultData));
      fclose($fp);
      connect("123");
      echo '<script type="text/javascript">location.href = "redirect.php";</script>';
 }

?>

<!DOCTYPE html> 
<html> 
<head>
  <title>Videos</title>
    <!--Import Google Icon Font-->
      <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="materialize/css/materialize.min.css"  media="screen,projection"/>
   
      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="mdl/material.min.css">
  <script src="mdl/material.min.js"></script>
      <!--Import jQuery before materialize.js-->
    
</head>
<body> 
   <nav class="nav-extended">
    <div class="nav-wrapper">
      <a href="#" class="brand-logo" style="margin-left: 2em;margin-top: 10px;">Video<b>fy</b></a>
       <form method="POST">
        <input type="text" name="url" placeholder="Link" style="background-color: white;color: black;margin-top: 20px;margin-left: 12em;width: 25em;font-size: 1.5em;padding-left: 10px;border-radius: 5px">
        <a href="#" class="brand-logo" style="margin-left: 3em;margin-top: 10px;font-size: 1.5em">Made for <b>#Wittyhacks </b></a>
        <img src="https://cdn.wittyfeed.com/assets_main_new/images/wittyfeed_new_update.svg" class="logo_new" alt="wittyfeed-beyond-stories" style="margin-left: 26.5em;width: 100px">
      </form>
    </div>
  </nav>

<div style="background-color: #eeeeee ;
          margin-left:0;margin:2.5em;
          float: left;width: 60%;
          padding: 5px;
          margin-bottom: 20px;
          box-shadow: 1px 2px 20px grey"> 
  
  <video id="video1" width="770" height="405" controls >
    <source src="test.mp4" type="video/mp4">
    <source src="test.ogg" type="video/ogg">
  </video>
</div>



  <form action="" method="POST"> 
    <div style="background-color: #f0f0f0;
                margin-top:2.5em;
                margin-right: 2.5em;
                width: 31%;   
                float: right;
                 box-shadow: 1px 2px 20px grey;
                height: 525px">

      <div style="margin-left: 9em;
                  font-size: 1.2em;
                  font-style: bold
                  padding-top:2em">
         <p ><b>Frame No.</b></p>
      </div>

      <div style="
                float: right;
                overflow-y: auto;
                padding: 1.5em;
                height: 490px;">
        <?php edit_box();?>
      </div>

      <div>
         <!-- <button id="edit"  name="edit"></button> -->
         <button class="waves-effect waves-light btn" id="edit" name="edit" type="submit" style="width: 100%"><i class="material-icons right"></i>Edit video</button>
      </div>
    </div>
    
  </form>
<u><a href="<?php echo $resultData[1]; ?>" style="
                                          font-size: 1.5em;
                                          margin-left: 1.5em;
                                          color: grey;
                                          margin-bottom:1em;"><?php echo $resultData[2]; ?></a></u>

<div style="background-color: #eeeeee ;
          margin-left:0;margin:2.5em;
          margin-top: 20px;
          float: left;width: 60%;
          padding: 5px;
          box-shadow: 1px 2px 20px grey"> 

          <a class="waves-effect waves-light btn" href="test.mp4"><i class="material-icons right">file_download</i>Download</a>
          <a class="waves-effect waves-light btn" style="background-color: #3b5998"><i class="material-icons right">share</i>facebook</a>


      <ul class="collection with-header" style="margin: 0;margin-top: 5px">
        <li class="collection-header"><h5 style="margin:0">Transcript</h5></li>
        <li class="collection-item"><?php transcript();?></li>
      </ul>
</div>



</body> 
</html>

<script> 
var myVideo = document.getElementById("video1"); 

function playPause() { 
    if (myVideo.paused) 
        myVideo.play(); 
    else 
        myVideo.pause(); 
} 

function makeBig() { 
    myVideo.width = 560; 
} 

function makeSmall() { 
    myVideo.width = 320; 
} 

function makeNormal() { 
    myVideo.width = 420; 
} 

</script> 
<style type="text/css">
  .edit{
      background-color: #fafafa;
      height: 5em;
      margin-bottom: .5em;
      border: 1px solid #616161;
      border-radius: 0;
      outline: none;
      height: 5rem;
      width: 100%;
      font-size: 1rem;
      color: grey;
      margin: 0 0 20px 0;
      box-shadow: 1px 2px 10px grey;
  }
</style>