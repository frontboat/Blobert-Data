import json
from collections import defaultdict
import heapq

def find_top_rare_traits(data):
    # Initialize a dictionary to count occurrences of each trait variation
    trait_occurrences = defaultdict(lambda: defaultdict(int))

    # Count occurrences of each trait variation
    for nft in data:
        traits = nft.get('traits', {}).get('variant', {}).get('Regular', {})
        for trait, variation in traits.items():
            trait_occurrences[trait][variation] += 1

    # Find the top 5 most rare variations for each trait
    top_rare_variations = {}
    for trait, variations in trait_occurrences.items():
        # Use nlargest to find the least occurring variations; since we want the rarest (least counts)
        rare_variations = heapq.nsmallest(5, variations.items(), key=lambda x: x[1])
        top_rare_variations[trait] = rare_variations

    return top_rare_variations

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    file_path = '/Users/boat/Projects/Blobert Data/traitsResults.json'  # Update this path to your JSON file location
    data = load_data(file_path)
    
    top_rare_traits = find_top_rare_traits(data)
    for trait, variations in top_rare_traits.items():
        print(f"Trait: {trait}")
        for variation, count in variations:
            print(f"  Variation: {variation}, Occurrences: {count}")
        print()

if __name__ == '__main__':
    main()
