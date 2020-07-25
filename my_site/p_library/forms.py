from django import forms
from p_library.models import Author, Book, BorrowBook, Friend

class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)
#    required_css_class = 'list-group-item'
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('friend',)

class BorrowBookFormGive(forms.ModelForm):
    class Meta:
        model = BorrowBook
        fields = ['book', 'friend','borrow_date',
        'state_before']
        widgets = {
            'borrow_date': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date','placeholder':'mm/dd/yyyy' }),
            'state_before': forms.TextInput(),
        }

class BorrowBookFormBack(forms.ModelForm):
    class Meta:
        model = BorrowBook
        fields = '__all__'

class BorrowBookFormReturn(forms.Form):
    return_date = forms.DateField(required=True, label="Дата возврата", widget=forms.DateInput(format='%m/%d/%Y',attrs={'type':'date','placeholder':'yyyy-mm-dd' }))
    state_after = forms.CharField(required=True, label="Состояние книги")
    returned_flad = forms.BooleanField(initial=True, required=True)
    class Meta:
        pass

class FriendFormAdd(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Friend
        fields = '__all__'

BorrowBookFormSet = forms.modelformset_factory(BorrowBook, fields=('book','friend','borrow_date'),
        widgets={'borrow_date':forms.TextInput()})