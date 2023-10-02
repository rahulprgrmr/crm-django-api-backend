from django.db import models
import uuid
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, editable=False)

    class Meta:
        abstract = True


class Timestamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SoftDelete(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        abstract = True