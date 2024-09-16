from user import User
from post import Post

app_user_1 = User("<EMAIL>", "Jane", "<PASSWORD>", "Software Engineer")
app_user_1.get_user_info()
app_user_1.change_job_title("Data Scientist")
app_user_1.get_user_info()
app_post_1 = Post("hello all", "jane doe")
app_post_1.get_post_info()