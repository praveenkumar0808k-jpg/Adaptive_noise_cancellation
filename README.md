Adaptive Noise Cancellation (ANC) is a Digital Signal Processing (DSP) technique used to remove unwanted noise from signals such as speech or music.
This project demonstrates ANC using two adaptive filters: Least Mean Squares (LMS) and Recursive Least Squares (RLS).

Recruiter appeal: It shows practical DSP knowledge, coding skills, and visualization through dashboards.

🪜 Workflow
Signal Generator

Generates a clean sine wave.

Adds random noise (white or colored).

LMS Filter

Learns slowly to cancel noise.

Simple and lightweight.

RLS Filter

Learns faster and cancels noise more effectively.

More computationally complex.

Visualization Dashboard

Shows clean vs noisy vs LMS vs RLS signals.

Compares error curves.

Displays performance metrics (MSE).

📂 Project Structure
Code
Adaptive-Noise-Cancellation/
   ├── code/
   │   ├── signal_generator.py
   │   ├── lms_filter.py
   │   ├── rls_filter.py
   │   ├── dashboard.py
   ├── results/
   │   ├── signal_plot.png
   │   ├── lms_output.png
   │   ├── rls_output.png
   │   ├── dashboard.png
   └── README.md
📊 Results
Signal Plot → Clean vs noisy signal.

LMS Output → Filtered signal using LMS.

RLS Output → Filtered signal using RLS.

Dashboard → Combined view with error comparison.

🧠 Analysis
LMS converges slowly but is simple to implement.

RLS converges faster with lower error but requires more computation.

Error comparison plots clearly show RLS outperforming LMS.

🚀 Innovations
Added colored noise simulation for real‑world scenarios (traffic, crowd noise).

Implemented error comparison dashboard for recruiter‑friendly visualization.

Extended project with dynamic LMS step size for improved adaptability.

🎯 Conclusion
This project demonstrates how adaptive filters can effectively cancel noise in signals.
The dashboard visualization makes results easy to understand, and the README.md highlights workflow, analysis, and innovations for recruiters.