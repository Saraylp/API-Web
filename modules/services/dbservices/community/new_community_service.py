# -*- coding: utf-8 -*-
from services.interfaces.i_service import IService

class NewCommunityService (IService):
    def __init__(self, core, parameters):
        super(NewCommunityService, self).__init__(core, parameters)

    def run(self):
        image = self.parameters.get("banner", None)
        self.parameters.pop("banner", None)

        record = self.core.InternalOperation("createCommunity",self.parameters)
        result = self.core.InternalOperation("suscribeUser2Community",
                                             {"id_user": record["id_creator"], "id_community": record["_id"]})

        id = record.get("_id", None)

        if not id:
            raise Exception("New community, Not exists the ID to generate the image.")

        print "Voy a entrar"
        if image:
            urlImage = self.core.InternalOperation("saveBanner", {'id':id, 'data':image})
            result['image'] = urlImage
        else:
            print "Entrando por save default banner"
            description = record.get("description", "")
            keywords = record.get("keywords", [])
            urlImage = self.core.InternalOperation("saveDefaultBanner", {'id':str(id), 'description': description, 'keywords':keywords})
            result['image'] = urlImage


        return result