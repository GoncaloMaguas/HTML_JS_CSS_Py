from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para exibir mensagens flash


def check_login(username, password):
    conn = sqlite3.connect('bd_users.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM utilizadores WHERE nome_utilizador = ? AND pw_utilizador = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None


def check_unique_username(username):
    conn = sqlite3.connect('bd_users.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM utilizadores WHERE nome_utilizador = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user is None


def check_unique_email(email):
    conn = sqlite3.connect('bd_users.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM utilizadores WHERE email_utilizador = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user is None


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if check_login(username, password):
            # Redireciona para o Google em caso de login bem-sucedido
            return redirect("https://www.google.pt")
        else:
            flash('Certifique-se de que inseriu corretamente os seus dados.', 'error')

    return render_template('Login.html')


@app.route('/registar', methods=['GET', 'POST'])
def registar():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        if not check_unique_username(username):
            flash('Nome de utilizador já existe!', 'error')
        elif not check_unique_email(email):
            flash('Endereço de e-mail já existe!', 'error')
        else:
            conn = sqlite3.connect('bd_users.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO utilizadores (nome_utilizador, email_utilizador, pw_utilizador) VALUES (?, ?, ?)",
                           (username, email, password))

            conn.commit()
            conn.close()

            flash('Registro bem-sucedido! Faça login.', 'success')
            return redirect(url_for('login'))

    return render_template('Registar.html')


@app.route('/login')
def login_page():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
