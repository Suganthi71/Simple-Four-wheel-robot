import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class RandomListener(Node):
    def __init__(self):
        super().__init__('random_listener')
        self.subscription = self.create_subscription(Int32, 'numbers', self.listener_callback, 10)

    def listener_callback(self, msg):
        if msg.data > 80:
            self.get_logger().info(f'ALERT! Number is {msg.data}')
        else:
            self.get_logger().info(f'Number: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = RandomListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
