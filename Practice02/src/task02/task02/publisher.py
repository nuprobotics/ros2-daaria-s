import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.parameter import Parameter


class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')

        # Load parameters from the parameter file
        self.declare_parameter('text', 'Hello, ROS2!')

        # Get parameters
        self.topic_name = self.get_parameter('topic_name').get_parameter_value().string_value
        self.text = self.get_parameter('text').get_parameter_value().string_value

        # Create a publisher
        self.publisher = self.create_publisher(String, self.topic_name, 10)

        # Create a timer to publish messages periodically
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = self.text
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}" to "{self.topic_name}"')


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()

    # Process command line parameters
    if len(args) > 1:
        node.set_parameters([
            Parameter('text', value=args[1])
        ])

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
