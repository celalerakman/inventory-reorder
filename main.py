"""Inventory warning using lead-time demand and explicit safety stock."""
from math import isfinite


def reorder(on_hand, daily_use, lead_days, safety_stock):
    values = (on_hand, daily_use, lead_days, safety_stock)
    if any(not isfinite(v) or v < 0 for v in values):
        raise ValueError('Finite non-negative inputs required')
    threshold = daily_use * lead_days + safety_stock
    return {'threshold': threshold, 'reorder': on_hand <= threshold}


if __name__ == '__main__':
    print(reorder(110, 12, 7, 30))
