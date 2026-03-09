from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    def __init__(self, player_name: str):
        self._player_name = player_name

    @abstractmethod
    def play(self) -> None:
        pass
    
    @abstractmethod
    def pause(self) -> None:
        pass
    
    @abstractmethod
    def stop(self) -> None:
        pass
    
    def display_status(self) -> None:
        print(f"[{self._player_name}] Status: Ready")

    def log_action(self, action: str) -> None:
        print(f"[{self._player_name}] Action: {action}")


class AudioPlayer(MediaPlayer):
    def __init__(self, audio_file: str):
        super().__init__("AudioPlayer")
        self._audio_file = audio_file

    def play(self) -> None:
        self.log_action(f"Playing audio: {self._audio_file}")

    def pause(self) -> None:
        self.log_action(f"Puased audio: {self._audio_file}")

    def stop(self) -> None:
        self.log_action(f"Stopped audio: {self._audio_file}")


class VideoPlayer(MediaPlayer):
    def __init__(self, video_file: str, resolution: str):
        super().__init__("VideoPlayer")
        self._video_file = video_file
        self._resolution = resolution

    def play(self) -> None:
        self.log_action(f"Playing video: {self._video_file} at {self._resolution}")

    def pause(self) -> None:
        self.log_action(f"Paused video: {self._video_file}")

    def stop(self) -> None:
        self.log_action(f"Stopped video: {self._video_file}")

class StreamingPlayer(MediaPlayer):
    def __init__(self, stream_url: str, buffer_size: int):
        super().__init__("StreamingPlayer")
        self._stream_url = stream_url
        self._buffer_size = buffer_size

    def play(self) -> None:
        self.log_action(f"Streaming from: {self._stream_url} (buffer: {self._buffer_size}KB)")

    def pause(self) -> None:
        self.log_action(f"Paused stream: {self._stream_url}")

    def stop(self) -> None:
        self.log_action(f"Stopped stream: {self._stream_url}")


class PlayerController:
    def __init__(self, player: MediaPlayer):
        self._player = player

    def start_playback(self) -> None:
        self._player.display_status()
        self._player.play()

    def pause_playback(self) -> None:
        self._player.pause()

    def stop_playback(self) -> None:
        self._player.stop()
        

if __name__ == "__main__":
    audio_ctrl = PlayerController(AudioPlayer("song.mp3"))
    audio_ctrl.start_playback()
    audio_ctrl.pause_playback()

    print()

    video_ctrl = PlayerController(VideoPlayer("movie.mp4", "1080p"))
    video_ctrl.start_playback()
    video_ctrl.stop_playback()

    print()

    stream_ctrl = PlayerController(
        StreamingPlayer("https://stream.example.com/live", 2048))
    stream_ctrl.start_playback()
    stream_ctrl.stop_playback()