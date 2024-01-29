from django.shortcuts import render,redirect
from .serializers import personserializer
from rest_framework import generics,status
from .models import person
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import messages


# Create your views here.




class registerView(generics.CreateAPIView):
    serializer_class = personserializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "register.html"

    def get(self, request):
        serializer = personserializer()
        return render(request, self.template_name, {"serializer": serializer})

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get("password")
            confirmpassword = serializer.validated_data.get("confirmpassword")
            username = serializer.validated_data.get("username")

            if person.objects.filter(username=username):
                messages.error(request, "Username already exists")
                return redirect("register")

            elif password != confirmpassword:
                messages.error(request, "password is not match")
                return redirect("register")

            serializer.save()
            return redirect("login")

        return render(request, self.template_name, {"serializer": serializer})   