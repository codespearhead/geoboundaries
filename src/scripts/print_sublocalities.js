// https://jsfiddle.net/x7bzwfue/
// https://developers.google.com/maps/documentation/places/web-service/supported_types
// https://jsfiddle.net/gh/get/library/pure/googlemaps/js-samples/tree/master/dist/samples/places-queryprediction/jsfiddle
// https://developers.google.com/maps/documentation/geocoding/overview

function initService() {
  const myQuery = "Barbacena - State of Minas Gerais, Brazil";

  const service = new google.maps.places.AutocompleteService();
  const alpha = Array.from(Array(26)).map((e, i) => i + 65);
  let alphabet = alpha.map((x) => String.fromCharCode(x));
  //alphabet = ["R"]

  async function hello() {
    for (let letter of alphabet) {
      console.log(letter);
      const options = {
        input: myQuery + ", " + letter,
        types: ["sublocality"],
        componentRestrictions: {
          country: "br",
        },
      };
      await service.getPlacePredictions(options, displaySuggestions);
      await sleep(2000);
    }
    console.log("finish");
  }
  hello();

  async function displaySuggestions(predictions, status) {
    if (status != google.maps.places.PlacesServiceStatus.OK || !predictions) {
      return;
    }
    predictions.forEach((prediction) => {
      let item = prediction.description;
      if (item.includes(myQuery)) {
        item = item.replace(", " + myQuery, "");
        const li = document.createElement("li");
        li.appendChild(document.createTextNode(item));
        document.getElementById("results").appendChild(li);
      }
    });
  }

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}

window.initService = initService;