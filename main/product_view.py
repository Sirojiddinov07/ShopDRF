
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Product, Review, Image, Category, Subcategory
from .serializers import ProductSerializer, ImageSerializer, CategorySerializer, SubcategorySerializer

from rest_framework import status, generics


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000



class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination


@api_view(['GET'])
def searchProducts(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''

    products = Product.objects.filter(
        name__icontains=query).order_by('-createdAt')
    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data} )




@api_view(['GET'])
def getTopProducts(request):
    products = Product.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    data = request.data

    product = Product.objects.create(
        name=data['name'],
        price=data['price'],
        color=data['color'],
        countInStock=data['countInStock'],
        category=data['category'],
        description=data['description'],
        extra_info=data['extra_info'],
        rating=data['rating'],

    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(id=pk)

    product.name = data['name']
    product.price = data['price']
    product.brand = data['brand']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)




@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Producted Deleted')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProductReview(request, pk):
    user = request.user
    product = Product.objects.get(_id=pk)
    data = request.data

    # 1 - Review already exists
    alreadyExists = product.review_set.filter(user=user).exists()
    if alreadyExists:
        content = {'detail': 'Product already reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 2 - No Rating or 0
    elif data['rating'] == 0:
        content = {'detail': 'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 3 - Create review
    else:
        review = Review.objects.create(
            user=user,
            product=product,
            name=user.first_name,
            rating=data['rating'],
            comment=data['comment'],
        )

        reviews = product.review_set.all()
        product.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        product.rating = total / len(reviews)
        product.save()

        return Response('Review Added')



@api_view(['PUT'])
@permission_classes([IsAdminUser])
def add_img(request):
    data = request.data
    img = Image.objects.create(
        img=data['img']
    )

    serializer = ImageSerializer(img, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteImage(request, pk):
    img = Image.objects.get(id=pk)
    img.delete()
    return Response('Image Deleted')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cat(request):
    cat = Category.objects.all()
    serializer = CategorySerializer(cat, many=True)
    return Response(serializer.data)




@api_view(['PUT'])
@permission_classes([IsAdminUser])
def add_cat(request):
    data = request.data
    cat = Category.objects.create(
        img=data['img'],
        name=data['name'],
        subcategory=data['subcategory'],
    )

    serializer = CategorySerializer(cat, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCat(request, pk):
    cat = Category.objects.get(id=pk)
    cat.delete()
    return Response('Category Deleted')



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sub(request):
    sub = Subcategory.objects.all()
    serializer = CategorySerializer(sub, many=True)
    return Response(serializer.data)




@api_view(['PUT'])
@permission_classes([IsAdminUser])
def addSubcat(request):
    data = request.data
    cat = Subcategory.objects.create(
        img=data['img'],
        name=data['name'],
    )

    serializer = SubcategorySerializer(cat, many=False)
    return Response(serializer.data)




@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteSubcat(request, pk):
    subcat = Subcategory.objects.get(id=pk)
    subcat.delete()
    return Response('Subcategory Deleted')
