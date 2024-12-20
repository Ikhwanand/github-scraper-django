from django.shortcuts import render
from .forms import ProfileForm
from .scrape import scrape_github_profile
from .models import GithubProfile

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            profile_data = scrape_github_profile(username)
            if profile_data:
                profile, created = GithubProfile.objects.update_or_create(
                    username=username,
                    defaults=profile_data
                )
                return render(request, 'scraper/result.html', {'profile': profile})
            else:
                form.add_error('username', 'Profile not found')
    else:
        form = ProfileForm()
    return render(request, 'scraper/index.html', {'form': form})