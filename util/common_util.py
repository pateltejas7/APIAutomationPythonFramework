import random


class commonUtility:

    @staticmethod
    def get_custom_header():
        header = {}
        return header

    @staticmethod
    def get_unique_email():
        random_no = random.randint(100000, 999999)
        email = f"test_automation{random_no}@mail.com"
        return email

