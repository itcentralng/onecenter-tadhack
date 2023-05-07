from app import celery, db

import os

from app.review.model import Review
from helpers.openai import transcribe, rewrite



@celery.task
def create_transcript(review_id, transient_audio_file=None):
    try:
        if transient_audio_file:
            review = Review.get_by_id(review_id)
            transcript = transcribe(transient_audio_file)
            review.content = rewrite(transcript).get('content')
            os.remove(transient_audio_file)
            return "Review Generated Successfully!"
    except Exception as e:
        print(e)
        if transient_audio_file:
            try:
                os.remove(transient_audio_file)
            except:
                pass
        db.session.rollback()
        return "Review Could Not Be Generated Successfully!"