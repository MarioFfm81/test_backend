from flask_restful import Resource

class Feedback(Resource):
    def get(self):
        file = open("testfile.txt","r")
        content = file.read()
        file.close()
        return {"msg": content}