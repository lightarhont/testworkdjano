from django.contrib.auth.mixins import AccessMixin
from feed.models import PostUser
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail

class OwnerRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.id != kwargs['userid']:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

def mailbody(name, url):
    return '''
    Привет %s, так как ты подписчик, я отправляю тебе уведомление на электронную почту.
    Зайди как нибудь прочитай содержимое в посте %s
    ''' % (name, url)

def mailsend(request, slug):
    pu = PostUser.objects.filter(subs_id=request.user.id).all()
    l=[]
    for i in pu:
        l.append(i.subs_id)
    u = User.objects.filter(pk__in=l).all()
    
    url = reverse('post_detail_url', kwargs={'slug': slug})
    l=[]
    for i in u:
        body = mailbody(i.username, url)
        #send_mail(subject, body, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
    
    
    
    