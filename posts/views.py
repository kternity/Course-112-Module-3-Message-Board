from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class PostListView(ListView): #select all from and show on python
   template_name = "list.html"
   model = Post

class PostDetailView(DetailView):#this will give a sigle Post return 
   template_name = "detail.html"
   model = Post

class PostCreateView(CreateView): 
   template_name = "new.html" #you need to creatd this new.html template
   model = Post
   fields = ["title", "subtitle", "body"] # we are only exposing the 3 from the 4 fields created in models

      