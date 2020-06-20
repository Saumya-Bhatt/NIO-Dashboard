
//======= GETTING DATE AND TIME =======

function time(){
    var date = new Date();    
    var time = date.toLocaleTimeString();
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    var day = date.toLocaleDateString('en-US',options);
    document.getElementById('time').innerHTML = time;
    document.getElementById('day').innerHTML = day;
    }
    setInterval(function(){
    time();
    },1000);


