from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,DetailView,ListView
from django.contrib.auth.models import User
import io
from reportlab.pdfgen import canvas
from easy_pdf.views import PDFTemplateView

from .forms import SignUpForm,SlamForm
from .models import SlamBook

# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    slams = SlamBook.objects.filter(being_written_to=user)
    context = {'user':user,'slams':slams}
    return render(request,'slam/dashboard.html',context)

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()

        args = {'form':form}
        return render(request,'slam/signup.html',args)

def slambook(request,user_name):
    uname = User.objects.get(username=user_name)
    if request.method=='POST':
        form = SlamForm(request.POST)
        if form.is_valid():
            slam = form.save(commit=False)
            slam.being_written_to = uname
            slam.save()
            return redirect('/slambook_submit_success/')
    else:
        form = SlamForm()

        args = {'form':form,'user_name':uname}
        return render(request,'slam/write_slam.html',args)

def slambook_submit_success(request):
    return render(request,'slam/slam_submit_success.html',{})

def view_slam(request,slam_id):
    user = request.user
    slam = SlamBook.objects.get(id=slam_id)
    context = {'user':user,'slam':slam}
    return render(request,'slam/view_slam.html',context)

class GeneratePDFView(PDFTemplateView,ListView):
    model = SlamBook()
    template_name = 'slam/generate_pdf.html'
    def get_context_data(self, **kwargs):
        c = super(GeneratePDFView, self).get_context_data(**kwargs)
        u = self.request.user
        c['slam_book'] = SlamBook.objects.filter(being_written_to=u)
        return c

    def get_queryset(self):
        data = model.objects.filter(being_written_to=self.request.user)

def generate_pdf(request):
    return render(request,'slam/generate_pdf.html',{})

def profile(request):
    user = request.user
    u = User.objects.get(id = user.id)
    context = {'user':u}
    return render(request,'slam/profile.html',context)