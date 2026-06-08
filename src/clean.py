import pandas as pd

def clean_customers(df):
    df = df.copy().drop_duplicates(subset=['customer_id'])
    df['email'] = df['email'].fillna('unknown@example.com')
    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
    df = df.dropna(subset=['signup_date'])
    df['country'] = df['country'].str.strip().str.title()
    return df

def clean_products(df):
    df = df.copy().drop_duplicates(subset=['product_id'])
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df[df['price'] > 0]
    df['category'] = df['category'].str.strip().str.title()
    return df

def clean_orders(df, customers, products):
    df = df.copy().drop_duplicates(subset=['order_id'])
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    today = pd.Timestamp.today().normalize()
    df = df.dropna(subset=['order_date', 'quantity'])
    df = df[(df['order_date'] <= today) & (df['quantity'] > 0)]
    df = df[df['customer_id'].isin(set(customers['customer_id']))]
    df = df[df['product_id'].isin(set(products['product_id']))]
    return df

def clean_payments(df, orders):
    df = df.copy().drop_duplicates(subset=['payment_id'])
    df['payment_date'] = pd.to_datetime(df['payment_date'], errors='coerce')
    df['payment_amount'] = pd.to_numeric(df['payment_amount'], errors='coerce')
    df['payment_status'] = df['payment_status'].str.strip().str.title()
    df = df.dropna(subset=['payment_date', 'payment_amount'])
    df = df[df['payment_amount'] > 0]
    return df[df['order_id'].isin(set(orders['order_id']))]

def clean_refunds(df, orders):
    df = df.copy().drop_duplicates(subset=['refund_id'])
    df['refund_date'] = pd.to_datetime(df['refund_date'], errors='coerce')
    df['refund_amount'] = pd.to_numeric(df['refund_amount'], errors='coerce')
    df = df.dropna(subset=['refund_date', 'refund_amount'])
    df = df[df['refund_amount'] > 0]
    return df[df['order_id'].isin(set(orders['order_id']))]

def clean_all(raw):
    customers = clean_customers(raw['customers'])
    products = clean_products(raw['products'])
    orders = clean_orders(raw['orders'], customers, products)
    payments = clean_payments(raw['payments'], orders)
    refunds = clean_refunds(raw['refunds'], orders)
    return {'customers': customers, 'products': products, 'orders': orders, 'payments': payments, 'refunds': refunds}
