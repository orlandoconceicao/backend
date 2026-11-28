import math
from django.core.paginator import Paginator


def make_pagination_range(page_range, window_size, current_page):
    middle_page = math.ceil(window_size / 2)
    start_range = current_page - middle_page
    stop_range = current_page + middle_page
    total_pages = len(page_range)
    
    start_range_offset = abs(start_range) if start_range < 0 else 0

    # Mantém a quantidade de páginas visíveis quando o intervalo começa antes da primeira página.
    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset
        
    # Desloca o intervalo de volta quando ele ultrapassa a última página.
    if stop_range >= total_pages:
        start_range = start_range - abs(stop_range - total_pages)

    pagination = page_range[start_range:stop_range]
    return {
        'pagination': pagination,
        'page_range': page_range,
        'window_size': window_size,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page > middle_page,
        'last_page_out_of_range': stop_range < total_pages,
        'middle_page': middle_page,
    }

def make_pagination(request, queryset, per_page, window_size=4):
    try:
        current_page = int(request.GET.get("page", 1))
    except ValueError:
        current_page = 1
        
    paginator = Paginator(queryset, per_page)
    page_object = paginator.get_page(current_page)
    
    pagination_range = make_pagination_range(
        paginator.page_range,
        window_size,
        current_page
    )
    
    return page_object, pagination_range