from django.views import generic
from polls.models import Choice, Question
from django.utils import timezone


class HomePage(generic.ListView):
    template_name = "home.html"
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

class AboutPage(generic.TemplateView):
    template_name = "about.html"
