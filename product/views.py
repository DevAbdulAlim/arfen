from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category,SubCategory, Product, ProductDetails
from django.utils.translation import activate
from django.conf import settings
from django.db.models import F

# Create your views here.
class CategoryListView(View):
    def get(self, request):
        # Get user's selected language
        user_language = request.session.get('django_language', settings.LANGUAGE_CODE)

        # Determine which columns to select based on language
        name_column = F('name_en')
        description_column = F('description_en')
        if user_language == 'ar':
           name_column = F('name_ar')
           description_column = F('description_ar')

        # Fetch products with appropriate columns based on language
        category_list = Category.objects.annotate(
            name=name_column,
            description = description_column
        ).values('id', 'name', 'description', 'image')

        # Set the selected language for this view
        activate(user_language)

        return render(request, 'product/categories.html', {'category_list': category_list, "MEDIA_URL":  settings.MEDIA_URL})



class ProductListView(View):
    def get(self, request, category_id):
        # Get user's selected language
        user_language = request.session.get('django_language', settings.LANGUAGE_CODE)

        # Determine which columns to select based on language
        name_column = F('name_en')
        description_column = F('description_en')
        if user_language == 'ar':
           name_column = F('name_ar')
           description_column = F('description_ar')

        # Fetch products with appropriate columns based on language
        product_list = Product.objects.filter(sub_category__category=category_id).annotate(
            name=name_column,
            description = description_column
        ).values('id', 'name', 'description', 'price')

        # Fetch Sub Categories
        sub_category_list = SubCategory.objects.filter(category_id=category_id)

        # Set the selected language for this view
        activate(user_language)

        return render(request, 'product/products.html', {'product_list': product_list, 'sub_category_list': sub_category_list})
    

class ProductFilterView(View):
    def get(self, request, category_id, sub_category_id):
         # Get user's selected language
        user_language = request.session.get('django_language', settings.LANGUAGE_CODE)

        # Determine which columns to select based on language
        name_column = F('name_en')
        description_column = F('description_en')
        if user_language == 'ar':
           name_column = F('name_ar')
           description_column = F('description_ar')

        # Fetch Sub Categories
        sub_category_list = SubCategory.objects.filter(category_id=category_id)

        # Fetch Products
        product_list = Product.objects.filter(sub_category_id=sub_category_id).annotate(
           name=name_column,
           description = description_column
        )


        
        # Set the selected language for this view
        activate(user_language)

        return render(request, 'product/products.html', {
            'sub_category_list': sub_category_list,
            'product_list': product_list
        })



class ProductDetailsView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        custom_property = get_object_or_404(ProductDetails, pk=1)
        custom_property_data = custom_property.data
        return render(request, 'product/product.html', {"product": product, "custom_property": custom_property_data})
