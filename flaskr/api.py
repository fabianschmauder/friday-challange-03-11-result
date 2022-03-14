import json
from flask import Blueprint

from flaskr.s3_utils import count_words_in_object, list_objects

api_bp = Blueprint("api", __name__)

@api_bp.route('/bucket/<bucketname>')
def bucket_objects(bucketname):
    objects = list_objects(bucketname)
    result = []

    for object in objects:
        mapped_object = {
            "key": object["Key"],
            "words": count_words_in_object(bucketname,object["Key"])
        }
        result.append(mapped_object)

    return json.dumps(result)