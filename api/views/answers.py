from flask_restplus import Resource
from flask import jsonify, request
from main import api
from api.utilities.messages import SUCCESS_MESSAGES
from api.models import Answer, Question, User
from api.model_serializers import AnswerSchema
from api.middlewares.token_required import token_required


@api.route('/questions/<string:question_id>/answers')
class AnswerResource(Resource):
    def get(self, question_id):
        answers =  Question.get_or_404(question_id).answers
        answer_schema = AnswerSchema(many=True, only=["id", "title", "answerer"])

        return jsonify({
            "data": answer_schema.dump(answers).data,
            "status": "success",
            "message": SUCCESS_MESSAGES["fetched"].format("Answers")
        })

    # @token_required
    def post(self, question_id):
        request_data = request.get_json()

        user = User.query.get("16")
        question =  Question.get_or_404(question_id)

        answer_schema = AnswerSchema(only=["id", "title", "created_at", "updated_at", "parent_id"])
        answer_data = answer_schema.load_object_into_schema(request_data)
        answer_data["answerer"] = user
        answer_data["answer"] = question
        answer_data["parent_id"] = 12
        answer = Answer(**answer_data)
        answer.save()

        return jsonify({
            "data": answer_schema.dump_object_into_schema(answer),
            "status": "success",
            "message": SUCCESS_MESSAGES["created"].format("Answer")
        })


@api.route('/questions/<string:question_id>/answers/<string:answer_id>')
class SingleAnswerResource(Resource):
    def get(self, question_id, answer_id):
        answer =  Answer.get_or_404(answer_id)

        answer_schema = AnswerSchema(only=["id", "title", "answerer", "children", "parent"])

        return jsonify({
            "data": answer_schema.dump_object_into_schema(answer),
            "status": "success",
            "message": SUCCESS_MESSAGES["fetched"].format("Answers")
        })

    def put(self, question_id, answer_id):
        request_data = request.get_json()

        answer =  Answer.get_or_404(answer_id)

        answer_schema = AnswerSchema(only=["title"])
        answer_data = answer_schema.load_object_into_schema(request_data)

        answer = answer.update(answer_data)
        answer.save()

        return jsonify({
            "data": answer_schema.dump_object_into_schema(answer),
            "status": "success",
            "message": SUCCESS_MESSAGES["updated"].format("Answer")
        })

    def delete(self, question_id, answer_id):
        answer = Answer.get_or_404(answer_id)
        answer.delete()

        return jsonify({
            "status": "success",
            "message": SUCCESS_MESSAGES["deleted"].format("Answer")
        })
