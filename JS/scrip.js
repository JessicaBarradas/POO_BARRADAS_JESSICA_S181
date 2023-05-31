const table = document.getElementById("table");
const modal = document.getElementById("modal");
const inputs = document.querySelectorAll("input");
let count = 0;

window.addEventListener("click", (e) => {
  if (e.target.matches(".btn-warning")) {
    let data = e.target.parentElement.parentElement.children;
    fillData(data);
    modal.classList.toggle("translate");
  }

  if (e.target.matches(".btn-danger")) {
  modal.classList.toggle("translate");
  count=0
  }
});

const fillData = (data) => {
  for (let index of inputs) {
    index.value = data[count].textContent;
    console.log(index);
    count += 1;
  }
};
const $tiempo = document.querySelector('.tiempo'),
$fecha = document.querySelector('.fecha');

function digitalClock(){
    let f = new Date(),
    dia = f.getDate(),
    mes = f.getMonth() + 1,
    anio = f.getFullYear(),
    diaSemana = f.getDay();

    dia = ('0' + dia).slice(-2);
    mes = ('0' + mes).slice(-2)

    let timeString = f.toLocaleTimeString();
    $tiempo.innerHTML = timeString;

    let semana = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
    let showSemana = (semana[diaSemana]);
    $fecha.innerHTML = `${anio}-${mes}-${dia} ${showSemana}`
}
setInterval(() => {
    digitalClock()
}, 1000);