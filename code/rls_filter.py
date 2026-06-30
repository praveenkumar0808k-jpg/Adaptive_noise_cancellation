import numpy as np
import matplotlib.pyplot as plt

# RLS Filter function
def rls_filter(noisy, clean, filter_order=4, lam=0.99, delta=0.1):
    n_samples = len(noisy)
    # Initialize filter weights
    weights = np.zeros(filter_order)
    # Initialize inverse correlation matrix
    P = (1/delta) * np.eye(filter_order)
    # Store output and error
    output = np.zeros(n_samples)
    error = np.zeros(n_samples)

    # Adaptive filtering loop
    for n in range(filter_order, n_samples):
        # Input vector (previous noisy samples)
        x = noisy[n-filter_order:n][::-1]  # reverse for proper order
        # Filter output
        y = np.dot(weights, x)
        # Error = clean - output
        error[n] = clean[n] - y
        # Gain vector
        g = (P @ x) / (lam + x.T @ P @ x)
        # Update weights
        weights = weights + g * error[n]
        # Update inverse correlation matrix
        P = (P - np.outer(g, x.T @ P)) / lam
        # Store output
        output[n] = y

    return output, error

# Example run
# Generate signals again
t = np.arange(1000)
clean = np.sin(2 * np.pi * 5 * t / 1000)
noisy = clean + np.random.normal(0, 0.5, 1000)

# Apply RLS filter
output, error = rls_filter(noisy, clean)

# Plot results
plt.figure(figsize=(10,5))
plt.plot(t, clean, label="Clean Signal")
plt.plot(t, noisy, label="Noisy Signal", alpha=0.6)
plt.plot(t, output, label="RLS Output", color="red")
plt.legend()
plt.title("Adaptive Noise Cancellation - RLS Filter")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()
