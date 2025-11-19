from django.shortcuts import render,redirect

from django.views import View

from .models import Movie,IndusttryChoices,GenereChoices,ArtistChoices,LanguagesChoices,CertificateChoices

from .forms import Movieform

from django.db.models import Q

# Create your views here.

class HomeView(View):

    template= 'home.html'

    def get(self,request,*args,**kwargs):

        data={'page':'Home'}

        return render(request,self.template,context=data)
    
class MovieListView(View):

    template= 'movies/movie-list.html'

    def get (self,request,*args,**kwargs):

        query=request.GET.get('query')

        movies=Movie.objects.filter(active_status = True)

        if query :

            movies =movies.filter(Q(name__icontains=query)|
                                  Q(description__icontains=query)|
                                  Q(industry__name__icontains=query)|
                                  Q(certification__icontains=query)|
                                  Q(genre__name__icontains=query)|
                                  Q(artists__name__icontains=query)|
                                  Q(languages__name__icontains=query)|
                                  Q(tags__icontains=query)
                                  ).distinct()


        data={'page':'Movies','movies':movies,'query':query}

        return render (request,self.template, context=data)
    
# class MovieCreateView(View):

#     def get(self,request,*args,**kwargs):

#         industrychoices=IndusttryChoices

#         genrechoices=GenereChoices

#         artistchoices=ArtistChoices

#         languageschoices=LanguagesChoices

#         certificatechoices=CertificateChoices

#         data={'page':'Create Movie',
#               'industrychoices':IndusttryChoices,
#               'genrechoices':GenereChoices,
#               'artistchoices':ArtistChoices,
#               'languageschoices':LanguagesChoices,
#               'certificatechoices':CertificateChoices}



#         return render (request,'movies/movie-create.html',context=data)
    
#     def post(self,request,*args,**kwargs):

#         movie_data=request.POST

#         name=movie_data.get('name')

#         photo=request.FILES.get('photo')

#         description=movie_data.get('description')

#         release_date=movie_data.get('release_date')

#         runtime=movie_data.get('runtime')

#         certification=movie_data.get('certification')

#         industry = movie_data.get('industry')

#         languages = movie_data.get('languages')

#         genre = movie_data.get('genre')

#         artists = movie_data.get('artists')

#         video = movie_data.get('video')

#         tags = movie_data.get('tags')

#         # print(name,photo,description,release_date,runtime,certification,industry,languages,genre,artists,video,tags)
        
#         Movie.objects.create(name=name,
#                              photo=photo,
#                              description=description,
#                              release_date=release_date,
#                              industry=industry,
#                              runtime=runtime,
#                              certification=certification,
#                              genre=genre,
#                              artists=artists,
#                              video=video,
#                              tags=tags,
#                              languages=languages)





#         return redirect('movie-list')
    
class MovieCreateView(View):

    form_class = Movieform

    template= 'movies/movie-create.html'


    def get(self,request,*args,**kwargs):

        form=Movieform()

        data={'page':'Create Movie',
              'form':form
              }
        
        return render (request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        form = Movieform(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('movie-list')
        
        # print(form.errors)
        
        data={'form':form,'page':'Create Movie'}

        return render(request,self.template,context=data)
    

    # ...........................................Implimenting with id....................................................
    
# class MovieDetailView(View):

#         template='movies/movie-details.html'

#         def get(self,request,*args,**kwargs):

#             id=kwargs.get('id')

#             movie=Movie.objects.get(id=id)

#             data={'movie':movie,'page':movie.name}



#             return render(request,self.template,context=data)
        

class MovieDetailView(View):

        template='movies/movie-details.html'

        def get(self,request,*args,**kwargs):

            uuid=kwargs.get('uuid')

            movie=Movie.objects.get(uuid=uuid)

            data={'movie':movie,'page':movie.name}



            return render(request,self.template,context=data)
        
            
            # return redirect('movie-list')
    
class MovieEditView(View):

    form_class=Movieform

    template='movies/movie-edit.html'

    def get (self,request,*args,**kwargs) :

        uuid=kwargs.get('uuid')

        movie=Movie.objects.get(uuid=uuid)

        form=self.form_class(instance=movie)

        data={'form':form,'page': movie.name}

        return render (request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        uuid=kwargs.get('uuid')

        movie=Movie.objects.get(uuid=uuid)

        form=self.form_class(request.POST,request.FILES,instance=movie)

        if form.is_valid():

            form.save()

            return redirect('movie-details',uuid=uuid)
        
class MovieDeletedView(View):

    def  get(self,request,*args,**kwargs):

        uuid=kwargs.get('uuid')

        movie=Movie.objects.get(uuid=uuid)

        # hard delete = movie.delete()


        movie.active_status=False  #=soft delete

        movie.save()

        return redirect('movie-list')
        
         