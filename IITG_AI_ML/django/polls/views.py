from django.http import HttpResponse

from .models import Question


def index(request):
    # The following line retrieves the latest 5 questions from the database, 
    # ordered by publication date in descending order (most recent first).
    # The slice method is used here to limit the results to the first 5 records.
    # Examples of the slice method:
    # - Question.objects.all()[:10] retrieves the first 10 questions.
    # - Question.objects.order_by("pub_date")[5:15] retrieves questions 6 to 15.
    # - Question.objects.filter(is_published=True)[:3] retrieves the first 3 published questions.
    
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


