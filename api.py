from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = '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'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    user_text = request.form['user_text']
    target_language = request.form['target_language']
    
    # Call the OpenAI language model API to perform translation
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'Translate the following English text to {target_language}: "{user_text}"\nTranslate to: {target_language}\nTranslation:',
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    translated_text = response.choices[0].text.strip()
    
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
