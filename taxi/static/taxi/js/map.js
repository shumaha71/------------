const apiKey = '8cad1a746a524b4b9a51b272067ec8cc';
const mapMessage = document.getElementById('map-message');

if (typeof L === "undefined") {
    mapMessage.textContent =
        "Не удалось загрузить библиотеку карты. Проверьте Интернет.";
} else {
    const map = L.map("map");

    map.setView([55.751244, 37.618423], 12);
    const tilesUrl =
        "https://maps.geoapify.com/v1/tile/osm-carto/{z}/{x}/{y}.png"
        + "?apiKey=" + encodeURIComponent(apiKey);
    const tiles = L.tileLayer(tilesUrl, {
        maxZoom: 20,
        attribution:
            'Powered by <a href="https://www.geoapify.com/">Geoapify</a>'
            + ' | © <a href="https://www.openstreetmap.org/copyright">'
            + 'OpenStreetMap</a> contributors'
    });
    tiles.on("tileerror", function () {
        mapMessage.textContent =
            "Не удалось загрузить часть карты. Проверьте ключ, Интернет и лимит Geoapify.";
    });
    tiles.addTo(map);
}
const routeForm = document.getElementById("route-form");
const pickupInput = document.getElementById("pickup-address");
const destinationInput = document.getElementById("destination-address");
const routeMessage = document.getElementById("route-message");

routeForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const pickupAddress = pickupInput.value.trim();
    const destinationAddress = destinationInput.value.trim();

    if (!pickupAddress || !destinationAddress) {
        routeMessage.textContent = "Введите оба адреса.";
        return;
    }

    routeMessage.textContent =
        "Откуда: " + pickupAddress + ". Куда: " + destinationAddress + ".";
});