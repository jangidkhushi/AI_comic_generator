from flask import Flask, request, jsonify, render_template
from gpt_story import generate_story
from kartoon import generate_comic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story_route():
    data = request.json
    prompt_text = data['prompt_text']
    try:
        story = generate_story(prompt_text)
        return jsonify({'success': True, 'story': story})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/generate_comic', methods=['POST'])
def generate_comic_route():
    data = request.json
    scenario = data['scenario']
    prompts = data['prompts']
    style = data['style']
    try:
        comic_strip_path = generate_comic(prompts, style)
        return jsonify({'success': True, 'comic_strip_path': comic_strip_path})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
