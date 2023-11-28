from flask import current_app, jsonify, blueprints

error_handler = blueprints.Blueprint("error_handler", __name__)


@error_handler.app_errorhandler(500)
def internal_server_error(e):
    current_app.logger.error(e)
    return (
        jsonify(
            {
                "status": "error",
                "message": "An error Occured...Try again later",
            }
        ),
        500,
    )


@error_handler.app_errorhandler(404)
def not_found_error(e):
    current_app.logger.error(e)
    return (
        jsonify(
            {
                "status": "error",
                "message": e.description,
            }
        ),
        404,
    )


@error_handler.app_errorhandler(400)
def bad_request_error(e):
    current_app.logger.error(e)
    return (
        jsonify(
            {
                "status": "error",
                "message": e.description,
            }
        ),
        400,
    )


@error_handler.app_errorhandler(401)
def unauthorized_error(e):
    current_app.logger.error(e)
    return (
        jsonify(
            {
                "status": "error",
                "message": e.description,
            }
        ),
        401,
    )


@error_handler.app_errorhandler(403)
def forbidden_error(e):
    current_app.logger.error(e)
    return (
        jsonify(
            {
                "status": "error",
                "message": "You are not allowed to access this resource",
            }
        ),
        403,
    )


@error_handler.app_errorhandler(Exception)
def unhandled_exception(e):
    current_app.logger.error(e)
    return (
        jsonify(
            {
                "status": "error",
                "message": "An error Occured...Try again later",
            }
        ),
        200,
    )
