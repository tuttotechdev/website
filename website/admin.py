from django.contrib import admin

from website.models import Category, Product, Feedback, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "image"]

    search_fields = ["product__name"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    readonly_fields = ["id"]
    search_fields = ["id", "name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "slug",
        "created_at",
        "updated_at",
        "short_description",
        "cost",
        "clicks",
        "views",
        "purchased",
    ]

    inlines = [ProductImageInline]

    readonly_fields = ["id", "clicks", "views", "created_at", "updated_at"]

    search_fields = [
        "id",
        "name",
        "slug",
        "short_description",
        "short_description_it",
        "description",
        "description_it",
        "labels_it",
        "labels",
        "categories__name",
        "categories__slug",
    ]

    list_filter = ["categories", "is_active", "is_featured"]


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "rating"]
    readonly_fields = ["user", "product", "feedback", "rating"]

    search_fields = [
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
        "feedback",
        "product__name",
        "product__slug",
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
