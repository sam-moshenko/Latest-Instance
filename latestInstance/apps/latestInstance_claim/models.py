from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Node(MPTTModel):
    text = models.TextField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.deletion.CASCADE)
    argument = models.BooleanField(default=False)
    class MPTTMeta:
        order_insertion_by = ['text']
    def __str__(self):
        return self.text
