import taodata as td
import pandas as pd

import json

if __name__ == '__main__':
    api = td.get_api('123456', 30)

    api_name = td.WbBlog.name

    bodyHelper = td.BodyHelper()
    bodyHelper.match_phrase(td.WbBlog.fields.blog_raw_text, '疫情形势').exists(td.WbBlog.fields.blog_retweeted_status_id, 'must_not')
    body = bodyHelper.to_json()
    print(body)
    fields = [td.WbBlog.fields.blog_id, td.WbBlog.fields.blog_raw_text]
    params = {
        'body': body,
        'archive_day': '20220301'
    }
    data = api.query(api_name=api_name, fields=fields, **params)
    print(data['info'])

    df = pd.DataFrame(columns=data['alias_fields'], data=data['items'])
    print(df)

    api.export('export.json', 'json', api_name, fields, **params)

