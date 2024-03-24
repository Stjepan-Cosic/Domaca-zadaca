import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisherSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_publisher_subscriber')
        self.publisher_ = self.create_publisher(String, 'Kvadrat_broja', 10)
        self.subscription = self.create_subscription(
            String,
            'Broj',
            self.listener_callback,
            10
        )
        self.subscription  
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = '%d' % self.i
        self.get_logger().info('Objavljeno: "%s"' % msg.data)
        self.i += 1

    def listener_callback(self, msg):
        received_number = int(msg.data) 
        square = received_number ** 2     
        self.get_logger().info('Primljeno: "%d", Kvadrat: "%d"' % (received_number, square))
        square1 = String()
        square1.data = '%d' % square
        self.publisher_.publish(square1)
        
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher_subscriber = MinimalPublisherSubscriber()
    rclpy.spin(minimal_publisher_subscriber)
    
    minimal_publisher_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
