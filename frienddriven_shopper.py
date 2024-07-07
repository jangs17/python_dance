#!/usr/bin/env python3

# Example purchase data
purchases = {
    0: ["Book", "Pen"],
    1: ["Notebook", "Pen"],
    2: ["Book"],
    3: ["Pen"],
    4: ["Notebook"],
    5: ["Book", "Notebook"],
    6: ["Pen"],
    7: ["Book"],
    8: ["Notebook"],
    9: ["Pen"]
}

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def recommend_products(user_id):
    friends = users[user_id]["friends"]
    friend_ids = [friend["id"] for friend in friends]
    friend_purchases = [purchases[friend_id] for friend_id in friend_ids]
    
    # Flatten the list of friend purchases and get unique products
    recommended_products = set(item for sublist in friend_purchases for item in sublist)
    
    return recommended_products

def main():
    user_names = {user['name']: user['id'] for user in users}
    print("Welcome to the recommendation system!")
    print("Available users:", ", ".join(user_names.keys()))
    
    user_name = input("Enter your name: ")
    
    if user_name not in user_names:
        print("User not found!")
        return
    
    user_id = user_names[user_name]
    
    print("Here are the products available: Book, Pen, Notebook")
    purchase = input("What would you like to purchase? ")
    
    if purchase:
        if purchase not in purchases[user_id]:
            purchases[user_id].append(purchase)
    
    recommended_products = recommend_products(user_id)
    recommended_products.discard(purchase)  # Remove the already purchased item
    
    print(f"Based on your friends' purchases, we recommend: {', '.join(recommended_products)}")

if __name__ == "__main__":
    main()

