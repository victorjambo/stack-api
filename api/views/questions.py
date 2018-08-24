from flask_restplus import Resource
from flask import jsonify, request
from main import api
from api.utilities.messages import SUCCESS_MESSAGES
from api.models import Question, User
from api.model_serializers import QuestionSchema


@api.route('/questions')
class QuestionResource(Resource):
    def get(self):
        questions = Question.query.all()
        questions_schema = QuestionSchema(many=True, only=("id", "title", "questioner"))
        return jsonify({
            "data": questions_schema.dump(questions).data,
            "status": "success",
            "message": SUCCESS_MESSAGES["fetched"].format("Questions")
        })

    def post(self):
        request_data = request.get_json()

        # Update this. user_id should come from token
        user = User.query.get("2")

        question_schema = QuestionSchema(only=["id", "title", "created_at", "updated_at"])
        question_data = question_schema.load_object_into_schema(request_data)
        question_data["questioner"] = user
        question = Question(**question_data)
        question.save()

        return jsonify({
            "data": question_schema.dump(question).data,
            "status": "success",
            "message": SUCCESS_MESSAGES["created"].format("Question")
        })


@api.route('/questions/<string:question_id>')
class SingleQuestionResource(Resource):
    def get(self, question_id):
        question = Question.get_or_404(question_id)
        question_schema = QuestionSchema(only=["title"])

        return jsonify({
            "data": question_schema.dump_object_into_schema(question),
            "status": "success",
            "message": SUCCESS_MESSAGES["fetched"].format("Question")
        })

    def put(self, question_id):
        request_data = request.get_json()

        question = Question.get_or_404(question_id)

        question_schema = QuestionSchema(only=["title"])
        question_data = question_schema.load_object_into_schema(request_data)

        question = question.update(question_data)
        question.save()

        return jsonify({
            "data": question_schema.dump_object_into_schema(question),
            "status": "success",
            "message": SUCCESS_MESSAGES["updated"].format("Question")
        })

    def delete(self, question_id):
        question = Question.get_or_404(question_id)
        question.delete()

        return jsonify({
            "status": "success",
            "message": SUCCESS_MESSAGES["deleted"].format("Question")
        })
