select
    price_date,
    ticker,
    open_price,
    high_price,
    low_price,
    close_price,
    volume,
    daily_return_pct,
    moving_avg_5day
from {{ ref('stock_prices_sample') }}