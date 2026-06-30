import numpy as np
import matplotlib.pyplot as plt

# LMS Filter function
def lms_filter(noisy, clean, mu=0.01, filter_order=4):
    n_samples = len(noisy)
    # Initialize filter weights
    weights = np.zeros(filter_order)
    # Store output and error
    output = np.zeros(n_samples)
    error = np.zeros(n_samples)

    # Adaptive filtering loop
    for n in range(filter_order, n_samples):
        # Input vector (previous noisy samples)
        x = noisy[n-filter_order:n]
        # Filter output
        y = np.dot(weights, x)
        # Error = clean - output
        error[n] = clean[n] - y
        # Update weights
        weights = weights + 2 * mu * error[n] * x
        # Store output
        output[n] = y

    return output, error

# Example run
# Generate signals again
t = np.arange(1000)
clean = np.sin(2 * np.pi * 5 * t / 1000)
noisy = clean + np.random.normal(0, 0.5, 1000)

# Apply LMS filter
output, error = lms_filter(noisy, clean)

# Plot results
plt.figure(figsize=(10,5))
plt.plot(t, clean, label="Clean Signal")
plt.plot(t, noisy, label="Noisy Signal", alpha=0.6)
plt.plot(t, output, label="LMS Output", color="green")
plt.legend()
plt.title("Adaptive Noise Cancellation - LMS Filter")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()
