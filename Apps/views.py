from django.shortcuts import HttpResponse,HttpResponseRedirect
from .forms import VideoForm
from .models import Youtube
from django.shortcuts import render,redirect
from pytube import YouTube

# Create your views here.
def download_video(request):
    if request.method=="POST":
            form = VideoForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data['url']
            # try:
            #     yt = YouTube(url)
            #     video_title = yt.title
            #     video_id = yt.video_id

            #     yt.streams.first().download()
                videos = Youtube(title="video_title", video_id="video_id", url=url)
                videos.save()
                # download video inn highest resolution stream
                # video_stream = yt.streams.get_highest_resolution()
                # video_stream.download()
                return redirect("download_video")
            # except Exception as e:
            #         error_message = f"Error:{e}"
    else:
        form = VideoForm()
        videos = Youtube.objects.all()
    return render(request,'downloader/download_video.html',{'form':form, 'video':videos})