
class WbBlogFields:
    blog_id = 'blog.id'
    blog_raw_text = 'blog.raw_text'
    blog_text = 'blog.text'
    blog_source = 'blog.source'
    blog_reposts_count = 'blog.reposts_count'
    blog_comments_count = 'blog.comments_count'
    blog_attitudes_count = 'blog.attitudes_count'
    blog_created_at = 'blog.created_at'
    blog_pid = 'blog.pid'
    blog_user_id = 'blog.user.id'
    blog_user_screen_name = 'blog.user.screen_name'
    blog_user_statuses_count = 'blog.user.statuses_count'
    blog_user_verified = 'blog.user.verified'
    blog_user_description = 'blog.user.description'
    blog_user_gender = 'blog.user.gender'
    blog_user_follow_count = 'blog.user.follow_count'
    blog_user_followers_count = 'blog.user.followers_count'
    blog_retweeted_status_id = 'blog.retweeted_status.id'
    blog_retweeted_status_raw_text = 'blog.retweeted_status.raw_text'
    blog_retweeted_status_text = 'blog.retweeted_status.text'
    blog_retweeted_status_source = 'blog.retweeted_status.source'
    blog_retweeted_status_reposts_count = 'blog.retweeted_status.reposts_count'
    blog_retweeted_status_comments_count = 'blog.retweeted_status.comments_count'
    blog_retweeted_status_attitudes_count = 'blog.retweeted_status.attitudes_count'
    blog_retweeted_status_created_at = 'blog.retweeted_status.created_at'
    blog_retweeted_status_user_id = 'blog.retweeted_status.user.id'
    blog_retweeted_status_user_screen_name = 'blog.retweeted_status.user.screen_name'
    blog_retweeted_status_user_statuses_count = 'blog.retweeted_status.user.statuses_count'
    blog_retweeted_status_user_verified = 'blog.retweeted_status.user.verified'
    blog_retweeted_status_user_description = 'blog.retweeted_status.user.description'
    blog_retweeted_status_user_gender = 'blog.retweeted_status.user.gender'
    blog_retweeted_status_user_follow_count = 'blog.retweeted_status.user.follow_count'
    blog_retweeted_status_user_followers_count = 'blog.retweeted_status.user.followers_count'


class WbBlogParams:
    action = 'action'
    archive_day = 'archive_day'
    body = 'body',
    scroll = 'scroll',
    scroll_id = 'scroll'
    export_file = 'export_file'
    export_type = 'export_type'


class WbBlog:
    name = 'wb_blog'
    fields = WbBlogFields()
    params = WbBlogParams()








