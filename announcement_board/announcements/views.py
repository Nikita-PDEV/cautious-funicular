from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.shortcuts import render, redirect, get_object_or_404  
from .models import Announcement, Reply  
from .forms import AnnouncementForm, ReplyForm  

class AnnouncementListView(LoginRequiredMixin, View):  
    def get(self, request):  
        category = request.GET.get('category')  
        if category:  
            announcements = Announcement.objects.filter(category=category)  
        else:  
            announcements = Announcement.objects.all()  
        return render(request, 'announcements/list.html', {'announcements': announcements})  

class AnnouncementDetailView(LoginRequiredMixin, View):  
    def get(self, request, pk):  
        announcement = get_object_or_404(Announcement, pk=pk)  
        reply_form = ReplyForm()  
        return render(request, 'announcements/detail.html', {'announcement': announcement, 'reply_form': reply_form})  

    def post(self, request, pk):  
        announcement = get_object_or_404(Announcement, pk=pk)  
        reply_form = ReplyForm(request.POST)  
        if reply_form.is_valid():  
            reply = reply_form.save(commit=False)  
            reply.user = request.user  
            reply.announcement = announcement  
            reply.save()  
            # Отправка email уведомления пользователю, оставившему отклик  
            return redirect('announcement_detail', pk=pk)  
        return render(request, 'announcements/detail.html', {'announcement': announcement, 'reply_form': reply_form})  

class AnnouncementCreateView(LoginRequiredMixin, View):  
    def get(self, request):  
        form = AnnouncementForm()  
        return render(request, 'announcements/create.html', {'form': form})  

    def post(self, request):  
        form = AnnouncementForm(request.POST)  
        if form.is_valid():  
            announcement = form.save(commit=False)  
            announcement.user = request.user  
            announcement.save()  
            return redirect('announcement_list')  
        return render(request, 'announcements/create.html', {'form': form})  

class AnnouncementUpdateView(LoginRequiredMixin, View):  
    def get(self, request, pk):  
        announcement = get_object_or_404(Announcement, pk=pk, user=request.user)  
        form = AnnouncementForm(instance=announcement)  
        return render(request, 'announcements/update.html', {'form': form, 'announcement': announcement})  

    def post(self, request, pk):  
        announcement = get_object_or_404(Announcement, pk=pk, user=request.user)  
        form = AnnouncementForm(request.POST, instance=announcement)  
        if form.is_valid():  
            form.save()  
            return redirect('announcement_detail', pk=pk)  
        return render(request, 'announcements/update.html', {'form': form, 'announcement': announcement})  

class ReplyListView(LoginRequiredMixin, View):  
    def get(self, request):  
        replies = Reply.objects.filter(announcement__user=request.user)  
        return render(request, 'announcements/reply_list.html', {'replies': replies})  

    def post(self, request, pk):  
        reply = get_object_or_404(Reply, pk=pk, announcement__user=request.user)  
        if 'accept' in request.POST:  
            reply.is_accepted = True  
            reply.save()  
            # Отправка email уведомления пользователю, оставившему принятый отклик  
        elif 'reject' in request.POST:  
            reply.delete()  
        return redirect('reply_list')