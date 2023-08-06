import os
import subprocess
import sys
import threading
import wave
from typing import Callable, Optional
import simpleaudio as sa


class WavFile:
    """
    Class contains parameters of sound file.
    """

    def __init__(self, path: str):
        self.wave_object = sa.WaveObject.from_wave_file(path)
        self.file_name = path
        with wave.open(path, "rb") as file:
            self.width = file.getsampwidth()
            self.channels = file.getnchannels()
            self.rate = file.getframerate()
            self.frames = file.getnframes()
            self.data = file.readframes(self.frames)
            self.duration = float(self.frames) / self.rate


def mute(func: Callable):
    def decorated(self, *args, **kwargs):
        if self._mute:
            return
        return func(self, *args, **kwargs)
    return decorated


class WavPlayer:
    """
    Class loads sounds from files and plays sounds.
    """

    def __init__(self, wait: bool = True, device: Optional[str] = None, channels: Optional[int] = None):
        """
        :param wait: play sound in sync mode;
        :param device: device to play sound on (valid for Linux).
        """

        self.sounds = dict()
        self._channels = channels
        self._device = device
        self._mute = False
        self._threads = []
        self._wait = wait

        if sys.platform.startswith("linux"):
            self.play = self.__play_linux
        elif sys.platform.startswith("win"):
            import winsound
            self.winsound = winsound
            self.play = self.__play_win
        else:
            self.play = self.__play_sa

    def add_sound(self, file_name: str, sound_name: str):
        """
        Method creates WavFile-object with sound and adds it to dictionary.
        :param file_name: name of file with sound;
        :param sound_name: name of sound.
        """

        self.sounds[sound_name] = WavFile(file_name)

    def check_sound_available(self) -> bool:
        """
        Method checks if it is possible to play sound files in system.
        :return: True if it is possible.
        """

        path_to_dummy_wav = os.path.join(os.path.dirname(__file__), "void.wav")
        self.add_sound(path_to_dummy_wav, "epsound_test_sound_for_driver_checking")
        try:
            self.play("epsound_test_sound_for_driver_checking")
            return True
        except RuntimeError:
            return False

    def is_mute(self) -> bool:
        return self._mute

    def remove_channels(self):
        """
        Method removes channels.
        """

        self._channels = None

    def remove_device(self):
        """
        Method removes audio device.
        """

        self._device = None

    def set_channels(self, channels: int):
        """
        Method sets number of used channels.
        :param channels: number of used channels.
        """

        if channels:
            self._channels = channels
        else:
            self._channels = None

    def set_device(self, device: str):
        """
        Method sets audio device to play sound. Method is relevant for Linux only.
        :param device: audio device.
        """

        if device:
            self._device = device
        else:
            self._device = None

    def set_mute(self, state: bool = True):
        self._mute = state

    def stop(self):
        """
        Function stop thread with sound
        :return:
        """
        for th in self._threads:
            th.join()

    @mute
    def __play_linux(self, sound_name: str):
        """
        Method plays sound on Linux.
        :param sound_name: name of sound to be played.
        """

        fh = open(os.devnull, "wb")
        args = ["aplay",]
        if self._device:
            args.extend(["--device", self._device])
        if self._channels:
            args.extend(["--channels", str(self._channels)])
        args.append(self.sounds[sound_name].file_name)
        proc = subprocess.Popen(args, stdout=fh, stderr=fh)
        if self._wait:
            proc.wait()
        fh.close()

    @mute
    def __play_sa(self, sound_name: str):
        """
        Method plays sound in another OS.
        :param sound_name: name of sound to be played.
        """

        def _play():
            self.sounds[sound_name].wave_object.play()

        thread = threading.Thread(target=_play, args=())
        self._threads.append(thread)
        thread.start()

    @mute
    def __play_win(self, sound_name: str):
        """
        Method plays sound on Windows.
        :param sound_name: name of sound to be played.
        """

        flags = self.winsound.SND_NOSTOP
        if not self._wait:
            flags |= self.winsound.SND_ASYNC
        self.winsound.PlaySound(self.sounds[sound_name].file_name, flags)
