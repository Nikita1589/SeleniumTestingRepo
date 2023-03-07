import os

def get_base_url():

    env=os.environ.get('ENV','test')

    if env.lower()=='test':

        return "http://demostore.supersqa.com"

        # return "http://localhost:8887/quicksite/"
