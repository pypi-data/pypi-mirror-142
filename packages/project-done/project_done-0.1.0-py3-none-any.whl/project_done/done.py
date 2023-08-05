from IPython.display import Audio, display
from datetime import datetime


def done(sound_path='sound_effects/mixkit-retro-game-notification-212.wav'):
    # play sound in ipython
    display(Audio(filename=sound_path, autoplay=True))
    now = datetime.now()
    message = "Finished @" + now.strftime("%Y-%m-%d, %H:%M:%S")
    return message


def slack_done():
    pass
