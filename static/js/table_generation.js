// Pobierz element tabeli
const tableBody = document.getElementById("table-body");

// Funkcja generująca zawartość tabeli na podstawie danych z kontekstu
function generateTable(data) {
    data.forEach((row) => {
        const newRow = document.createElement("tr");
        newRow.innerHTML = `
            <td>${row.rank}</td>
            <td>${row.name}</td>
            <td>${row.played}</td>
            <td>${row.win}</td>
            <td>${row.draw}</td>
            <td>${row.lose}</td>
            <td>${row.points}</td>
        `;
        tableBody.appendChild(newRow);
    });
}

// Wywołanie funkcji generującej tabelę z danymi z kontekstu
generateTable(leagueData);
