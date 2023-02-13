from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from empresa.models import Vagas
from django.contrib import messages
from django.contrib.messages import constants
from .models import Tarefa, Emails
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def nova_vaga(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        email = request.POST.get('email')
        tecnologias_domina = request.POST.getlist('tecnologias_domina')
        tecnologias_nao_domina = request.POST.getlist('tecnologias_nao_domina')
        experiencia = request.POST.get('experiencia')
        data_final = request.POST.get('data_final')
        empresa = request.POST.get('empresa')
        status = request.POST.get('status')


        if len(titulo.strip()) == 0 or len(email.strip()) == 0 or len(tecnologias_domina.strip()) == 0 or len(tecnologias_nao_domina.strip()) == 0 or len(experiencia.strip()) == 0 or len(data_final.strip()) == 0 or len(empresa.strip()) == 0 or len(status.strip()) == 0: 
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/home/empresa/')

        vaga = Vagas(
                    titulo=titulo,
                    email=email,
                    nivel_experiencia=experiencia,
                    data_final=data_final,
                    empresa_id=empresa,
                    status=status,
        )


        vaga.save()

        vaga.tecnologias_estudar.add(*tecnologias_nao_domina)
        vaga.tecnologias_dominadas.add(*tecnologias_domina)

        vaga.save()
        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        return redirect(f'/home/empresa/{empresa}')
    elif request.method == "GET":
        raise Http404()

def vaga(request, id):
    vaga = get_object_or_404(Vagas, id=id)
    tarefas = Tarefa.objects.filter(vaga=vaga).filter(realizada=False)
    emails = Emails.objects.filter(vaga=vaga)
    return render(request, 'vaga.html', {'vaga': vaga, 'tarefas': tarefas, 'emails': emails})

def nova_tarefa(request, id_vaga):
    titulo = request.POST.get('titulo')
    prioridade = request.POST.get("prioridade")
    data = request.POST.get('data')
    
    try:
        tarefa = Tarefa(vaga_id=id_vaga,
                        titulo=titulo,
                        prioridade=prioridade,
                        data=data)
        tarefa.save()
        messages.add_message(request, constants.SUCCESS, 'Tarefa criada com sucesso')
        return redirect(f'/vagas/vaga/{id_vaga}')
    except: 
        messages.add_message(request, constants.ERROR, 'Erro interno no sistema')
        return redirect(f'/vagas/vaga/{id_vaga}')
    
    
def realizar_tarefa(request, id):
    tarefa_list = Tarefa.objects.filter(id=id).filter(realizada=False)
    
    if not tarefa_list.exists():
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
        return redirect(f'/home/empresas/')
    
    tarefa = tarefa_list.first()
    tarefa.realizada = True
    tarefa.save()    
    messages.add_message(request, constants.SUCCESS, 'Tarefa realizada com sucesso, parabéns!')
    return redirect(f'/vagas/vaga/{tarefa.vaga.id}')

def envia_email(request, id_vaga):
    vaga = Vagas.objects.get(id=id_vaga)
    assunto = request.POST.get('assunto')
    corpo = request.POST.get('corpo')
    
    html_content = render_to_string('emails/template_email.html', {'corpo': corpo})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, [vaga.email, 'kaikerocha350@gmail.com'])
    email.attach_alternative(html_content, 'text/html')
    
    if email.send():
        mail = Emails(
            vaga=vaga,
            assunto=assunto,
            corpo=corpo,
            enviado=True
        )
        mail.save()
        messages.add_message(request, constants.SUCCESS, 'Email enviado com sucesso')
        return redirect(f'/vagas/vaga/{id_vaga}')
    else:
        mail = Emails(
            vaga=vaga,
            assunto=assunto,
            corpo=corpo,
            enviado=False
        )
        mail.save()
        messages.add_message(request, constants.ERROR, 'Não conseguimos enviar o seu email')
        return redirect(f'/vagas/vaga/{id_vaga}')
    
def tecnologia_status(request, id_vaga):
    if request.method == 'POST':
        vaga = get_object_or_404(Vagas, id=id_vaga)

        try:
            tecnologia1 = request.POST.get('tecnologia_dominada')
            tecnologia2 = request.POST.get('tecnologia_estudar')

            if tecnologia1:
                vaga.tecnologias_dominadas.remove(tecnologia1)
                vaga.tecnologias_estudar.add(tecnologia1)
                vaga.save()

            if tecnologia2:
                vaga.tecnologias_estudar.remove(tecnologia2)
                vaga.tecnologias_dominadas.add(tecnologia2)
                vaga.save()

            return redirect(f'/vagas/vaga/{id_vaga}#tecnologias')

        except:
            messages.add_message(
                request,
                constants.ERROR,
                message='Erro ao realizar a operação.'
            )
            return redirect(f'/vagas/vaga/{id_vaga}')

    raise Http404()