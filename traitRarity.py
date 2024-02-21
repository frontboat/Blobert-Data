import json

def find_most_rare_trait(data):
    # Initialize a dictionary to count occurrences of each trait and its variations
    trait_occurrences = {}

    # Iterate through each NFT's traits to count occurrences
    for nft in data:
        traits = nft.get('traits', {}).get('variant', {}).get('Regular', {})
        for trait, variation in traits.items():
            if trait not in trait_occurrences:
                trait_occurrences[trait] = {}
            if variation not in trait_occurrences[trait]:
                trait_occurrences[trait][variation] = 0
            trait_occurrences[trait][variation] += 1

    # Initialize variables to track the most rare trait and its occurrence count
    most_rare_trait = None
    min_occurrence = float('inf')

    # Iterate through the trait occurrences to find the most rare trait
    for trait, variations in trait_occurrences.items():
        for variation, count in variations.items():
            if count < min_occurrence:
                min_occurrence = count
                most_rare_trait = (trait, variation)

    return most_rare_trait, min_occurrence

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    file_path = '/Users/boat/Projects/Blobert Data/traitsResults.json'  # Update this path to your JSON file location
    data = load_data(file_path)
    
    most_rare_trait, occurrence = find_most_rare_trait(data)
    print(f'The most rare trait is "{most_rare_trait[0]}" with variation "{most_rare_trait[1]}" occurring {occurrence} times.')

if __name__ == '__main__':
    main()
