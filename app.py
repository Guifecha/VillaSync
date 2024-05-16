from flask import Flask, make_response, render_template, request, render_template_string

from persistence import anuncios
from persistence.anuncios import AnuncioDetalhes


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/anuncios', methods=['GET'])
def get_anuncios():
    all_anuncios = anuncios.list_all()
    return render_template('anuncios.html', all_anuncios=all_anuncios)



@app.route('/anuncios', methods=['POST'])
def criar_anuncio():
    novo = AnuncioDetalhes(**request.form)
    anuncios.create(novo)
    
    response = make_response(render_template_string(f"Anuncio {novo.titulo} criado com sucesso!"))
    response.headers['Location'] = '/anuncios'
    response.status_code = 303  
    return response

@app.route('/anuncios/<id>', methods=['GET'])
def get_anuncio(id):
    id, detalhes = anuncios.read(id)
    return render_template('anuncio.html', id=id, detalhes=detalhes)

@app.route('/anuncios/<id>', methods=['DELETE'])
def delete_anuncio(id):
    try:
        anuncios.delete(id)
        response = make_response(render_template_string(f"Anuncio {id} apagado com sucesso!"))
        response.headers['Location'] = '/anuncios'
        return response
    
    except Exception as e:
        r = make_response(render_template_string(f"Erro ao apagar anuncio"))
        return r



'''
@app.route('/propriedades')
def propriedades():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Propriedade;")
    propriedades = list(cursor)
    conn.close()
    return render_template('propriedades.html', propriedades=propriedades)

@app.route('/contratos')
def contratos():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contrato;")
    contratos = list(cursor)
    conn.close()
    return render_template('contratos.html', contratos=contratos)


@app.route('/clientes')
def clientes():
    return render_template('clientes.html')


@app.route('/agentes')  
def agentes():
    return render_template('agentes.html')

@app.route('/visitas')
def visitas():
    return render_template('visitas.html')

@app.route('/ofertas')
def ofertas():
    return render_template('ofertas.html')




@app.route('/test_connection', methods=['POST'])
def test_connection():
    # Get form data
    server_addr = "PORTATIL-GUI"  #request.form['connection_string']
    db_name = "VillaSync"        #request.form['database_name']
    #user = request.form['user']
    #password = request.form['password']

    try:
        with create_connection(server_addr, db_name) as conn:  #user, password
            message = "Connection successful!"
            colour = "green"
    except pypyodbc.Error as e:
        message = f"Connection failed: {str(e)}"
        colour = "red"

    return f'<label style="color: {colour};">{message}</label>'


@app.route('/hello', methods=['POST'])
def print_hello_table():
    # Get form data
    server_addr = "PORTATIL-GUI" #request.form['connection_string']
    db_name = "VillaSync" #request.form['database_name']
    #user = request.form['user']
    #password = request.form['password']

    # Fetch the hello table
    with create_connection(server_addr, db_name) as conn:   #user,pass
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Anuncio;")
        messages = list(cursor)

    return render_template_string("""
        <h1>Anuncio Table</h1>
        {% for x in messages %}
        <p>{{ x }}</p>
        {% endfor %}
        """, messages=messages)


def create_connection(server_addr, db_name):
    connection_string = f"DRIVER={{SQL Server}};SERVER={server_addr};DATABASE={db_name}"
    conn = pypyodbc.connect(connection_string)# user=user, password=password)
    return conn
'''

if __name__ == '__main__':
    app.run(debug=True)
