import pyaudio
def check_mic():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if dev['maxInputChannels'] == 0:
            continue
        print((i,dev['name'],dev['maxInputChannels']))