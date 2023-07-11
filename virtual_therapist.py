from flask import Flask, request, render_template, jsonify, redirect
import openai

app = Flask(__name__)
api_key = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global api_key

    if request.method == 'POST':
        api_key = request.form['api_key']
        if validate_api_key(api_key):
            return redirect('/virtual-therapist')
        else:
            return render_template('index.html', error_message='Invalid API key')

    return render_template('index.html')

@app.route('/virtual-therapist', methods=['GET', 'POST'])
def virtual_therapist():
    global api_key

    if api_key is None:
        return redirect('/')

    if request.method == 'POST':
        user_input = request.json['user_input']
        bot_response = generate_response(user_input)

        return jsonify({'bot_response': bot_response})

    return render_template('virtual-therapist.html')

def validate_api_key(api_key):
    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt='Test',
            max_tokens=5
        )
        return True
    except Exception as e:
        print(f"API key validation error: {str(e)}")
        return False

def generate_response(user_input):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens=100,
        temperature=0.8
    )
    bot_response = response.choices[0].text.strip()
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
