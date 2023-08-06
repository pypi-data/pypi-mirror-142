# epsound

Minimalistic cross-platform library for playing sounds (from wav files).
* Works on Windows and Linux.
* Supports devices with architecture x86, x64 and arm.
* Provides minimal latency when starting and stopping sound playback.
* Suitable for adding sound effects to a device where you want to ensure maximum response speed.

Repository: https://github.com/EPC-MSU/epsound
## Prerequisites

Your Linux system should have the following installed to successfully complete:
```bash
     $ sudo apt-get install libasound2-dev
```

## Installation

Installation is very simple:
```bash
pip install epsound
```

## Working example

```Python
import time
import epsound

if __name__ == "__main__":
    # Let's create object of class WavPlayer and add sound from file with name "one" to it
    player = epsound.WavPlayer()
    player.add_sound(file="sound.wav", name="one")
    # Then let's play sound
    player.play("one")
    time.sleep(1)

```
