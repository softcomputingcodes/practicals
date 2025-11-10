import random

# --- 1️⃣ Flipping Mutation (Binary GA) ---
def flip_mutation(chrom, rate=0.3):
    new = chrom.copy()
    for i in range(len(chrom)):
        if random.random() < rate:
            new[i] = 1 - new[i]  # Flip 0→1 or 1→0
    return new

# --- 2️⃣ Reversing Mutation (Binary GA) ---
def reverse_mutation(chrom):
    new = chrom.copy()
    i, j = sorted(random.sample(range(len(chrom)), 2))
    new[i:j] = reversed(new[i:j])  # Reverse a random segment
    print(f"👉 Reversed segment from index {i} to {j}")
    return new

# --- 3️⃣ Inversion Mutation (Order GA / TSP) ---
def inversion_mutation(chrom):
    new = chrom.copy()
    i, j = sorted(random.sample(range(len(chrom)), 2))
    new[i:j] = reversed(new[i:j])
    print(f"👉 Inverted segment from index {i} to {j}")
    return new

# --- 4️⃣ Swap Mutation (Order GA / TSP) ---
def swap_mutation(chrom):
    new = chrom.copy()
    i, j = random.sample(range(len(chrom)), 2)
    new[i], new[j] = new[j], new[i]
    print(f"👉 Swapped genes at index {i} and {j}")
    return new

# --- MAIN PROGRAM ---
def main():
    print("=== 🧬 Mutation Techniques Demonstration ===")
    print("Choose mutation type:")
    print("1. Flipping (Binary)")
    print("2. Reversing (Binary)")
    print("3. Inversion (Order-based)")
    print("4. Swap (Order-based)")

    choice = int(input("Enter your choice (1-4): "))

    # Get chromosome details dynamically
    n = int(input("\nEnter number of genes: "))

    if choice in [1, 2]:
        print("Enter binary chromosome (0s and 1s separated by space):")
        chrom = list(map(int, input().split()))
    else:
        print("Enter ordered chromosome (e.g., letters or numbers separated by space):")
        chrom = input().split()

    if len(chrom) != n:
        print("❌ Error: Number of genes entered doesn't match the specified count!")
        return

    print("\nOriginal Chromosome:", chrom)

    # Apply the chosen mutation
    if choice == 1:
        mutated = flip_mutation(chrom)
        print("After Flipping Mutation:", mutated)

    elif choice == 2:
        mutated = reverse_mutation(chrom)
        print("After Reversing Mutation:", mutated)

    elif choice == 3:
        mutated = inversion_mutation(chrom)
        print("After Inversion Mutation:", mutated)

    elif choice == 4:
        mutated = swap_mutation(chrom)
        print("After Swap Mutation:", mutated)

    else:
        print("❌ Invalid choice!")

    print("\n✅ Mutation Demonstration Complete")

# Run the program
if __name__ == "__main__":
    main()
