from channels import route
from channels.staticfiles import StaticFilesConsumer
from posts.consumers import connect_blog, disconnect_blog
from chat import consumers  


channel_routing=[

route('websocket.connect',connect_blog,path=r'^/posts/(?P<slug>[^/]+)/stream/$'),
route("websocket.disconnect", disconnect_blog, path=r'^/posts/(?P<slug>[^/]+)/stream/$'),

# 'http.request', StaticFilesConsumer(),
route('websocket.connect',consumers.ws_connect),
route('websocket.receive',consumers.ws_receive),
route('websocket.disconnect',consumers.ws_disconnect),

]