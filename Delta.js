fetch(
  "https://euw1.api.riotgames.com/lol/status/v4/platform-data?api_key=RGAPI-RGAPI-edc04cdc-0a04-47bd-b103-2be0e4330234"
)
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  });

let Meter = 0;

const meterField = document.querySelector("[data-meter]");

const WalkButton = document.querySelector("#Walk");
WalkButton.addEventListener("click", WalkEvent);

function WalkEvent() {
  Meter += 1;
  meterField.innerHTML = Meter;
}
updateFields();
