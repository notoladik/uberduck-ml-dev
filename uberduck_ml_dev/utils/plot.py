# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/utils.plot.ipynb (unless otherwise specified).

__all__ = ['save_figure_to_numpy', 'plot_tensor', 'plot_spectrogram', 'plot_attention', 'plot_gate_outputs']

# Cell
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def save_figure_to_numpy(fig):
    """Save figure to a numpy array."""
    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep="")
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return data


def plot_tensor(tensor):
    plt.style.use("default")
    fig, ax = plt.subplots(figsize=(12, 3))
    im = ax.imshow(tensor, aspect="auto", origin="lower", interpolation="none")
    plt.colorbar(im, ax=ax)
    plt.tight_layout()
    fig.canvas.draw()
    data = save_figure_to_numpy(fig)
    plt.close()
    return data


def plot_spectrogram(mel):
    figure = plt.figure()
    plt.xlabel("Spectrogram frame")
    plt.ylabel("Channel")
    plt.imshow(mel, aspect="auto", origin="lower", interpolation="none", cmap="inferno")
    figure.canvas.draw()
    return figure

# Cell


def plot_attention(attention, encoder_length=None, decoder_length=None):
    figure = plt.figure()
    plt.xlabel("Decoder timestep")
    plt.ylabel("Encoder timestep")
    plt.imshow(
        attention.data.cpu().numpy(),
        aspect="auto",
        origin="lower",
        interpolation="none",
        cmap="inferno",
    )
    title_info = []
    if encoder_length is not None:
        title_info.append(f"Encoder_length: {encoder_length}")
    if decoder_length is not None:
        title_info.append(f"Decoder length: {decoder_length}")
    title = " ".join(title_info)
    plt.title(title)
    figure.canvas.draw()
    return figure


def plot_gate_outputs(gate_targets=None, gate_outputs=None):
    figure = plt.figure()
    plt.xlabel("Frames")
    plt.ylabel("Gate state")
    ax = figure.add_axes([0, 0, 1, 1])
    if gate_targets is not None:
        ax.scatter(
            range(gate_targets.size(0)),
            gate_targets,
            alpha=0.5,
            color="green",
            marker="+",
            s=1,
            label="target",
        )
    if gate_outputs is not None:
        ax.scatter(
            range(gate_outputs.size(0)),
            gate_outputs,
            alpha=0.5,
            color="red",
            marker=".",
            s=1,
            label="predicted",
        )
    figure.canvas.draw()
    return figure