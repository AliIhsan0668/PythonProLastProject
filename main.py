# İçe Aktarma
from flask import Flask, render_template, request


app = Flask(__name__)


# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')

# İkinci sayfa
@app.route('/etki')
def etki():
    return render_template('etki.html')

# Üçüncü sayfa
@app.route('/neden')
def neden():
    return render_template('neden.html')

# Hesaplama
@app.route('/nedir')
def end():
    return render_template('tanim.html')


# Form
@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları
@app.route('/submit', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    name = request.form['name']
    text = request.form['text']
    email = request.form['email']

    with open('static\kayıt.txt', 'a',) as f:
        f.write(name + '\n',)
        f.write(text + '\n',)
        f.write(email + '\n\n',)


    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    return render_template('form_result.html', 
                           # Değişkenleri buraya yerleştirin
                           name=name,
                           email=email,
                           text=text,
                           )
  
app.run(debug=True)