from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .apps import PredictorConfig
from .form import DocumentForm
from .models import Document
from .metadata import getmetadata
import warnings
from .predictor import predict_gen
from django.contrib import messages
warnings.simplefilter('ignore')


def Work(request):
    return render(request,'music/Work.html')


def model_form_upload(request):

    documents = Document.objects.all()
    if request.method == 'POST':
        if len(request.FILES) == 0:
            messages.error(request,'Upload a file')
            return redirect("predictor:Work")

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploadfile = request.FILES['document']
            print(uploadfile.name)
            print(uploadfile.size)
            if not uploadfile.name.endswith('.wav'):
                messages.error(request,'Only .wav file type is allowed')
                return redirect("predictor:Work")
            meta = getmetadata(uploadfile)
            
            genre = predict_gen(meta)
            print(genre)

            context = {'genre':genre}
            return render(request,'music/result.html',context)

    else:
        form = DocumentForm()

    return render(request,'music/result.html',{'documents':documents,'form':form})