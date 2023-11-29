from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from item.models import Items

from .forms import ConversationMessageForm
from .models import Conversation
# Create your views here.

@login_required
def new_conversation(request,item_pk):
    item = get_object_or_404(Items, pk = item_pk)

    if item.created_by == request.user:
        return redirect('deshboard:index')

    conversations = Conversation.objects.filter(item = item).filter(members__in = [request.user.id])

    

    #conversations between you and the vendor
    if conversations:
        return redirect('deshboard:detail', pk =conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item= item)
            conversation.members.add(request.user) #adding you
            conversation.members.add(item.created_by) #adding vendor
            conversation.save()

            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk = item.pk)
    else:
        form = ConversationMessageForm() #empty form

    return render(request, 'messaging/new.html',{
        'form':form
        }) 

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in= [request.user.id])

    return render(request, 'messaging/inbox.html', {
        'conversations':conversations
        })

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in= [request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit= False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('messaging:detail', pk = pk)
    else:
        form = ConversationMessageForm()

    return render(request,'messaging/detail.html',{
        'form':form,
        'conversation':conversation
    })

# @login_required
# def new_conversation(request, item_pk):
#     item = get_object_or_404(Items, pk=item_pk)

#     if item.created_by == request.user:
#         return redirect('deshboard:index')

#     conversations = Conversation.objects.filter(item=item, members=request.user)

#     # Conversations between you and the vendor
#     if conversations:
#         return redirect('deshboard:detail', pk=conversations.first().id)

#     if request.method == 'POST':
#         form = ConversationMessageForm(request.POST)

#         if form.is_valid():
#             conversation = Conversation.objects.create(item=item)
#             conversation.members.add(request.user)  # adding you
#             conversation.members.add(item.created_by)  # adding vendor
#             conversation.save()

#             conversation_message = form.save(commit=False)
#             conversation_message.conversation = conversation
#             conversation_message.created_by = request.user
#             conversation_message.save()

#             return redirect('item:detail', pk=item.pk)
#     else:
#         form = ConversationMessageForm()

#     return render(request, 'messaging/new.html', {'form': form})

# @login_required
# def inbox(request):
#     conversations = Conversation.objects.filter(members=request.user)

#     return render(request, 'messaging/inbox.html', {'conversations': conversations})

# @login_required
# def detail(request, pk):
#     conversation = Conversation.objects.filter(members=request.user, pk=pk).first()

#     if not conversation:
#         # Handle the case where the conversation doesn't exist or the user doesn't have access
#         return HttpResponse("Conversation not found or you don't have access.")

#     if request.method == 'POST':
#         form = ConversationMessageForm(request.POST)

#         if form.is_valid():
#             conversation_message = form.save(commit=False)
#             conversation_message.conversation = conversation
#             conversation_message.created_by = request.user
#             conversation_message.save()

#             return redirect('messaging:detail', pk=pk)
#     else:
#         form = ConversationMessageForm()

#     return render(request, 'messaging/detail.html', {'form': form, 'conversation': conversation})
