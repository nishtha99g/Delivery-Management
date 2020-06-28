from django import forms
 
#PRODUCT_QUANTITY_CHOICES= [(i, str(i)) for i in range( 1,21)]

class CartAddProductForm(forms.Form):
    quantity=forms.IntegerField(
        #choices=PRODUCT_QUANTITY_CHOICES,
        #coerce= int
        widget=forms.NumberInput(attrs={'class': 'form-control text-center',
                                        'aria-describedby': 'button-addon1',
                                        'aria-label': 'Example text with button addon'   ,
                                        'placeholder': '',
                                        'value':'1',  
                                    }),
                                label='',                   
    )
    update=forms.BooleanField(initial=False, widget=forms.HiddenInput, required=False)
