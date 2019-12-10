import json

AUTH_COOKIE_NAME = 'tizza-auth'


class TizzaAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        unsigned_auth_cookie = request.get_signed_cookie(AUTH_COOKIE_NAME)
        request.auth = json.loads(unsigned_auth_cookie)

        response = self.get_response(request)

        response.set_signed_cookie(AUTH_COOKIE_NAME, json.dumps(unsigned_auth_cookie))

        return response


class SignupView(View):
    template_name = 'signup.html'

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            response.set_signed_cookie(AUTH_COOKIE_NAME, json.dumps({
                # auth cookie value
            }))

            login(request, user)
            return redirect('/')
