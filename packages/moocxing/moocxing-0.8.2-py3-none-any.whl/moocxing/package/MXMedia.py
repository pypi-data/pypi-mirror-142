from time import sleep, time
import wave
import pyaudio
import logging
from threading import Thread
from moocxing.robot import Constants
import webrtcvad
import sys

log = logging.getLogger(__name__)


class MXMedia:

    def __init__(self):
        self._isPlay = False
        self._pause = False
        self._stop = False

    @staticmethod
    def record(RS=4, path=Constants.TEMP_PATH + "back.wav"):
        """录音"""
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000
        CHUNK_DURATION_MS = 30
        CHUNK_SIZE = int(RATE * CHUNK_DURATION_MS / 1000)

        vad = webrtcvad.Vad(1)

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        start=False,
                        frames_per_buffer=CHUNK_SIZE)

        stream.start_stream()
        log.info(f"* 开始录音{RS}s<<<<<<")

        frames = []
        flag = 0
        for _ in range(1000 * RS // CHUNK_DURATION_MS):
            data = stream.read(CHUNK_SIZE)
            active = vad.is_speech(data, RATE)

            sys.stdout.write('+' if active else '_')

            if active:
                flag = 0
            else:
                flag += 1
            if flag >= 20:
                break
            frames.append(data)
        sys.stdout.write('\n')
        stream.stop_stream()
        stream.close()

        wf = wave.open(path, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

        wf.close()
        p.terminate()
        log.info("* 结束录音<<<<<<")

    def play(self, path=Constants.TEMP_PATH + "back.wav"):
        """播放"""
        log.info("* 开始播放>>>>>>")
        wf = wave.open(path, 'rb')

        p = pyaudio.PyAudio()
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True)

        stream.start_stream()

        self._pause = False
        self._stop = False
        data = wf.readframes(1024)
        while data and not self._stop:
            if not self._pause:
                stream.write(data)
                data = wf.readframes(1024)

        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()

        log.info("* 结束播放>>>>>>")

    def playThread(self, path="back.wav"):
        Thread(target=self.play, args=(path,)).start()

    def stop(self):
        self._stop = True
        sleep(0.1)
        log.info("* 退出播放>>>>>>")

    def pause(self):
        self._pause = True
        log.info("* 暂停播放>>>>>>")

    def unpause(self):
        self._pause = False
        log.info("* 继续播放>>>>>>")
