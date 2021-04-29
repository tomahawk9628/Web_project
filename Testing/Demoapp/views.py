from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .forms import Imageform,CreationUserForm,Movieform,Reviewform,ImageCh
from .forms import Adminform
from .models import Video,AdminLogin,Movie,Review,Check
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from .decorators import unauthenticated_user,allowed_users
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import TemporaryUploadedFile
from io import BytesIO
import pandas as pd
import numpy as np
from tensorflow import keras
from keras.preprocessing import image


# Create your views here.
def hi(request):

       

 return HttpResponse("Hello, world. 4f97b077 is the polls index.")






def hel(request):
  print("it is working")
  form = UserCreationForm()
  if request.method == "POST":
          form = UserCreationForm(request.POST)
          username =  request.POST['username']
          password = request.POST['password']
          print(username+" "+password)  
          context={'username':username,}
          if form.is_valid():
              print(" second if working")
              form.save()
          return redirect('/')
  else:  
      print("else")
      form=UserCreationForm()
  print(form.errors)
  return render(request,'Demoapp//test.html',{'form':form})


#def login(request):
 #   print("In snd ")
 #   if request.method == "POST":
 #        form = UserCreationForm(request.POST)
 #        uname =  request.POST['username']
 #        password = request.POST['password']
 #        print(uname+" "+password)  
 #        context={'uname':uname,}
 #        if form.is_valid():
 #           print(" second if working")
 #           form.save()
 #        return redirect('/')
 #   else:
 #     form = UserCreationform()  
 #     print("else")
 #   print(form.errors)
 #   return render(request, 'Demoapp//logintest.html',context)




def post_list(request):
    return render(request, 'blog/post_list.html', {uname})

def disp(request,*args, **kwargs):
    image = Video.objects.only('image')
    video = Video.objects.only('video')
    print("disp func")
    if request.method == "POST":
        print("If")
        form = Imageform(request.POST,request.FILES)
        if form.is_valid():
         print(" second ifworking")
         form.save()
         return redirect('/')
    else:
        form = Imageform()  
        print("else")   
    context={
      'form':form,
      'image':image,
      'video':video,
    }
    print(form.errors)
    return render(request,'Demoapp//index.html',context)
    

def home(request):
  return render(request,'Demoapp//Website//main.html')

@unauthenticated_user
def login_url(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect('dashboard')
    else:
        messages.info(request,'Username Or Password Incorrect')
        return render(request,'registration//login.html',{})
  return render(request,'registration//login.html',{})






@unauthenticated_user
def register(request):
  if request.method == "POST":
      form = CreationUserForm(request.POST)
      if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        emailf = form.cleaned_data.get('email')
        frm = settings.EMAIL_HOST_USER
        email = EmailMessage(
        subject = 'REGISTRATION TO MOVIE MAGIC IS SUCCESSFULL',
        body = 'HELLO '+user+', WELCOME TO MOVIE MAGIC HAVE A GREAT TIME WATCHING MOVIES FOR FREE',
        from_email = frm,
        to = [emailf],
         )
        email.send()
        messages.success(request,"You have been successfully registered")
        if email.send():
           return redirect('login_url')
  else:
      form = CreationUserForm()
  return render(request,'registration//register.html',{'form':form})

@login_required(login_url='login_url')
def dashboardView(request):
  movieob = Movie.objects.exclude(image__isnull=True)
  # movieob = Movie.objects.all()[:20]
  context={
      #'form':form,
      #'movie':movie,
      #'image':image,
#'video':video,
      'movieob':movieob,
      #'title':title,
    }  
  return render(request,'dashboard.html',context)


def adlog(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    uname = AdminLogin.objects.only('uname')[0].uname
    passw = AdminLogin.objects.only("password")[0].password
    print(uname)
    print(passw)
    if (username==uname)and(password==passw):
        return redirect('adminl')
    else:
        messages.error(request, 'Incorrect Username Or Password.')
    #if user is not None:
     #   login(request,user)
     #   return redirect('adminl')
  else:
        messages.info(request,'Username Or Password Incorrect')
        return render(request,'Demoapp//adlogin.html',{})
  return render(request,'Demoapp//adlogin.html',{})


# def adminl(request):
#     form = Movieform()
#     review = Review.objects.all()
#     movie = Movie.objects.all()
#     video = Movie.objects.only('video')
#     movieob = Movie.objects.exclude(image__isnull=True)
#     movieob1 = Movieform()
#     #image = Movie.objects.only('image')
#     #title = Movie.objects.only('title')
#     #print(title)
#     movieid = request.POST.get('movieId')
#     print("disp func")
   
#     if request.method=='POST'and 'add' in request.POST:     
#          form = Movieform(request.POST,request.FILES)
#          print("elif")
#          print(form.errors)
#          if form.is_valid():
#               movieob.movieId = request.POST.get('movieId')
#               movieob.title = request.POST.get('title')
#               movieob.genres = request.POST.get('genres')
#               movieob.imdbId = request.POST.get('imdbId')
#               movieob.average = request.POST.get('average')
#               movieob.description = request.POST.get('description')
#               movieob.image = request.POST.get('image')
#               movieob.video = request.POST.get('video')
#               print("elifworking")
#               form.save()
#               messages.success(request, 'Sucesfully added to database.')
         
           
#     elif request.method=='POST'and 'check' in request.POST:     
#            mid = request.POST.get('movieId1')
#            print(mid)
#            movieob1 = get_object_or_404(Movie,movieId = mid)
#            print(movieob1)
           
           

#     elif request.method=='POST'and 'update' in request.POST:     
#            mid = request.POST.get('movieId1')
#            print(mid)
#            movieob2 = get_object_or_404(Movie,movieId = mid)
#            print(movieob1)
#            form = Movieform(request.POST,request.FILES)
#            print(form.errors)
#            if form.is_valid():
#                movieob2.title = request.POST.get('title')
#                movieob2.genres = request.POST.get('genres')
#                movieob2.imdbId = request.POST.get('imdbId')
#                movieob2.average = request.POST.get('average')
#                movieob2.description = request.POST.get('description')
#                movieob2.image = request.POST.get('image')
#                movieob2.video = request.POST.get('video')
#                form.save()
           

         

#     elif request.method=='POST'and 'delete' in request.POST:     
#            mid = request.POST.get('movieId1')
#            print(mid)
#            movieob1 = get_object_or_404(Movie,movieId = mid)
#            print(movieob1)
#            movieob1.delete
           

     
          
           
#     else:
#         form = Movieform()  
#         print("else") 
    
#     context={
#       'form':form,
#       'movie':movie,
#       #'image':image,
#       'video':video,
#       'movieob':movieob,
#       #'title':title,
#       'review':review,
#       'movieob1':movieob1,
#     }
#     print(form.errors)
#     return render(request,'Demoapp//admin.html',context)

def adminl(request):
    review = Review.objects.all()
    movie = Movie.objects.all()
    video = Movie.objects.only('video')
    movieob = Movie.objects.exclude(image__isnull=True)
    #image = Movie.objects.only('image')
    #title = Movie.objects.only('title')
    #print(title)
    movieid = request.POST.get('movieId')
    print("disp func")
   
    if request.method=='POST'and 'submit' in request.POST:     
         form = Movieform(request.POST,request.FILES)
         print("elif")
         print(form.errors)
         if form.is_valid():
              movieob.movieId = request.POST.get('movieId')
              movieob.title = request.POST.get('title')
              movieob.genres = request.POST.get('genres')
              movieob.imdbId = request.POST.get('imdbId')
              movieob.average = request.POST.get('average')
              movieob.description = request.POST.get('description')
              movieob.image = request.POST.get('image')
              movieob.video = request.POST.get('video')
              print("elifworking")
              form.save()
         return render(request,'Demoapp//admin.html')

    else:
        form = Movieform()  
        print("else") 
    
    context={
      'form':form,
      'movie':movie,
      #'image':image,
      'video':video,
      'movieob':movieob,
      #'title':title,
      'review':review
    }
    print(form.errors)
    return render(request,'Demoapp//admin.html',context)
  



def dummy(request):
   image = Video.objects.all()
   
   print("disp func")
   if request.method == "POST":
        print("If")
        form = Imageform(request.POST,request.FILES)
        if form.is_valid():
            print(" second ifworking")
            form.save()
            return redirect('/')
   else:
         form = Imageform()  
         print("else")   
   context={
      'form':form,
      'image':image,
      
    }
   print(form.errors)
   return render(request,'Demoapp//Website//dashboard.html',context)


@login_required(login_url='login_url')
def mdetails(request,movie_id):
  movie = get_object_or_404(Movie,movieId = movie_id)
  # print(get_ds(movie.title))
  title1 = movie.title.replace(".s", "'s")
  rec = get_ds(title1)
  if len(rec) == 0:
      context={
          'movie': movie,
      }
  else:
    m1 = Movie.objects.get(title__exact=rec[0].replace("'s", ".s"))
    m2 = Movie.objects.get(title__exact=rec[1].replace("'s", ".s"))
    m3 = Movie.objects.get(title__exact=rec[2].replace("'s", ".s"))
    m4 = Movie.objects.get(title__exact=rec[3].replace("'s", ".s"))
    m5 = Movie.objects.get(title__exact=rec[4].replace("'s", ".s"))
    context={
        'movie':movie,
        'm1': m1,
        'm2': m2,
        'm3': m3,
        'm4': m4,
        'm5': m5,
  }
  return render(request,"details1.html",context)


def about(request):
 return render(request,"about.html")

def contact(request):
 form = Reviewform()
 if request.method == "POST":
        print("If")
        form = Reviewform(request.POST)
        print(form.errors)
        if form.is_valid():
            print(" second ifworking")
            form.save()
 else:
      form = Reviewform()  
      print("else")  
 context={
   'form':form,
  }
 return render(request,"contact.html",context)


def get_ds(mt):
    #column_names = ['userId', 'movieId', 'rating', 'timestamp']
    ds = pd.read_csv('C:/Web/Testing/ratings.csv')
    ds.head()
    movie_titles = pd.read_csv('C:/Web/Testing//movies.csv')
    #print(movie_titles)
    global ratings
    df = pd.merge(ds,movie_titles, on='movieId')
    df.head()
    df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
    df.groupby('title')['rating'].count().sort_values(ascending=False).head()
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings.head()
    ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
    ratings.head()
    global moviemat
    moviemat=df.pivot_table(index='userId',columns='title',values='rating')
    ratings.sort_values('num of ratings',ascending=False).head(10)
    ratings.head()
    user_ratings = moviemat[mt]
    liarliar_user_ratings = moviemat['Liar Liar (1997)']
    user_ratings.head()
    similar_to = moviemat.corrwith(user_ratings)
    similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)
    corr_starwars = pd.DataFrame(similar_to,columns=['Correlation'])
    corr_starwars.dropna(inplace=True)
    corr_starwars.head()
    corr_starwars.sort_values('Correlation',ascending=False).head(10)
    corr_starwars = corr_starwars.join(ratings['num of ratings'])
    corr_starwars.head()
    rec=corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()
    rec1 = rec.iloc[:, 1]
    index_slice = rec1.index
    mv_list = index_slice.to_list()
    return mv_list




#def create_training_data(Dir,Cat):
  
def search(request):
  if request.method == "POST":
    smovie = request.POST.get('smovies')
    print(smovie)
  movieob = Movie.objects.filter(title__icontains=smovie).exclude(image__isnull=True)
  movieob2 = Movie.objects.filter(genres__icontains=smovie).exclude(image__isnull=True)
  # movieob = Movie.objects.all()[:20]
  context={
      #'form':form,
      #'movie':movie,
      #'image':image,
      #'video':video,
      'movieob2' :movieob2,
      'movieob':movieob,
      #'title':title,
    }  
  return render(request,'search.html',context)


@csrf_exempt
def mlmodel(request):
    if request.method == "POST":
      
      path = TemporaryUploadedFile.temporary_file_path(self=request.FILES['imagecheck'])
      print(path)
      classifier = keras.models.load_model('D:/Code/Practice/Django/Web/model') #Point to the folder where the saved_model is stored
      test_image = image.load_img(path, target_size = (224, 224))
      test_image = image.img_to_array(test_image)
      test_image = np.expand_dims(test_image, axis = 0)
      result = classifier.predict(test_image)
      # training_set.class_indices
      if result[0][0] == 1:
        prediction = 'Non Animation'
      else:
        prediction = 'Animation'
      print(prediction)
      print(result)

    return render(request, 'dashboard.html')


def check(request):
  if request.method == "POST":
    form = ImageCh(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    else:
      print(form.errors)  
  return render(request, "check.html")