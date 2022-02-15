from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from core.models import BaseModel
from customer.models import Customer
from product.models import Product


# Create your models here.


class Cart(BaseModel):
    total_price = models.PositiveIntegerField(help_text="Total Price", default=0)
    final_price = models.PositiveIntegerField(help_text="Final Price", default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    off_code = models.OneToOneField("OffCode", on_delete=models.CASCADE, null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def calculate_total_price(self):   ############# FRONT FUNCTION #############
        all_order_items = self.orderitem_set.all()
        for order in all_order_items:
            each_price = order.product.price
            price_for_all = each_price * order.how_many
            self.total_price += price_for_all
        return self.total_price

    def calculate_final_price(self):  ############# FRONT FUNCTION #############
        all_order_items = self.orderitem_set.all()
        if self.off_code is not None:
            for order in all_order_items:
                discounted_prices = order.sum_of_prices_after_discount()
                self.final_price += discounted_prices

            self.final_price = self.final_price * (100 - self.off_code.value) // 100

            return self.final_price

        else:
            for order in all_order_items:
                discounted_prices = order.sum_of_prices_after_discount()
                self.final_price += discounted_prices
                return self.final_price

    def check_is_paid(self):
        if self.is_paid is True:
            self.is_deleted = True
        else:
            pass


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    how_many = models.PositiveSmallIntegerField(help_text="How many of this product do you need")

    def sum_of_prices_after_discount(self):
        res = self.product.after_discount_price() * self.how_many
        return res


class OffCode(BaseModel):
    the_code = models.CharField(max_length=10, help_text="Enter code for offer", unique=True)
    value = models.PositiveIntegerField(help_text="Enter code percentage for offer",
                                        validators=[MinValueValidator(1), MaxValueValidator(100)])
    is_active = models.BooleanField(default=True)
    how_many_use = models.PositiveSmallIntegerField(default=3, help_text="how many times do you want this code")

    def dis_activator(self):
        if self.how_many_use == 0:
            self.is_active = False
            self.is_deleted = True
        else:
            pass
