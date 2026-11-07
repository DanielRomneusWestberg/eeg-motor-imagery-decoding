# Decoding imagined hand movements from EEG

My first brain-computer interface project. The goal is to train a classifier that can tell from EEG alone whether a person is imagining moving their left or right hand.

## Data

[EEG Motor Movement/Imagery Dataset](https://physionet.org/content/eegmmidb/1.0.0/) from PhysioNet: 64-channel EEG sampled at 160 Hz, recorded with BCI2000. I use runs 4, 8 and 12, where the subject imagines opening and closing the left or right fist when a target appears on that side of the screen (T1 = left, T2 = right, T0 = rest). MNE downloads the files automatically the first time the script runs.

## Status

- [x] Load subject 1, check event labels and class balance, inspect the raw signal ([`src/01_explore_signal.py`](src/01_explore_signal.py))
- [ ] Filter to the mu (8-12 Hz) and beta (13-30 Hz) bands and cut out an epoch around each cue
- [ ] Train a first classifier and compare its cross-validated accuracy with chance (50 %)
- [ ] Repeat for more subjects and see how much accuracy varies between people

## Run it

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/01_explore_signal.py
```

## References

- Schalk, G. (2009). EEG Motor Movement/Imagery Dataset (version 1.0.0). PhysioNet. https://doi.org/10.13026/C28G6P
- Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N., & Wolpaw, J. R. (2004). BCI2000: A general-purpose brain-computer interface (BCI) system. *IEEE Transactions on Biomedical Engineering*, 51(6), 1034-1043.
- Pollard, T., et al. (2026). PhysioNet as a global platform for biomedical research. *Nature Health*. https://doi.org/10.1038/s44360-026-00096-z
