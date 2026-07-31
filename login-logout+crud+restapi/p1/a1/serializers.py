# pyrefly: ignore [missing-import]
from rest_framework import serializers
# pyrefly: ignore [missing-import]
from .models import std

class seristd(serializers.ModelSerializer):
    class Meta:
        model=std
        fields="__all__"