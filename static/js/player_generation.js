function generatePlayerInfo(data) {
    const playerPhoto = document.getElementById("player-photo");

    playerPhoto.src = data["photo"]; // Przypisz URL logo klubu

    const playerName = document.getElementById("player-name");
    
    playerName.textContent = `Name: ${data["name"]}`;

    const playerAge = document.getElementById("player-age");
    playerAge.textContent = `Age: ${data["age"]}`;

    const playerClub = document.getElementById("player-club");
    playerClub.textContent = `Club: ${data["club"]}`; // Przypisz nazwę stadionu

}

// Wywołaj funkcję generującą informacje o klubie
generatePlayerInfo(playerData);