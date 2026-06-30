import numpy as np
import matplotlib.pyplot as plt
from lms_filter import lms_filter
from rls_filter import rls_filter

# Generate signals
t = np.arange(1000)
clean = np.sin(2 * np.pi * 5 * t / 1000)
noisy = clean + np.random.normal(0, 0.5, 1000)

# Apply LMS and RLS filters
lms_output, lms_error = lms_filter(noisy, clean)
rls_output, rls_error = rls_filter(noisy, clean)

# Create dashboard with subplots
plt.figure(figsize=(12,8))

# Plot signals
plt.subplot(2,2,1)
plt.plot(t, clean, label="Clean")
plt.plot(t, noisy, label="Noisy", alpha=0.6)
plt.title("Clean vs Noisy Signal")
plt.legend()

# Plot LMS output
plt.subplot(2,2,2)
plt.plot(t, clean, label="Clean")
plt.plot(t, lms_output, label="LMS Output", color="green")
plt.title("LMS Filter Output")
plt.legend()

# Plot RLS output
plt.subplot(2,2,3)
plt.plot(t, clean, label="Clean")
plt.plot(t, rls_output, label="RLS Output", color="red")
plt.title("RLS Filter Output")
plt.legend()

# Plot error comparison
plt.subplot(2,2,4)
plt.plot(t, lms_error, label="LMS Error", color="green")
plt.plot(t, rls_error, label="RLS Error", color="red")
plt.title("Error Comparison")
plt.legend()

plt.tight_layout()
plt.show()
