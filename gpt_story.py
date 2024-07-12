from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch 
import re
model_name = "pranavpsv/gpt2-genre-story-generator"  # You can specify different versions like "gpt2-medium", "gpt2-large", or "gpt2-xl"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
def clean_text(text):
    # Remove timestamps and other patterns like [HH:MM:SS]
    cleaned_text = re.sub(r'\[\d{2}:\d{2}:\d{2}\]', '', text)
    # Remove other potential unwanted characters or patterns
    cleaned_text = re.sub(r'\* BOS has left #holidaybullshit', '', cleaned_text)
    # Remove extra spaces that may result from cleaning
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text
# def generate_story(prompt_text, length=150, temperature=0.7):
#     input_ids = tokenizer.encode(prompt_text, return_tensors="pt")
#     output = model.generate(input_ids, max_length=length, num_return_sequences=1, no_repeat_ngram_size=2, temperature=temperature)
#     story = tokenizer.decode(output[0], skip_special_tokens=True)
#     return story.strip()
# def generate_story(prompt_text, length=500, temperature=0.7, do_sample=True):
#     model_name = 'gpt2'
#     tokenizer = GPT2Tokenizer.from_pretrained(model_name)
#     model = GPT2LMHeadModel.from_pretrained(model_name)

#     input_ids = tokenizer.encode(prompt_text, return_tensors='pt')
#     attention_mask = tokenizer.encode(prompt_text, return_tensors='pt')

#     output = model.generate(
#         input_ids=input_ids,
#         max_length=length,
#         temperature=temperature,
#         do_sample=do_sample,
#         pad_token_id=tokenizer.eos_token_id,
#         attention_mask=attention_mask
#     )

#     story = tokenizer.decode(output[0], skip_special_tokens=True)
#     return story
def generate_story(prompt_text, length=500, temperature=0.7, do_sample=True):
    try:
        model_name = 'gpt2'
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        model = GPT2LMHeadModel.from_pretrained(model_name)

        if not prompt_text:
            raise ValueError("Prompt text is empty")

        input_ids = tokenizer.encode(prompt_text, return_tensors='pt')
        if len(input_ids[0]) == 0:
            raise ValueError("Input IDs are empty")

        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

        print(f"Input IDs: {input_ids}")
        print(f"Attention Mask: {attention_mask}")

        output = model.generate(
            input_ids=input_ids,
            max_length=length,
            temperature=temperature,
            do_sample=do_sample,
            pad_token_id=tokenizer.eos_token_id,
            attention_mask=attention_mask
        )

        if len(output) == 0:
            raise ValueError("Model output is empty")

        story = tokenizer.decode(output[0], skip_special_tokens=True)
        return story
    except Exception as e:
        print(f"Error generating story: {str(e)}")
        raise e


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
