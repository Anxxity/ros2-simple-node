#!/usr/bin/env python3  

import rclpy
from rclpy.node import Node

class SimpleNode(Node):
    def __init__(self):
        super().__init__("simple_node")
        self.get_logger().info("SimpleNode initialized")


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin(node)  # Keep the node running & help run timers, callbacks, etc
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()