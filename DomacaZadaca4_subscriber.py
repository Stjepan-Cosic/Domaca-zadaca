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
        self.subscription  # spriječava upozorenje o nekorišćenoj varijabli
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = '%d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Objavljeno: "%s"' % msg.data)
        self.i += 1

    def listener_callback(self, msg):
        received_number = int(msg.data)  # Pretvara primljenu poruku u broj
        square = received_number ** 2     # Računa kvadrat primljenog broja
        self.get_logger().info('Primljeno: "%d", Kvadrat: "%d"' % (received_number, square))

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher_subscriber = MinimalPublisherSubscriber()
    rclpy.spin(minimal_publisher_subscriber)
    # Eksplicitno uništavanje čvora
    # (opciono - inače će se automatski uništiti
    # kada sakupljač smeća uništi objekat čvora)
    minimal_publisher_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()