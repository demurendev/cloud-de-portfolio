with source as (
    select * from {{ ref('raw_stock_prices') }}
),

staged as (
    select
        price_date,
        ticker,
        close_price,
        open_price,
        high_price,
        low_price,
        volume,
        daily_return_pct,
        moving_avg_5day
    from source
    where close_price > 0
      and price_date is not null
)

select * from staged