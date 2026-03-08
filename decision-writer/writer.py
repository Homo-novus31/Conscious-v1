def generate_decision(prompt):
  inputs = tokeniser(prompt, return_tensors = 'pt').to(model.device)

  with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens = 800,
        temperature = 0.5,
        do_sample = False
    )
    generated_tokens = output[0][inputs["input_ids"].shape[-1]:]
    text = tokeniser.decode(generated_tokens, skip_special_tokens=True)

  return text

def writer(decision_spec):

    prompt = f"""
You are a sharp, analytical and very experienced AI newsletter writer who does very well in tapping into the curiosity of people, explaining very complex terms in simple words
Write a professional AI safety newsletter article.

Decision specification:
{decision_spec}

Start the article below.

Headline:
"""



    return generate_decision(prompt)