from app import db
from app.models.log import Log


def read_log(save_path):
    with open(save_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        log = Log(content=content)
                        db.session.add(log)
                        db.session.commit()
                        