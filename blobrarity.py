import json

def calculate_rarity_scores(data):
    # Calculate the count of each trait variation
    traits_count = {}
    for nft in data:
        traits = nft.get('traits', {}).get('variant', {}).get('Regular', {})
        for trait, value in traits.items():
            if trait not in traits_count:
                traits_count[trait] = {}
            if value not in traits_count[trait]:
                traits_count[trait][value] = 0
            traits_count[trait][value] += 1

    # Invert the counts to get rarity scores (lower count = higher rarity)
    traits_rarity_scores = {}
    for trait, variations in traits_count.items():
        max_count = max(variations.values())  # Find the highest count to normalize rarity scores
        traits_rarity_scores[trait] = {variation: max_count / count for variation, count in variations.items()}

    # Calculate combined rarity score for each TokenID
    token_rarity_scores = {}
    for nft in data:
        token_id = nft['tokenId']
        traits = nft.get('traits', {}).get('variant', {}).get('Regular', {})
        combined_rarity_score = 1
        for trait, value in traits.items():
            if trait in traits_rarity_scores and value in traits_rarity_scores[trait]:
                combined_rarity_score *= traits_rarity_scores[trait][value]
        token_rarity_scores[token_id] = combined_rarity_score

    return token_rarity_scores

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    file_path = '/Users/boat/Projects/Blobert Data/traitsResults.json'  # Update this path to your JSON file location
    data = load_data(file_path)
    token_rarity_scores = calculate_rarity_scores(data)

    # Sort the rarity scores by highest rarity
    sorted_rarity_scores = sorted(token_rarity_scores.items(), key=lambda item: item[1], reverse=True)

    # Export the sorted rarity scores to a plain text file
    output_file_path = '/Users/boat/Projects/Blobert Data/rarityScoresSorted.txt'  # Define the output text file path
    with open(output_file_path, 'w') as outfile:
        # Write a header
        outfile.write("TokenID\tRarity Score\n")
        outfile.write("-" * 30 + "\n")
        
        # Write each token ID and its rarity score in a readable format
        for token_id, rarity_score in sorted_rarity_scores:
            outfile.write(f"{token_id}\t{rarity_score}\n")

    # Optionally, print a message to indicate the export is complete
    print(f'Sorted rarity scores exported to {output_file_path}')

if __name__ == '__main__':
    main()
