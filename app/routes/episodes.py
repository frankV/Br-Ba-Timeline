from app import app, db
from app.models import episode
from flask import abort, jsonify, request
import datetime
import json

@app.route('/bb.timeline/episodes', methods = ['GET'])
def get_all_episodes():
    entities = episode.Episode.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/bb.timeline/episodes/<int:id>', methods = ['GET'])
def get_episode(id):
    entity = episode.Episode.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/bb.timeline/episodes', methods = ['POST'])
def create_episode():
    entity = episode.Episode(
        season = request.json['season']
        , number = request.json['number']
        , title = request.json['title']
        , released = datetime.datetime.strptime(request.json['released'], "%Y-%m-%d").date()
        , duration = request.json['duration']
        , rating = request.json['rating']
        , summary = request.json['summary']
        , storyline = request.json['storyline']
        , photos = request.json['photos']
        , keywords = request.json['keywords']
        , quote = request.json['quote']
        , director = request.json['director']
        , writer = request.json['writer']
        , calendar_start = datetime.datetime.strptime(request.json['calendar_start'], "%Y-%m-%d").date()
        , calendar_end = datetime.datetime.strptime(request.json['calendar_end'], "%Y-%m-%d").date()
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/bb.timeline/episodes/<int:id>', methods = ['PUT'])
def update_episode(id):
    entity = episode.Episode.query.get(id)
    if not entity:
        abort(404)
    entity = episode.Episode(
        season = request.json['season'],
        number = request.json['number'],
        title = request.json['title'],
        released = datetime.datetime.strptime(request.json['released'], "%Y-%m-%d").date(),
        duration = request.json['duration'],
        rating = request.json['rating'],
        summary = request.json['summary'],
        storyline = request.json['storyline'],
        photos = request.json['photos'],
        keywords = request.json['keywords'],
        quote = request.json['quote'],
        director = request.json['director'],
        writer = request.json['writer'],
        calendar_start = datetime.datetime.strptime(request.json['calendar_start'], "%Y-%m-%d").date(),
        calendar_end = datetime.datetime.strptime(request.json['calendar_end'], "%Y-%m-%d").date(),
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/bb.timeline/episodes/<int:id>', methods = ['DELETE'])
def delete_episode(id):
    entity = episode.Episode.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
