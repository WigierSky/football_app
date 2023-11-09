function generateClubInfo(data) {
    const clubLogo = document.getElementById("club-logo");

    clubLogo.src = data["logo"]; // Przypisz URL logo klubu

    const clubName = document.getElementById("club-name");
    clubName.textContent = `Club Name: ${data["name"]}`; // Przypisz nazwę klubu
    
    const clubCountry = document.getElementById("club-country");
    clubCountry.textContent = `Country: ${data["country"]}`; // Przypisz kraj

    const clubFoundationYear = document.getElementById("club-foundation-year");
    clubFoundationYear.textContent = `Foundation Year: ${data["year"]}`; // Przypisz rok założenia

    const clubStadium = document.getElementById("club-stadium");
    clubStadium.textContent = `Stadium: ${data["stadium"]}`; // Przypisz nazwę stadionu

    const clubStadiumCapacity = document.getElementById("club-stadium-capacity");
    clubStadiumCapacity.textContent = `Stadium Capacity: ${data["capacity"]}`; // Przypisz pojemność stadionu

}

// Wywołaj funkcję generującą informacje o klubie
generateClubInfo(teamData);