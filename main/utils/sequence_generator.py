from main import db
from main.models.sequence import Sequence

def generate_sequence(sequence_name):
    if get_sequence := Sequence.query.filter_by(name=sequence_name).first():
        sequence = get_sequence.prefix + str(get_sequence.current)
        get_sequence.current = get_sequence.current + get_sequence.increment
        db.session.commit()
        return sequence
    else:
        return ''

