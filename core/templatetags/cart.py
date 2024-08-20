from django import template 

register=template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(item,cart):
    if str(item.id) in cart:
        return True 
    return False


@register.filter(name='quantity_in_cart')
def quantity_in_cart(item,cart):
    
    return cart[str(item.id)]



@register.filter(name='price_total')
def price_total(item,cart):
    return item.price * quantity_in_cart(item,cart)

@register.filter(name='cart_total_price')
def cart_total_price(items,cart):
    sum=0

    for item in items:
        sum+=item.price * quantity_in_cart(item,cart)
    return sum

@register.filter(name='sumCart')
def sumCart(l):
    return sum(l)


