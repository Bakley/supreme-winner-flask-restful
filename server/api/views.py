# """Meetup views file"""
# import json
# from flask_restful import Resource, reqparse
# from flask_jwt_extended import jwt_required




# class QuestionViewsResource(Resource):
#     """Create and Delete a meetup"""
#     parser = reqparse.RequestParser()
#     parser.add_argument('title', required=True,
#                         help='title cannot be blank', type=str)
#     parser.add_argument('body', required=True,
#                         help='body cannot be blank', type=str)
#     parser.add_argument('userId', required=True,
#                         help='User ID cannot be blank', type=int)
#     parser.add_argument('meetupId', required=True,
#                         help='Meetup Id cannot be blank', type=int)

#     @jwt_required
#     def post(self, meetup_id):
#         """Admin create a meetup"""

#         try:
#             meetup_id = int(meetup_id)
#         except Exception:
#             return {
#                 "status": 404,
#                 "error": "Resource Identifier need an integer"
#             }, 404
#         try:
#             args = QuestionViewsResource.parser.parse_args()
#             title = args.get('title')
#             body = args.get('body')
#             userId = args.get('userId')
#             meetupId = args.get('meetupId')
#         except Exception:
#             return {
#                 "status": 400,
#                 "error":
#                 "Invalid field. Missing or wrongly spelled Keys, should be title and body"
#             }, 400

#         # Check for user
#         question_meetup = meetup_views.get_a_specific_meetup_id(id=meetup_id)
#         if not question_meetup:
#             return {
#                 "status": 404,
#                 "error": "Meetup of id {} not found".format(meetup_id)
#             }, 404

#         # Check meetup passed by user
#         passed_meetup = meetup_views.get_a_specific_meetup_id(args['meetupId'])
#         print("Passed meetup", passed_meetup)
#         if not passed_meetup:
#             return {
#                 "status": 404,
#                 "error": "The meetup you entered is not found. Please pass same meetup on your URL"
#             }, 404

#         # check user input int
#         for values in meetupId, userId:
#             if not check_number_format(values):
#                 return {
#                     "status": 404,
#                     "error": "Resource Identifier need an integer"
#                 }, 404

#         # check if meetup url and passed url are equal
#         if args['meetupId'] != meetup_id:
#             return {
#                 "status": 404,
#                 "error": "Meetup of id do not match"
#             }, 404

#         if check_for_empty_string(title):
#             return {
#                 "status": 400,
#                 "error":
#                 "Please provide a title for the question"
#             }, 400

#         if check_for_empty_string(body):
#             return {
#                 "status": 400,
#                 "error":
#                 "Please provide a body for the question"
#             }, 400

#         question = question_views.create_a_question(
#             title=args.get('title'),
#             body=args.get('body'),
#             userId=args.get('userId'),
#             meetupId=args.get('meetupId')
#         )

#         return {
#             "status": 201,
#             "data": question,
#             "Message": "Question successfully created"
#         }, 201


# class UpvoteResource(Resource):
#     """Upvote view class"""

#     @jwt_required
#     def patch(self, questions_id):
#         """Upvote method, increments a vote by 1"""
#         try:
#             questions_id = int(questions_id)
#         except Exception:
#             return {
#                 "status": 404,
#                 "error": "Resource Identifier need an integer"
#             }, 404

#         new_question_vote = question_views.upvote_question(id=questions_id)
#         new_question_vote = json.dumps(new_question_vote, default=str)
#         new_question_vote = json.loads(new_question_vote)

#         if not new_question_vote:
#             return {
#                 "status": 404,
#                 "error": "No question found"
#             }, 404
#         return {
#             "status": 200,
#             "data": new_question_vote
#         }


# class DownvoteResource(Resource):
#     """Downvote view class"""

#     @jwt_required
#     def patch(self, questions_id):
#         """Downvote method, decrements a vote by 1"""

#         try:
#             questions_id = int(questions_id)
#         except Exception:
#             return {
#                 "status": 404,
#                 "error": "Resource Identifier need an integer"
#             }, 404

#         new_question_downvote = question_views.downvote_question(
#             id=questions_id)
#         new_question_downvote = json.dumps(new_question_downvote, default=str)
#         new_question_downvote = json.loads(new_question_downvote)

#         if not new_question_downvote:
#             return {
#                 "status": 404,
#                 "error": "No question found"
#             }, 404
#         return {
#             "status": 200,
#             "data": new_question_downvote
#         }


# class SpecificQuestion(Resource):
#     """Get a specific question"""

#     @jwt_required
#     def get(self, questions_id):
#         """Method to get a specific question"""
#         try:
#             questions_id = int(questions_id)
#         except Exception:
#             return {
#                 "status": 404,
#                 "error": "Url need an integer"
#             }, 404
#         new_question = question_views.get_a_specific_question(id=questions_id)
#         new_question = json.dumps(new_question, default=str)
#         new_question = json.loads(new_question)
#         if not new_question:
#             return {
#                 "status": 404,
#                 "error": "Question of id {} not found".format(questions_id)
#             }, 404
#         return {
#             "status": 200,
#             "data": new_question
#         }, 200