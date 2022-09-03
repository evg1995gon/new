import datetime

def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        "year": datetime.datetime.now().year
    }

# def post_number(request):
#     current_url = request.resolver_match.url_name
#     return {
#         #'post_number': request.resolver_match.url_name,
#         'post_number': request.resolver_match.url_name
#     }