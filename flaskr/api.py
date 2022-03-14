from flask import Blueprint

api_bp = Blueprint("api", __name__)

@api_bp.route('/bucket/<bucketname>')
def bucket_objects(bucketname):
    return bucketname