import mne
import numpy as np
from mne.datasets import eegbci

paths = eegbci.load_data(subjects=[1], runs=[4, 8, 12])

raw_objects = [mne.io.read_raw_edf(path, preload=True) for path in paths]

raw = mne.concatenate_raws(raw_objects)

# Clean up channel names ("C3.." -> "C3") so channels can be selected by name
# and matched to standard electrode positions.
eegbci.standardize(raw)

# In runs 4, 8 and 12, T0 = rest, T1 = imagined left fist,
# T2 = imagined right fist (per PhysioNet docs).
# Verify annotations in data (other runs use T1/T2 for other tasks).
desc = raw.annotations.description
assert set(desc) == {"EDGE boundary", "BAD boundary", "T0", "T1", "T2"}, (
    f"Unexpected annotations: {set(desc)}"
)

# Check that classes (T1, T2) are balanced (chance level ~50%).
print(np.unique(desc, return_counts=True))

# Visualize EEG data
raw.plot(block=True)
