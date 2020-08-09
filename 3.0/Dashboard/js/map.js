function global2local(pos) {
  var offset_x = ((pos[0] - 73.801957)*12658.227848182)+305;
  var offset_y = ((pos[1] - 15.456659)*(-14529.37460517901))+143;
  return [~~(offset_x),~~(offset_y)];
}

var places = {  "home" : [73.801957, 15.456659], 
                "boat" : [73.796335, 15.454740], 
                "c-bot" : [73.798335, 15.452740] 
};

window.onload = function() {
  var canvas = document.getElementById("myCanvas");
  var ctx = canvas.getContext("2d");
  var img = document.getElementById("scream");
  ctx.drawImage(img, 0, 0);

  home = global2local(places['home'])
  ctx.beginPath();
  ctx.arc(home[0],home[1], 3, 0, 2*Math.PI); //450 x 300
  ctx.fillStyle = "chartreuse";
  ctx.fill();

  boat = global2local(places['boat'])
  ctx.beginPath();
  ctx.arc(boat[0],boat[1], 3, 0, 2*Math.PI);
  ctx.fillStyle = "blue";
  ctx.fill();

  c_bot = global2local(places['c-bot'])
  ctx.beginPath();
  ctx.arc(c_bot[0],c_bot[1], 3, 0, 2*Math.PI);
  ctx.fillStyle = "red";
  ctx.fill();
};