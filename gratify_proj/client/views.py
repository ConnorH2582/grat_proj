# Create your views he
from django.template.context import RequestContext

class HomeView(View):
	template='templates/home.html'
	def home(request):

		context = {'user': request.user}
		return render(request,self.template,context_instance=context)