from django.contrib import admin
from .models import Chat, ChatMessage, Forum, ForumMessage, ForumTopic, University, UniversityCourse, User



admin.site.register(User)
admin.site.register(University)
admin.site.register(UniversityCourse)
admin.site.register(Chat)
admin.site.register(ChatMessage)
admin.site.register(ForumTopic)
admin.site.register(Forum)
admin.site.register(ForumMessage)
