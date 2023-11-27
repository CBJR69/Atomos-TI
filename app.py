from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['name']
    email = request.form['email']
    assunto = request.form['subject']
    mensagem = request.form['message']

    # Configurações do servidor de e-mail
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('seu_email@example.com', 'sua_senha')

    # Construa a mensagem de e-mail
    corpo_email = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
    mensagem_email = f'Subject: Formulário de Contato\n\n{corpo_email}'

    # Substitua os detalhes do remetente e destinatário
    remetente = 'seu_email@example.com'
    destinatario = 'destinatario@example.com'

    # Envie o e-mail
    server.sendmail(remetente, destinatario, mensagem_email)

    # Encerre a conexão com o servidor de e-mail
    server.quit()

    return 'E-mail enviado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
