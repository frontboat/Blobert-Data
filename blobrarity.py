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

    # Print or save the rarity scores
    for token_id, rarity_score in sorted(token_rarity_scores.items(), key=lambda item: item[1], reverse=True):
        print(f'TokenID: {token_id}, Rarity Score: {rarity_score}')

if __name__ == '__main__':
    main()
