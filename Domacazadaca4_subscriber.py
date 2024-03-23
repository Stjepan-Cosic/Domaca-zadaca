import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10
        )
        self.subscription  # spriječava upozorenje o nekorišćenoj varijabli

    def listener_callback(self, msg):
        received_number = int(msg.data)  # Pretvara primljenu poruku u broj
        square = received_number ** 2     # Računa kvadrat primljenog broja
        self.get_logger().info('Primljeno: "%d", Kvadrat: "%d"' % (received_number, square))

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    # Eksplicitno uništavanje čvora
    # (opciono - inače će se automatski uništiti
    # kada sakupljač smeća uništi objekat čvora)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()