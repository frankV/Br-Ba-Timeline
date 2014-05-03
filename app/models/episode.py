from app import db

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    season = db.Column(db.Float)
    number = db.Column(db.Integer)
    title = db.Column(db.String)
    released = db.Column(db.Date)
    duration = db.Column(db.Integer)
    rating = db.Column(db.Float)
    summary = db.Column(db.String)
    storyline = db.Column(db.String)
    photos = db.Column(db.String)
    keywords = db.Column(db.String)
    quote = db.Column(db.String)
    director = db.Column(db.String)
    writer = db.Column(db.String)
    calendar_start = db.Column(db.Date)
    calendar_end = db.Column(db.Date)


    def to_dict(self):
        return dict(
            season = self.season,
            number = self.number,
            title = self.title,
            released = self.released.isoformat(),
            duration = self.duration,
            rating = self.rating,
            summary = self.summary,
            storyline = self.storyline,
            photos = self.photos,
            keywords = self.keywords,
            quote = self.quote,
            director = self.director,
            writer = self.writer,
            calendar_start = self.calendar_start.isoformat(),
            calendar_end = self.calendar_end.isoformat(),
            id = self.id
        )

    def __repr__(self):
        return '<Episode %r>' % (self.id)
