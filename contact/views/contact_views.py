from django.shortcuts import get_object_or_404, render

from contact.models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('id')[10:20]
    # print(contacts.query)
    site_title = "Contatos"
    context = {
        'contacts': contacts,
        'site_title': site_title
    }
    template = "contact/index.html"
    return render(request, template, context)

def contact(request, contact_id: int):
    single_contact = get_object_or_404(
        Contact, 
        pk=contact_id,
        show=True
        )
    site_title = f"{single_contact.first_name} {single_contact.last_name}"
    context = {
        'contact': single_contact,
        'site_title': site_title
    }
    template = "contact/contact.html"
    return render(request, template, context)