document.addEventListener("DOMContentLoaded", function() {
    // Funkcja do aktualizacji tabeli
    function updateTable() {
        // Pobranie danych z pliku input.txt
        fetch('input.txt')
            .then(response => response.text())
            .then(data1 => {
                // Pobranie danych z pliku output.txt po pomyślnym pobraniu danych z input.txt
                return fetch('output.txt')
                    .then(response => response.text())
                    .then(data2 => {
                        // Wywołanie funkcji aktualizującej ciało tabeli na podstawie danych z plików
                        updateTableBody(data1.split('\n'), data2.split('\n'));
                    });
            })
            .catch(error => console.error('Error fetching data:', error));

        // Aktualizacja elementu z datą i godziną
        var datetimeElement = document.getElementById('datetime');
        var currentDate = new Date();
        var formattedDate = currentDate.toLocaleDateString();
        var formattedTime = currentDate.toLocaleTimeString();
        datetimeElement.textContent = 'Raport z dnia ' + formattedDate + ' godzina ' + formattedTime;
    }

    // Funkcja aktualizująca ciało tabeli na podstawie dostarczonych danych
    function updateTableBody(values1, values2) {
        var tableBody = document.getElementById('dataTable').getElementsByTagName('tbody')[0];
        tableBody.innerHTML = '';

        // Pętla iterująca przez dane i aktualizująca tabelę
        for (var i = 0; i < values1.length; i++) {
            var row = tableBody.insertRow(i);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);

            // Wstawienie danych do komórek tabeli
            cell1.textContent = values1[i];
            cell2.textContent = values2[i];
        }
    }

    // Wywołanie funkcji aktualizującej tabelę po załadowaniu zawartości strony
    updateTable();
});
