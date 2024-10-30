from django.shortcuts import render
from .models import Customer
import logging
logger = logging.getLogger(__name__)
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import Count # type: ignore
from django.utils.timezone import now, timedelta # type: ignore
from django.http import JsonResponse # type: ignore




def get_user_registration_stats(request):
    # Daily registered users (last 6 days)
        daily_counts = Customer.objects.filter(
            user_joined_date__gte=now() - timedelta(days=6)
        ).extra(select={'day': 'date(user_joined_date)'}).values('day').annotate(count=Count('user_id'))

        # Monthly registered users (last 6 months)
        monthly_counts = Customer.objects.filter(
            user_joined_date__gte=now() - timedelta(days=180)
        ).extra(select={'month': "to_char(user_joined_date, 'YYYY-MM')"}).values('month').annotate(count=Count('user_id'))

        return JsonResponse({
            'daily': list(daily_counts),
            'monthly': list(monthly_counts),
        })