from models import session
import inspect

def create(data, Model):
    Model = (
        Model(
            **data
        )
    )
    try:
        session.add(Model)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
