from django.db import models
from django.conf import settings
from book.models import Book


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Is the list of save for later empty?
    def is_saved_empty(self):
        items = self.cartitem_set.all()
        for item in items:
            if item.save_for_later is True:
                return False
        return True

    # Is the cart empty?
    def is_cart_empty(self):
        items = self.cartitem_set.all()
        if items:
            for item in items:
                if item.save_for_later is False:
                    return False
        return True


class CartItem(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    save_for_later = models.BooleanField(default=False, null=False)

    # Compute price
    @property
    def cost(self):
        return self.quantity * self.item.price


# Does the user have a cart?
def has_cart(user):
    carts = Cart.objects.all()
    for cart in carts:
        if user == cart.user:
            return True
    return False


# Calculate the subtotal
def total(cart_items):
    subtotal = 0
    for cart_item in cart_items:
        if cart_item.save_for_later is False:
            subtotal += cart_item.cost
    return subtotal
