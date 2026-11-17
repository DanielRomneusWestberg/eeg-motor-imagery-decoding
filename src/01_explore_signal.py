from pathlib import Path

import matplotlib.pyplot as plt
import mne
import numpy as np
from mne.datasets import eegbci

paths = eegbci.load_data(subjects=[1], runs=[4, 8, 12])

raw_objects = [mne.io.read_raw_edf(path, preload=True) for path in paths]

raw = mne.concatenate_raws(raw_objects)

# Clean up channel names ("C3.." -> "C3") so channels can be selected by name
# and matched to standard electrode positions.
eegbci.standardize(raw)

# Attach standard 10-05 electrode positions (needed for spatial colors and topomaps).
raw.set_montage("colin27_1005")

# In runs 4, 8 and 12, T0 = rest, T1 = imagined left fist,
# T2 = imagined right fist (per PhysioNet docs).
# Verify annotations in data (other runs use T1/T2 for other tasks).
desc = raw.annotations.description
assert set(desc) == {"EDGE boundary", "BAD boundary", "T0", "T1", "T2"}, (
    f"Unexpected annotations: {set(desc)}"
)

# Check that classes (T1, T2) are balanced (chance level ~50%).
print(np.unique(desc, return_counts=True))

# Power spectrum of the motor cortex electrodes: expect 1/f decay, a mu/beta bump
# around 8-30 Hz, and a narrow 60 Hz line-noise peak (US power grid).
Path("figures").mkdir(exist_ok=True)

spectrum = raw.compute_psd(fmax=80, picks=["C3", "C4"])
fig = spectrum.plot()
fig.savefig("figures/psd_c3_c4.png", dpi=150)


# Interactive view of the raw signal with annotations.
raw.plot()
plt.show()
