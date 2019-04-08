from pypianoroll import Multitrack, Track
from matplotlib import pyplot as plt
from prtoolkit import vis, utils

# load file
midifile = 'test.mid'
multi = Multitrack(midifile)

# select track
track = multi.tracks[2]

# get pianoroll (time x pitch)
pr = track.pianoroll

# ---------------------------------------------
# Example 1: visialize the piano roll
#   simmulate the scenario that the piano rolls
#   are usually downsampled and cropped

# downsample
pr = pr[::2, :]
resol = multi.beat_resolution // 2
# downbeats = multi.downbeat
downbeats = 4  # beats per bar

# crop by pitch
st, ed = 24, 84
pr_sub = pr[:, st:ed]

# set display range
x_range = (resol * downbeats * 16, resol * downbeats * 32)
y_range = (48, 80)

# display
fig, ax = vis.plot(
    pr_sub,
    note_range=(st, ed),
    beat_resolution=resol,
    downbeats=downbeats,
    x_range=x_range,
    y_range=y_range)

# plt.show()
fig.savefig('test.png')
plt.close()

# ---------------------------------------------
# Example 2: visialize the chromagram
#   using utils.py to create chromagram and
#   visualize it

chroma = utils.tochroma(pr)

# display
fig, ax = vis.plot_chroma(
    chroma,
    beat_resolution=resol,
    downbeats=downbeats,
    xtick='beat',
    x_range=x_range)

# plt.show()
fig.savefig('test_chroma.png')
plt.close()

# ---------------------------------------------
# Example 3: different layouts

fig, ax = vis.plot(
    pr_sub,
    note_range=(st, ed),
    beat_resolution=resol,
    downbeats=downbeats,
    grid_layout='both',
    x_range=x_range,
    y_range=y_range,
    xtick='beat',
    ytick='note',
    ytick_interval=1,
    xtick_interval=2)

# plt.show()
fig.savefig('test2.png')
plt.close()
