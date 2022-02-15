from django.http import Http404,HttpResponseRedirect
from audioop import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, View,CreateView
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
# Create your views here.
class Index(DeleteView):
    def get(self, request):

        new_post = Post.objects.all().order_by('-time')[:5]

        context={
            'new_post':new_post
        }
        return render(request, 'base.html',context)

class Profile(DeleteView):
    def get(self, request):
        if not request.user.is_authenticated:
             return render(request, 'errorac.html')
        user = request.user
        new_post = Post.objects.filter(auth = user).order_by('-time')[:5]
        context={
            'new_post':new_post
        }
        return render(request, 'prof.html',context)


class AllProfPost(DeleteView):
    def get(self, request):
        if not request.user.is_authenticated:
             return render(request, 'errorac.html')
        user = request.user
        post = Post.objects.filter(auth = user).order_by('-time')
        context={
            'post':post
        }
        return render(request, 'allprofpost.html',context)

class AllProfCom(DeleteView):
    def get(self, request):
        if not request.user.is_authenticated:
             return render(request, 'errorac.html')
        user = request.user
        art = Article.objects.filter(auth_article = str(user)).order_by('-time_article')
        context={
            'art':art
        }
        return render(request, 'comment.html',context)


class AllProfArtToDel(DeleteView):
    def get(self, request):
        if not request.user.is_authenticated:
             return render(request, 'errorac.html')
        user = request.user
        art = Article.objects.filter(auth_article = str(user)).order_by('-time_article')
        context={
            'art':art
        }
        return render(request, 'commentodel.html',context)


class AllProfArtDellId(DeleteView):
    def post(self, request,art_id):
        if not request.user.is_authenticated:
             return render(request, 'errorac.html')
        user = request.user
        art = Article.objects.get(id = art_id)
        art.delete()
        return redirect('delart')

class AllProfPostDell(DeleteView):
    def get(self, request):
        if not request.user.is_authenticated:
             return render(request, 'errorac.html')
        user = request.user
        post = Post.objects.filter(auth = user).order_by('-time')
        context={
            'post':post
        }
        return render(request, 'allpostdel.html',context)



class AllProfPostDellId(DeleteView):
    def post(self, request,post_id):
        if not request.user.is_authenticated:
             return render(request, 'errorac.html')
        user = request.user
        post = Post.objects.get(id = post_id)
        post.delete()
        return redirect('profalld')
        




class Login(DeleteView):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'errorlogin.html')

        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            messages.info(request,'Пароль или логен не верный....')
            return render(request, 'login.html')

class Reg(CreateView):
    def get(self,request,*args, **kwargs):
        form=RegisterForm()
        if request.user.is_authenticated:
            return render(request, 'errorlogin.html')
        return render(request, 'reg.html',{'form':form})

    def post(self,request,*args, **kwargs):
        user = User.objects.all()
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'reg.html',{'form':form})

def logoutUser(request):
    logout(request)
    return redirect('login')

class Info(DeleteView):
    def get(self,request,post_id):
        try:
            post = Post.objects.get(id = post_id)
            art = Article.objects.filter(post_article = post).order_by('-time_article')
            form = CreateArt()
        except:
            raise Http404("Статья не найдена(")
        context={
            'post':post,
            'form':form,
            'art':art
        }
        return render(request, 'info.html',context)

    def post(self,request,post_id):
        user = request.user
        post = Post.objects.get(id = post_id)
        form=CreateArt(request.POST)
        if form.is_valid():
            new_art = form.save(commit=False)
            new_art.auth_article = user
            new_art.post_article = post
            new_art.save()
            return redirect('base')
        


class AllPost(DeleteView):
    def get(self,request,*args, **kwargs):
        post = Post.objects.all().order_by('-time')
        context={
            'post':post
        }
        return render(request, 'all.html',context)

class Create(DeleteView):
    def get(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
             return render(request, 'errorac.html')
        post = Post.objects.all()
        form = CreateForm()
        context={
            'form':form,
            'post':post
        }
        return render(request, 'createpost.html',context)
    def post(self,request,*args, **kwargs):
        user = request.user
        post = Post.objects.all()
        form=CreateForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.auth = user
            new_post.save()
            return redirect('base')
        return render(request, 'reg.html',{'form':form})

#likes)
class AddLike(View):
    def post(self, request, post_id, *args, **kwargs):
        post = Post.objects.get(id=post_id)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)
            

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next','info')
        return HttpResponseRedirect(next)

class AddLike2(View):
    def post(self, request, post_id, *args, **kwargs):
        post = Post.objects.get(id=post_id)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)
            

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next','all')
        return HttpResponseRedirect(next)

class AddLikeArt(View):
    def post(self, request, art_id, *args, **kwargs):
        art = Article.objects.get(id=art_id)

        is_like = False

        for like in art.likes_article.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            art.likes_article.add(request.user)
            

        if is_like:
            art.likes_article.remove(request.user)

        next = request.POST.get('next','info')
        return HttpResponseRedirect(next)

class AddLikeArt2(View):
    def post(self, request, art_id, *args, **kwargs):
        art = Article.objects.get(id=art_id)

        is_like = False

        for like in art.likes_article.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            art.likes_article.add(request.user)
            

        if is_like:
            art.likes_article.remove(request.user)

        next = request.POST.get('next','comment')
        return HttpResponseRedirect(next)