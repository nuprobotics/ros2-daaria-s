import rclpy
from std_msgs . msg import String
from rclpy . node import Node


class ReceiverNode(Node):
    def __init__(self):
        super(ReceiverNode, self).__init__("receiver")
        self.subscriber = self.create_subscription(String, "receiver",
                                                   self.subscriber_callback, qos_profile=10)

    def subscriber_callback(self, msg):
        self.get_logger().info(f" Received : {msg.data}")


def main():
    rclpy.init()
    node = ReceiverNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
