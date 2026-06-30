import numpy as np              # Library for math and arrays
import matplotlib.pyplot as plt # Library for plotting graphs

# Function to generate signals
def generate_signal(length=1000, freq=5, noise_type="white"):
    t = np.arange(length)  # Create time samples (0 to 999)
    clean = np.sin(2 * np.pi * freq * t / length)  # Clean sine wave

    # Add noise
    if noise_type == "white":
        noise = np.random.normal(0, 0.5, length)   # Random white noise
    elif noise_type == "colored":
        noise = np.convolve(np.random.normal(0, 0.5, length),
                            [0.2, 0.5, 0.3], mode='same')  # Colored noise
    else:
        noise = np.zeros(length)  # No noise

    noisy_signal = clean + noise  # Add noise to clean signal
    return t, clean, noisy_signal

# Run the generator
t, clean, noisy = generate_signal(noise_type="white")

# Plot signals
plt.figure(figsize=(10,5))
plt.plot(t, clean, label="Clean Signal")
plt.plot(t, noisy, label="Noisy Signal", alpha=0.7)
plt.legend()
plt.title("Adaptive Noise Cancellation - Signal Generator")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()
