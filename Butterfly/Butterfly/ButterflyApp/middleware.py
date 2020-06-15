# from django.http import HttpResponse
#
# class AppMaintenanceMiddleware(object):
#     def __init__(self,get_response):
#             self.get_response = get_response
#     def __call__(self,request):
#         if request.get_full_path() == 'quiz.html':
#             print(request.get_full_path())
            # response = self.get_response

        # return response
    # def process_request(request):
    #     if current_url == 'general_knowledge.html/':
    #         return HttpResponse("Under Construction")
