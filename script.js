

//===========GAUGES=================================================================

const gaugeBattery = document.querySelector('.battery');
const gaugePressure = document.querySelector('.pressure');
const gaugeTemperature = document.querySelector('.temperature');

function setGaugeValueB(gauge,value) {
  if(value<0||value>1) {
    return;
  }
  gauge.querySelector(".battery__fill").style.transform = `rotate(${value/2}turn)`;
  gauge.querySelector(".battery__cover").textContent = `${Math.round(value*100)}%`;
}

function setGaugeValueP(gauge,value) {
  if(value<0||value>1) {
    return;
  }
  gauge.querySelector(".pressure__fill").style.transform = `rotate(${value/2}turn)`;
  gauge.querySelector(".pressure__cover").textContent = `${Math.round(value*100)}Pa`;
}

function setGaugeValueT(gauge,value) {
  if(value<0||value>1) {
    return;
  }
  gauge.querySelector(".temp__fill").style.transform = `rotate(${value/2}turn)`;
  gauge.querySelector(".temp__cover").textContent = `${Math.round(value*100)}°C`;
}



