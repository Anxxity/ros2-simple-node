import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/remin/Desktop/ros2-creating _simple_node/install/simplenode'
