from grpc import Status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Categort,Cart,CartItem
from .serializers import CadSerializer, ProductSerializer, CategorySerializer

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_categories(request):
    categories = Categort.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        # Passing context ensures absolute media paths are generated for the images
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'message': 'Product not found'}, status=Status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_cart(requrest):
    cart, careated= Cart.objects.get_or_create(user=requrest.user)
    serializer=CadSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    product_id=request.data.get("prodect_id")
    product=Product.objects.get(id=product_id)

    cart,created=Cart.objects.get_or_create(user=request.user if request.user.is_authenticated else None)
    item,item_created=CartItem.objects.get_or_create(cart=cart,product=product)
  
    if not item_created:
        item.quantity +=1
        item.save()

    serializer=CadSerializer(cart)
    return Response({"message":"prodect added to cart ","cart":serializer.data})


@api_view(['POST'])
def remove_from_cart(request):
    item_id = request.data.get('item_id')
    CartItem.objects.filter(id=item_id).delete()
    return Response({"message": "Item removed from cart"})