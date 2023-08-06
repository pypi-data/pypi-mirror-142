# b2binpay-py
> Python library for working with [B2binPay](https://docs.b2binpay.com/v2/en/api-reference.html?roistat_visit=584687)
# Install
`pip install b2binpay-py`

## Example 
```buildoutcfg
from b2binpay import client
import asyncio


async def main():
    c = await client.AsyncClient("API_KEY", "API_SERCET", test=True).connect()
    w = await c.get_wallets()
    await c.close_connection()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

```