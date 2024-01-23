#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class NodeTemplate(Node): # Modify file name

    def __init__(self):
        super().__init__("node_name") # Shortened version of node name
        self.counter_= 0
        self.create_timer(0.5,self.timer_callback)

    def timer_callback(self): 
        self.counter_ +=1
        self.get_logger().info("Hello from sample node : " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args)
    node=NodeTemplate() # Modify file name
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__== "__main__":
    main()