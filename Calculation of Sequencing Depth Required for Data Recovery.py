import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# ========== DATA INPUT ==========
# DISK abundance group
disk_data = {
    "Dog": 24298,
    "Speech": 23070,
    "Cat": 22775,
    "Motto": 21019
}

# Random abundance group
random_data = {
    "Speech": 42331,
    "Motto": 24542,
    "Cat": 12214,
    "Dog": 5138
}

# ========== CALCULATIONS ==========
def calculate_abundances(data):
    total = sum(data.values())
    return {k: v/total for k,v in data.items()}

# Calculate relative abundances
p_disk = calculate_abundances(disk_data)['Dog']
p_random = calculate_abundances(random_data)['Dog']

# Target detection probability
target_prob = 0.9

# Calculate required depths
def calculate_required_D(p, target):
    return np.ceil(np.log(1 - target) / np.log(1 - p)).astype(int)

D_disk = calculate_required_D(p_disk, target_prob)
D_random = calculate_required_D(p_random, target_prob)
ratio = D_random / D_disk

# ========== PLOT GENERATION ==========
# Create detection probability curves
max_depth = max(D_random * 2, 60)  # Adjust x-axis limit
depths = np.arange(1, max_depth + 1)
prob_disk = 1 - (1 - p_disk)**depths
prob_random = 1 - (1 - p_random)**depths

# Initialize figure
plt.figure(figsize=(10, 6))

# Plot curves
plt.plot(depths, prob_disk, 'b-', linewidth=2, 
         label=f'DISK (Dog={p_disk*100:.1f}%)')
plt.plot(depths, prob_random, 'r-', linewidth=2, 
         label=f'Random (Dog={p_random*100:.1f}%)')

# Add reference lines
plt.axhline(y=target_prob, color='gray', linestyle='--', alpha=0.7)
plt.axvline(x=D_disk, color='blue', linestyle=':', alpha=0.5)
plt.axvline(x=D_random, color='red', linestyle=':', alpha=0.5)

# Mark critical points
plt.plot(D_disk, target_prob, 'bo', markersize=8)
plt.plot(D_random, target_prob, 'ro', markersize=8)

# Add annotations
plt.text(D_disk + 1, target_prob - 0.15, 
         f'D={D_disk}', color='blue', fontsize=12)
plt.text(D_random + 1, target_prob - 0.05, 
         f'D={D_random}', color='red', fontsize=12)
plt.text(5, target_prob + 0.02, 
         f'{target_prob*100:.0f}% detection threshold', 
         color='gray', fontsize=10)

# Formatting
plt.title('Sequencing Depth Requirements for Rare Species Detection', fontsize=14)
plt.xlabel('Sequencing Depth (Total Reads Sampled)', fontsize=12)
plt.ylabel('Detection Probability P(detect ≥1 read)', fontsize=12)
plt.legend(loc='lower right', fontsize=12)
plt.grid(alpha=0.2)
plt.ylim(0, 1.05)
plt.xlim(0, max_depth)

# Display ratio
plt.figtext(0.5, 0.01, 
            f"Depth ratio (Random/DISK) for {target_prob*100:.0f}% detection: {ratio:.1f}x",
            ha="center", fontsize=12, 
            bbox={"facecolor":"orange", "alpha":0.2, "pad":5})

# Save and show
plt.tight_layout()
plt.savefig('sequencing_depth_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# ========== OUTPUT RESULTS ==========
print("\n=== Calculation Results ===")
print(f"DISK group - Dog abundance: {p_disk*100:.2f}%")
print(f"Random group - Dog abundance: {p_random*100:.2f}%")
print(f"\nRequired depth for {target_prob*100:.0f}% detection:")
print(f"DISK group: D = {D_disk}")
print(f"Random group: D = {D_random}")
print(f"\nDepth ratio (Random/DISK): {ratio:.2f}x")
print(f"Abundance ratio (DISK/Random): {p_disk/p_random:.2f}x")