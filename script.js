
//GAUGE
const gaugeElement = document.querySelector(".gauge");

function setGaugeValue(gauge, value) {
  if (value < 0 || value > 1) {
    return;
  }

  gauge.querySelector(".gauge__fill").style.transform = `rotate(${
    value / 2
  }turn)`;
  gauge.querySelector(".gauge__cover").textContent = `${Math.round(
    value * 100
  )}%`;
}

setGaugeValue(gaugeElement, 0.75);



//CHART
getData();

async function getData() {
  const response = await fetch('globalTemp.csv');
  const data = await response.text();

  const rows = data.split('\n').slice(1);
  rows.forEach(ele => {
      const row = ele.split(',');
      const year = row[0];
      const temp = row[1];
      console.log(year);
      console.log(temp);
  });
}
