from flask import Flask, request

app = Flask(__name__)

# creat the real project 
ideas = {
    1 :{
        "id" : 1,
        "idea_name" : "vishal",
        "idea_description" : "Detail about vishal",
        "idea_author" : " kumar"
    },
    2 : { "id" : 2,
            "idea_name" : "vishal thakur",
            "idea_description" : "Deol",
            "idea_author" : " parjapati"
    },
    4 : {
        "id": 4,
            "idea_author": "tarun",
            "idea_description": "Ai and it adoptation",
            "idea_name": "AI"
    }
}

''' Creat an restful end poin for fetching  all the ideas'''

@app.get("/ideaapp/api/v1/ideas")
def  get_all_ideas():
    #i need to read query param
    idea_author = request.args.get("idea_author")
    if idea_author:
        # filter the idea create by author
        idea_res = {}
        for key,value in ideas.items():
            if value ['idea_author'] == idea_author:
                idea_res[key] = value
        return idea_res 
    #logice to fetch all ideas
    return ideas


'''creat  a restful endpoint for creating a  new idea'''

@app.post("/ideaapp/api/v1/ideas")
def creat_idea():
    try:
        request_body = request.get_json()

        if request_body['id'] and request_body['id'] in  ideas:
            return "idea with the same id already present", 409
    
        ideas[request_body['id']] = request_body
        return 'idea created and saved successful ',201
    except KeyError:
        return "id is missing", 400
    except:
        return "some internal error",500


'''end  point to fetch idea base on the idea id'''

@app.get("/ideaapp/api/v1/ideas/<idea_id>")
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return "idea id pass in not present",400

    except:
        return "some internal error",500
    

'''End point for the updating the idea
'''

@app.put("/ideaapp/api/v1/ideas/<idea_id>")
def update_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)] = request.get_json()
            return ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400
        
    except:
        return "some internal error is happen",500
    

'''end point to delete an idea'''
@app.delete("/ideaapp/api/v1/ideas/<idea_id>")
def delete_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas.pop(int(idea_id))
            return "Idea got successful remove"
        else:
            return "Idea id pass is not present",400
        
    except:
        return "some internal error is happen",500


    
if __name__ == '__main__': 
    app.run(port = 1962)





