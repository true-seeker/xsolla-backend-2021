import graphene

'''Создание типов GraphQL для существующих моделей данных'''
from graphene_django.types import DjangoObjectType, ObjectType
from main_app.models import Product, ProductType


class ProductGraphQLType(DjangoObjectType):
    """Type продукт"""

    class Meta:
        model = Product


class ProductTypeGraphQLType(DjangoObjectType):
    """Type тип продукта"""

    class Meta:
        model = ProductType


class Query(ObjectType):
    """Резолверы запросов"""
    product = graphene.Field(ProductGraphQLType, id=graphene.Int())
    product_type = graphene.Field(ProductTypeGraphQLType, id=graphene.Int())

    products = graphene.List(ProductGraphQLType)
    product_types = graphene.List(ProductTypeGraphQLType)

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Product.objects.get(pk=id)
        return None

    def resolve_product_type(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return ProductType.objects.get(pk=id)
        return None

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_product_types(self, info, **kwargs):
        return ProductType.objects.all()


class ProductInput(graphene.InputObjectType):
    """Определяем данные, которые можно изменять для продукта"""
    id = graphene.ID()
    stock_keeping_unit = graphene.String()
    title = graphene.String()
    product_type = graphene.Field(lambda: ProductTypeInput)
    price = graphene.Float()


class ProductTypeInput(graphene.InputObjectType):
    """Определяем данные, которые можно изменять для типа продукта"""
    id = graphene.ID()
    title = graphene.String()


class CreateProduct(graphene.Mutation):
    """Мутация создания продукта"""

    class Arguments:
        input = ProductInput(required=True)

    ok = graphene.Boolean()
    product = graphene.Field(ProductGraphQLType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        product_instance = Product(stock_keeping_unit=input.stock_keeping_unit,
                                   title=input.title,
                                   product_type=input.product_type,
                                   price=input.price)
        product_instance.save()
        return CreateProduct(ok=ok, product=product_instance)


class UpdateProduct(graphene.Mutation):
    """Мутация изменения продукта"""

    class Arguments:
        id = graphene.Int(required=True)
        input = ProductInput(required=True)

    ok = graphene.Boolean()
    product = graphene.Field(ProductGraphQLType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        product_instance = Product.objects.get(pk=id)
        if product_instance:
            ok = True
            product_instance.stock_keeping_unit = input.stock_keeping_unit
            product_instance.title = input.title
            product_instance.product_type = input.product_type
            product_instance.price = input.price
            product_instance.save()
            return UpdateProduct(ok=ok, product=product_instance)
        return UpdateProduct(ok=ok, product=None)


class CreateProductType(graphene.Mutation):
    """Мутация создания типа продукта"""

    class Arguments:
        input = ProductTypeInput(required=True)

    ok = graphene.Boolean()
    product_type = graphene.Field(ProductTypeGraphQLType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        product_type_instance = ProductType(title=input.title)
        product_type_instance.save()
        return CreateProductType(ok=ok, product_type=product_type_instance)


class UpdateProductType(graphene.Mutation):
    """Мутация изменения типа продукта"""

    class Arguments:
        id = graphene.Int(required=True)
        input = ProductInput(required=True)

    ok = graphene.Boolean()
    product_type = graphene.Field(ProductTypeGraphQLType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        product_type_instance = ProductType.objects.get(pk=id)
        if product_type_instance:
            ok = True
            product_type_instance.title = input.title
            product_type_instance.save()
            return UpdateProductType(ok=ok, product_type=product_type_instance)
        return UpdateProductType(ok=ok, product_type=None)


class Mutation(graphene.ObjectType):
    """Мутации"""
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    create_product_type = CreateProductType.Field()
    update_product_type = UpdateProductType.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
