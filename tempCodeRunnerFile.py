from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "pranavpsv/gpt2-genre-story-generator"  # You can specify different versions like "gpt2-medium", "gpt2-large", or "gpt2-xl"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_story(prompt_text, length=150, temperature=0.7):
    input_ids = tokenizer.encode(prompt_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=length, num_return_sequences=1, no_repeat_ngram_size=2, temperature=temperature)
    story = tokenizer.decode(output[0], skip_special_tokens=True)
    return story.strip()

def main():
    while True:
        user_prompt = input('Enter a single line prompt (e.g., "A boy finds a magic wand"): ')
        if user_prompt.lower() in ['exit', 'quit']:
            break
        story = generate_story(user_prompt, length=500, temperature=0.7)  # Adjust length and temperature as needed
        print('\nGenerated Story:')
        print(story)
        print('-----------------\n')

if __name__ == '__main__':
    main()
