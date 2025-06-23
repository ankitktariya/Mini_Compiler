from flask import Flask, request, jsonify
from flask_cors import CORS
from core.math_evaluator import evaluate
from core.markdowna_parser import convert_markdown_to_html
from core.sql_executor import query_executor

app = Flask(__name__)
CORS(app)  # ✅ Important: Allow connection from React

@app.route('/compile', methods=['POST'])
def compile_code():
    data = request.json
    mode = data.get('mode')
    code = data.get('input')

    try:
        if mode == 'math':
            result = evaluate(code)
        elif mode == 'markdown':
            result = convert_markdown_to_html(code)
        elif mode == 'sql':
            result = query_executor(code)
        else:
            result = 'Invalid mode'
        return jsonify({'output': str(result)})
    except Exception as e:
        return jsonify({'output': '❌ Error: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
