#!usr/bin/env python3

import rclpy
from rclpy.node import Node

class Timer(Node):
    def __init__(self):
        super().__init__("timer_node")
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.counter = 0
    
    # def print_primes(self, n):
    #     primes = []
    #     num = 2
    #     while len(primes) < n:
    #         is_prime = True
    #         for p in primes:
    #             if num % p == 0:
    #                 is_prime = False
    #                 break
    #         if is_prime:
    #             primes.append(num)
    #         num += 1
    #     return primes
    def list(self, n):
        list_of_words = ["idle", "run", "walk", "jump"]
        return list_of_words[n]

    def timer_callback(self):
        self.counter += 1 
        # self.get_logger().info('Timer callback triggered %d' % self.counter)   
        # self.get_logger().info('First %d prime numbers: %s' % (self.counter, self.print_primes(self.counter))) 
        self.get_logger().info('First %d words: %s' % (self.counter, self.list(self.counter)))

def main(args=None):
        rclpy.init(args=args)
        node=Timer()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()
        
if __name__ == '__main__':
     main()        