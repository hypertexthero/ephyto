# http://superjared.com/projects/static-generator/
from django.contrib.flatpages.models import FlatPage
# from blog.models import Post
from django.db.models import signals
from staticgenerator import quick_delete
from django.contrib.comments.models import Comment, FreeComment

def delete_index(sender, instance):
    quick_delete(instance, '/')

# signals.post_delete.connect(delete_index, sender=Post)
signals.post_delete.connect(delete_index, sender=FlatPage)
# signals.post_save.connect(publish_flatpage, sender=FlatPage)

def publish_comment(sender, instance):
    quick_delete(instance.get_content_object())

signals.post_save.connect(publish_comment, sender=Comment)
signals.post_save.connect(publish_comment, sender=FreeComment)

# TODO: file uploads