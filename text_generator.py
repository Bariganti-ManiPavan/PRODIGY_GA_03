import random
from collections import defaultdict

def build_markov_chain(text, state_size=1):
    words = text.split()
    markov_chain = defaultdict(list)
    for i in range(len(words) - state_size):
        state = tuple(words[i : i + state_size])
        next_word = words[i + state_size]
        markov_chain[state].append(next_word)
    return markov_chain

def generate_text(chain, state_size=1, max_words=30):
    if not chain:
        return "Chain is empty."
    current_state = random.choice(list(chain.keys()))
    output = list(current_state)
    for _ in range(max_words - state_size):
        if current_state in chain:
            next_word = random.choice(chain[current_state])
            output.append(next_word)
            current_state = tuple(output[-state_size:])
        else:
            current_state = random.choice(list(chain.keys()))
            output.extend(list(current_state))
    return " ".join(output)

if __name__ == "__main__":
    # Training text for Generative AI model
    sample_text = """
    The quick brown fox jumps over the lazy dog. The lazy dog slept all day, 
    but the quick brown fox was full of energy. A quick brown fox is hard to catch, 
    especially when the lazy dog is fast asleep.
    """
    
    # Using state_size=1 (First-order Markov Chain)
    chain_model = build_markov_chain(sample_text, state_size=1)
    generated_story = generate_text(chain_model, state_size=1, max_words=20)
    
    print("\n--- Generated Text ---")
    print(generated_story, "\n")