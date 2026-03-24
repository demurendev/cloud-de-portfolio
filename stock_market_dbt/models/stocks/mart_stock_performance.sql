with staged as (
    select * from {{ ref('stg_stock_prices') }}
),

performance as (
    select
        ticker,
        min(price_date) as first_date,
        max(price_date) as last_date,
        round(avg(daily_return_pct)::numeric, 4) as avg_daily_return,
        round(max(close_price)::numeric, 2) as highest_price,
        round(min(close_price)::numeric, 2) as lowest_price,
        round(avg(moving_avg_5day)::numeric, 2) as avg_5day_ma,
        sum(volume) as total_volume
    from staged
    group by ticker
    order by avg_daily_return desc
)

select * from performance