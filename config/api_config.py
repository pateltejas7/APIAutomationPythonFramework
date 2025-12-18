from functional_APITest.functional_param import FunctionalParam


class APIURLS:

    Get_User = FunctionalParam.get_base_end_point() + "/public/v2/users"

    @staticmethod
    def get_user_userid(user_id):
        return FunctionalParam.get_base_end_point() + f"/public/v2/users/{user_id}"