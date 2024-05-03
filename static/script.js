const timeElement = document.getElementById("clock");

function updateTime() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    const clockStr = `${hours}:${minutes}:${seconds}`;

    timeElement.innerText = clockStr;
}

updateTime();
setInterval(updateTime, 1000);

console.log('hello from script.js')
