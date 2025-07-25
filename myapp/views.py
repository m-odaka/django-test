from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse

def index(request):
    return render(request, "myapp/index.html", {"now": timezone.now()})

def current_time(request):
    """
    ボタン押下で呼ばれるAJAX用エンドポイント。JSONでサーバ時刻を返す。
    """
    now = timezone.now().isoformat()
    return JsonResponse({"now": now})