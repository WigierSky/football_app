// Pobierz element tabeli najlepszych strzelców
const topScorersTable = document.getElementById("top-scorers-table");
const topScorersBody = document.getElementById("top-scorers-body");

// Funkcja generująca zawartość tabeli najlepszych strzelców na podstawie danych z kontekstu
function generateTopScorers(data) {
    data.forEach((row) => {
        const newRow = document.createElement("tr");
        newRow.innerHTML = `
            <td class="highlight" data-player-id="${row.id}">
                <a href="#">${row.name}</a>
            </td>
            <td>${row.goals}</td>
            <td>${row.assists}</td>
        `;
        topScorersBody.appendChild(newRow);
    });


    const playerLinks = document.querySelectorAll(".highlight a");

    playerLinks.forEach((playerLink) => {
        playerLink.addEventListener("click", (event) => {
            event.preventDefault(); // Zapobiegamy domyślnemu działaniu linka

            const playerId = playerLink.parentElement.dataset.playerId.trim(); // Pobieramy ID zespołu
            const url = `/players/${playerId}/`; // Tworzymy odpowiedni URL
    
            // Przenosimy użytkownika do nowego URL
            window.location.href = url;
        });
    });
}

// Wywołanie funkcji generującej tabelę najlepszych strzelców
generateTopScorers(scoreData);
