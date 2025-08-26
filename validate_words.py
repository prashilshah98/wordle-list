import requests
import time

def validate_words(input_filepath, output_filepath, delay=0.5):
    
    with open(input_filepath, 'r') as infile:
        words = [line.strip() for line in infile if line.strip()]
        
    valid = []
    invalid = []

    for idx, word in enumerate(words, 1):
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            # Confirm it has valid definitions
            if isinstance(data, list) and data and data[0].get("meanings"):
                valid.append(word)
            else:
                invalid.append(word)
        else:
            invalid.append(word)
        
        if idx % 20 == 0:
            print(f"Checked {idx}/{len(words)} words...")

        time.sleep(delay)  # Delay to avoid rate limiting
    
    # Save results
    with open(output_filepath, 'w') as outfile:
        outfile.write("\n".join(valid))

    print(f"\nValidation complete!")
    print(f"Total words checked: {len(words)}")
    print(f"Valid words: {len(valid)}")
    print(f"Invalid words: {len(invalid)}")
    if invalid:
        print("Here are some invalid words:", invalid[:10])

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Validate words using dictionaryapi.dev")
    parser.add_argument("input_file", help="Path to input file (one word per line)")
    parser.add_argument("output_file", help="Path to write valid words")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between API calls (seconds)")
    args = parser.parse_args()

    validate_words(args.input_file, args.output_file, delay=args.delay)
