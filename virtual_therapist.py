from flask import Flask, request, render_template, redirect
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
        user_input = request.form['user_input']

        # Use the OpenAI GPT-3 model to generate a response
        bot_response = generate_response(user_input)

        return render_template('virtual-therapist.html', user_input=user_input, bot_response=bot_response)

    return render_template('virtual-therapist.html')

def validate_api_key(api_key):
    openai.api_key = api_key

    # Test API call to validate the OpenAI API key
    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt='Test',
            max_tokens=5
        )
        # If the API call succeeds without raising an exception, the API key is considered valid
        return True
    except Exception as e:
        # If the API call fails, the API key is considered invalid
        print(f"API key validation error: {str(e)}")
        return False


def generate_response(user_input):
    # Add your OpenAI API code here to generate the response based on the user input
    # Replace the placeholder code below with your actual implementation
    response = "Response from virtual therapist"
    return response

if __name__ == '__main__':
    app.run(debug=True)
