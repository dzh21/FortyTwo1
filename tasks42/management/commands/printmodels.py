from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Print models and objects count'

    def handle(self, *args, **options):
        for ct in ContentType.objects.all():
            m = ct.model_class()
            self.stdout.write("%s.%s\t%d" % (m.__module__, m.__name__, m._default_manager.count()))
            self.stderr.write("error: %s.%s\t%d" % (m.__module__, m.__name__, m._default_manager.count()))