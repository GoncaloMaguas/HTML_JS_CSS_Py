function validarLogin() {
    var username = document.getElementById("username-login").value;
    var password = document.getElementById("password-login").value;


    fetch('utilizadores.json')
        .then(response => response.json())
        .then(data => {

            var user = data.utilizadores.find(u => u.UserName === username);
            if (user && user.Password === password) {
                window.location.href = 'Editavel.html';
                alert("Correto");
            } else {
                window.location.href = 'NaoEditavel.html';
                alert("Incorreto");
            }
        })
        .catch(error => console.error('Erro ao carregar o arquivo JSON:', error));


    return false;
}
