from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import Post, Tag


class HomeView(TemplateView):
  template_name = 'home.html'



def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog/post_list.html',
                  {'post_list': qs})

def post_detail(request, pk):
    post = Post.objects.all()
    all_tag = Tag.objects.all()
    mystr = post.tagged()
    my_tag = {}
    for t in all_tag:
        # mystr에서 t.name을 발견한 위치를 my_tag 사전에 등록
        # 키는 t.name으로, 값은 (못 찾으면 -1, 찾으면 양수)
        my_tag[t.name] = str(mystr).find(t.name)
    return render(request, 'blog/post_detail.html',
                  {'post': post, 'my_tag': my_tag})
