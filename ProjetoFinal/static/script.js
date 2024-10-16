// script.js

function registrarUsuario() {
    var email = document.getElementById("email").value;
    var username = document.getElementById("username-registar").value;
    var password = document.getElementById("password-registar").value;

    fetch('/registar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            username: username,
            password: password
        })
    })
        .then(response => {
            if (response.ok) {
                window.location.href = 'Login.html';
            } else {
                window.location.href = 'Erro.html';
            }
        })
        .catch(error => console.error('Erro ao registar:', error));

    return false; // Impede o envio do formulário tradicional
}
