import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def main():
    # Parameters
    fs = 1000  # Sampling frequency
    f_signal = 5  # Signal frequency
    f_carrier = 100  # Carrier frequency
    duration = 10  # Duration of the signal in seconds

    # Time vector
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    # Original signal (message)
    message_signal = np.sin(2 * np.pi * f_signal * t)

    # Carrier signal
    carrier_signal = np.sin(2 * np.pi * f_carrier * t)

    # Modulation (AM)
    modulated_signal = (1 + message_signal) * carrier_signal

    # Demodulation (envelope detection)
    demodulated_signal = np.abs(modulated_signal)

    # Plotting
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.title("Message Signal")
    plt.plot(t, message_signal)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.title("Modulated Signal (AM)")
    plt.plot(t, modulated_signal)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.title("Demodulated Signal (Envelope Detection)")
    plt.plot(t, demodulated_signal)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.tight_layout()
    plt.savefig("modulation_demodulation.png")


if __name__ == "__main__":
    main()