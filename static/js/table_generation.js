// Pobierz element tabeli
const tableBody = document.getElementById("table-body");

// Funkcja generująca zawartość tabeli na podstawie danych z kontekstu
function generateTable(data) {
    data.forEach((row) => {
        const newRow = document.createElement("tr");
        newRow.innerHTML = `
            <td>${row.rank}</td>
            <td class="highlight" data-team-id="${row.id}">
                <a href="#">${row.name}</a>
            </td>
            <td>${row.played}</td>
            <td>${row.win}</td>
            <td>${row.draw}</td>
            <td>${row.lose}</td>
            <td>${row.gd}</td>
            <td class="highlight">${row.points}</td>
        `;
        tableBody.appendChild(newRow);
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


// Wywołanie funkcji generującej tabelę z danymi z kontekstu
generateTable(leagueData);
