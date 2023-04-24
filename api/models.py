from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):

        return {
            'id': self.id,
            'name': self.name
        }



class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural= 'SubCategories'

    def to_json(self):
        
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'category_id': self.category.id
        }


class SubSubCategory(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(SubCategory, related_name="subsubcategories", on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'SubSubCategories'

    def to_json(self):
        
        return {
            'id': self.id,
            'name': self.name,
            'subcategory': self.subcategory
        }



