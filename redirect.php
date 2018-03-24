<!DOCTYPE html>
<html>
<style>
#div1 {
  font-size:40px;
  text-align: center;
  margin-left: 49%;
  margin-top: 20px;
}
#div2 {
  font-size:30px;
  text-align: center;
  margin-left: 48%;
  margin-top: 100px;
}
.logo{
  margin-top: 3em;
  height: 250px;
  width: 460px;
}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

<body>

<center><img src="assets/logo.png" class="logo" ></center>
<div id="div1" class="fa"></div>
<!-- <p id="div2">Wait for few seconds..<br></p> -->
<center><p>Wait for few seconds.</p></center>
<center><p>We are working on it.</p></center>
<!-- <p id='123'>hekk</p> -->
<script>
function hourglass() {
  var a;
  a = document.getElementById("div1");
  a.innerHTML = "&#xf251;";
  setTimeout(function () {
      a.innerHTML = "&#xf252;";
    }, 1000);
  setTimeout(function () {
      a.innerHTML = "&#xf253;";
    }, 2000);
}
hourglass();
setInterval(hourglass, 1500);

function status() {
  var xhttp;
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // document.getElementById("123").innerHTML = this.responseText;
      if(this.responseText=='1'){
        location = 'index.php';
      }
    }
  };
  xhttp.open("GET", "assets/con.txt", true);
  xhttp.send();   
}
setInterval(status,1000);

</script>

</body>
</html>
