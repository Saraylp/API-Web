# -*- coding: utf-8 -*-

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getFirstByFieldsPost():
    core = Core()
    result = core.PostOperation("getFirstByFieldsPost", request.vars)
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
#@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "getByIdPost")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getByIdPost():
    _id = request.vars["id"]
    result = Core().PostOperation("getByIdPost", {"_id":_id})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getPosts():
    core = Core()
    result = core.PostOperation("getAllPost", {})
    return response.json(result)

##Used from Front##
#@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["DELETE"], request)
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "deletePost")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def deletePost():
    _id = request.vars["id"]
    core = Core()
    result = core.PostOperation("deletePost", {"_id":_id})
    if result >= 1:
        return response.json({"result":0})
    return response.json({"result":1})

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def createPost():
    core = Core()
    result = core.PostOperation("createPost", dict(request.vars))
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory", "new_values":"mandatory"}, "updatePost")
def updatePost():
    _id = request.vars["id"]
    _new_values = request.vars["new_values"]
    core = Core()
    result = core.PostOperation("updatePost", {"_id":_id, "new_values":_new_values})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "getPostsByCommunityId")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getPostsByCommunityId():
    _id = request.vars["id"]
    core = Core()
    result = core.PostOperation("getPostsByCommunityId", {"community_id" : _id})
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "getPostsByCommunityFormat")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getPostsByCommunityFormated():
    _id = request.vars["id"]
    core = Core()
    result = core.PostOperation("getPostsByCommunityFormated", {"community_id" : _id})
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getCommunityPosts():
    _id = request.vars["id"]
    return response.json(Core().PostOperation("getCommunityPosts", {"community_id": _id}))

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory", "post":"mandatory"}, "updatePostContent")
def updatePostContent():
    _id = request.vars["id"]
    _post = request.vars["post"]
    result = Core().PostOperation("updatePostContent", {"id":_id, "post":str(_post)})
    return response.json(result)

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"user_id":"mandatory", "id":"mandatory"}, "like2Post")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def like2Post():
    return response.json(Core().PostOperation("like2Post", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"user_id":"mandatory", "id":"mandatory"}, "unlike2Post")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def unlike2Post():
    return response.json(Core().PostOperation("unlike2Post", dict(request.vars)))

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"user_id":"mandatory", "id":"mandatory", "status":"mandatory"}, "likePost")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def likePost():
    return response.json(Core().PostOperation("likePost", dict(request.vars)))

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"user_id":"mandatory", "post_id":"mandatory", "comment":"mandatory","files":"optional"}, "comment2Post")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def commentPost():
    core = Core()
    result = core.PostOperation("comment2Post", dict(request.vars))
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "getCommentsByPost")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getCommentsByPost():
    _id = request.vars["id"]
    core = Core()
    result = core.PostOperation("getCommentsPost", {"post_id": _id})
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def newPost():
    result = Core().PostOperation("newPost", dict(request.vars))
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "getMainCommunityById")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getMainCommunityById():
    _id = request.vars["id"]
    core = Core()
    result = core.PostOperation("getMainCommunityById", {"user_id": _id})
    return response.json(result)

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST"], request)
#@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "checkSurveyByPostId")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def checkSurveyByPostId():
    return response.json(Core().PostOperation("checkSurveyByPostId", dict(request.vars)))

##Used from Front##
@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST","OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"link":"mandatory"}, "checkContentTypeUrl")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def checkContentTypeUrl():
    return response.json(Core().PostOperation("checkContentTypeUrl", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["POST", "OPTIONS"], request)
@HTTP_METHOD_OPTION_CHECKER_DECORATOR.isOption(request, response)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"user_id":"mandatory","community_id":"mandatory","post_id":"mandatory"}, "checkContentTypeUrl")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def newRepost():
    return response.json(Core().PostOperation("newRepost", dict(request.vars)))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "getRepost")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def getRepost():
    _id = request.vars["id"]
    return response.json(Core().PostOperation("getRepost", {"post_id": _id}))

@HTTP_METHOD_CONSTRAINT_DECORATOR.isAllowed(["GET"], request)
@CHECK_PARAMETERS_DECORATOR.checkIt(request.vars, {"id":"mandatory"}, "countRepost")
@CROSS_DOMAIN_DECORATOR.changesHeaders(response)
def countRepost():
    _id = request.vars["id"]
    return response.json(Core().PostOperation("countRepost", {"post_id": _id}))
