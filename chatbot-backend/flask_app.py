# -*- coding: utf-8 -*-
"""Flask_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pFIIy4KNzBdfVxxqPpCxlWYDo8EXzlLy
"""

import warnings
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask_cors import CORS
import torch

# Suppress warnings
warnings.filterwarnings("ignore", category=FutureWarning)

app = Flask(__name__)
CORS(app)

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained("fine_tuned_model")
tokenizer = AutoTokenizer.from_pretrained("fine_tuned_model")
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON input
        data = request.get_json(force=True)
        user_input = data.get('text', '')

        # Validate input
        if not user_input or not isinstance(user_input, str):
            return jsonify({'error': 'Invalid input. Text input required.'}), 400

        # Tokenize input
        inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True)
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']

        # Generate response with more focused parameters
        with torch.no_grad():
          outputs = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,  # explicitly pass the attention mask
                max_length=60,  # limit response length
                do_sample=True,  # enable sampling
                temperature=0.6,  # reduce temperature for less randomness
                top_k=50,  # top-k sampling to limit candidate tokens
                top_p=0.85,  # reduce top-p sampling threshold
                no_repeat_ngram_size=2,  # prevent repetitive phrases
                pad_token_id=tokenizer.eos_token_id
            )

        # Decode and clean response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # If response is too verbose, trim it to make it more relevant
        if len(response.split()) > 50:
            response = " ".join(response.split()[:50])

        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)