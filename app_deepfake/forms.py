from django import forms
from .models import Deepfake


class DeepfakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["video"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["model"].widget.attrs["class"] = "form-control form-control-lg"

    class Meta:
        model = Deepfake
        fields = ["video", "model"]
