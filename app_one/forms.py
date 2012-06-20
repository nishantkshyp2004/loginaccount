from django.forms import ModelForm
from app_one.models import FileUpload

class FileUploadForm(ModelForm):
    class Meta:
        model=FileUpload