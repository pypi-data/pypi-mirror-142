import taodata as td
import pandas as pd

import json

if __name__ == '__main__':
    api = td.get_api('123456', 30)

    api_name = 'wb_blog'

    data = api.query(api_name)
    df = pd.DataFrame(columns=data['alias_fields'], data=data['items'])
    print(df)
    api.clear()
    api.export('export.xlsx',api_name,fields=['blog.id', 'blog.raw_text'])


