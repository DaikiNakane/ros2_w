import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0

def cb():
    global n
    if n % 2 == 0: # nが偶数の場合のみメッセージを送信する
        msg = Int16()
        msg.data = n
        pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)

