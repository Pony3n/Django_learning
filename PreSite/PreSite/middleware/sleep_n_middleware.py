import random
import time


class SleepNMiddleware:
    def __init__(self, get_response, count=0):
        self.get_response = get_response
        self.count = count


    def __call__(self, request):
        self.count += 1

        if self.count % 5 != 0:
            pass
        else:
            time.sleep(1)
            self.count = 1

        response = self.get_response(request)
        count = self.count

        return response



