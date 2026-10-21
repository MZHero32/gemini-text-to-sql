from flask import Flask, render_template, request
from text_to_sql import generate_query, execute_query

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16384

@app.route('/', methods=['GET', 'POST'])
def home():
    question = request.form.get('question', '')
    query = request.form.get('query', '')
    columns, rows, error = [], [], None
    if request.method == 'POST':
        try:
            if request.form.get('action') == 'execute':
                columns, rows = execute_query(query)
            else:
                query = generate_query(question)
        except ValueError as exc:
            error = str(exc)
        except Exception:
            app.logger.exception('Query request failed')
            error = 'The request failed. Check local settings and server logs.'
    return render_template('index.html', question=question, query=query, columns=columns, rows=rows, error=error)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=False)
