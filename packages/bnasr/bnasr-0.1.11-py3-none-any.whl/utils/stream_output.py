from datetime import datetime
def stream_output(transcript, status):
    return {
        'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'result': {'transcript': transcript},
        'status': status
    }