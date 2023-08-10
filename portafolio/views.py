from django.shortcuts import render, redirect
from .models import *
from .forms import CustomContactForm
from django.contrib import messages
from django.core.mail import send_mail

# podrias separar la vista en varias, en este caso realizo todo en una vista
# renderizo mi perfil, mis proyectos, y establezco la logica de los correos.
def index(request):
    perfil = Profile.objects.first()
    proyectos = Proyecto.objects.all()

    if request.method == 'POST':
        form = CustomContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado con éxito.')

            name = form.cleaned_data['name']

            # Obtén el email del remitente del formulario
            from_email = form.cleaned_data['email']

            # Lista de destinatarios (tu dirección de correo electrónico)
            recipient_list = ['contact@tudominio.com']

            # Asunto del correo
            subject = form.cleaned_data['subject']

            # Cuerpo del correo
            message = f"Nombre: {name}\nCorreo Electrónico: {from_email}\nMensaje: {form.cleaned_data['message']}"

            # Envía el correo
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return redirect('/')
        else:
            messages.error(request, 'Ocurrió un error. Por favor, verifica los campos.')
    else:
        form = CustomContactForm()

    return render(request, 'index.html', {'perfil': perfil, 'proyectos': proyectos, 'form': form})

