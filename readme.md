# Spectral Analysis and Stability Lobe Diagram Project

## Overview
This project is an experimental endeavor aimed at processing machining vibration data to perform spectral analysis and ultimately generate stability lobe diagrams. The workflow covers data import, FFT-based spectral analysis, spectrum smoothing with resonance peak identification, and final visualization of the lobe diagram based on a custom implementation of the Tlustý/Altintas equation for critical depth calculation.

**Note:** This project is still in the concept phase. A huge success would be to simply process the first step: loading the CSV data correctly.

## Features
- **Data Import:**
  Read data from CSV files using either `pandas.read_csv` or `numpy.loadtxt`.

- **FFT and Spectral Analysis:**
  Use `numpy.fft.rfft` for computing the FFT and apply spectral analysis methods such as `scipy.signal.welch` for power spectral density estimation and `scipy.signal.csd` for cross-spectrum analysis when needed.

- **Spectrum Smoothing and Resonance Peak Identification:**
  Smooth the spectrum and average the results to identify resonant peaks with functions like `scipy.signal.find_peaks`.

- **Visualization:**
  Plot both time-domain signals and frequency-domain curves using `matplotlib.pyplot.plot`.

- **Custom Tlustý/Altintas Equation Implementation:**
  Develop a custom function (using pure Python or `numpy`) to compute the critical depth of cut based on the Tlustý/Altintas equation.

- **Stability Lobe Diagram:**
  Generate the final stability lobe diagram using `matplotlib.pyplot.plot`, showcasing the stability boundaries in machining operations.

## Lobe Diagram Explanation
Lobe diagrams illustrate the stability regions in machining processes. They help predict chatter by mapping the relationship between cutting parameters and stability. The diagram typically shows "lobes" that indicate safe operating conditions and regions where vibrations may become unstable.


## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git

2. **Install Dependencies: Ensure you have the required Python libraries installed:**
   ```bash
   pip install pandas numpy scipy matplotlib
3. **Run the Project: Execute the main script to begin the analysis:**
    ```bash
    python main.py