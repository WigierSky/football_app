var matchesList = document.getElementById("matches-container");

// Funkcja generująca zawartość listy meczów na podstawie danych z kontekstu
function generateMatches(data) {
    data.forEach((match) => {
        const matchElement = document.createElement("div");
        matchElement.classList.add("match");
        matchElement.innerHTML = `
            <span class="highlight" data-team-id="${match.home_team_id}">
                <a href="#">${match.home_team}</a>
            </span>
            - 
            <span class="highlight" data-team-id="${match.away_team_id}">
                <a href="#">${match.away_team}</a>
            </span>
            ${match.home_goals}:${match.away_goals}`;
        matchesList.appendChild(matchElement);
    });

    const teamLinks = document.querySelectorAll(".highlight a");

    teamLinks.forEach((teamLink) => {
        teamLink.addEventListener("click", (event) => {
            event.preventDefault(); // Zapobiegamy domyślnemu działaniu linka

            const teamId = teamLink.parentElement.dataset.teamId; // Pobieramy ID zespołu
            const url = `/teams/${teamId}/`; // Tworzymy odpowiedni URL

            // Przenosimy użytkownika do nowego URL
            window.location.href = url;
        });
    });
}

// Wywołanie funkcji generującej listę meczów
generateMatches(fixturesData);