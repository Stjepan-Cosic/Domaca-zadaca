from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'dz5'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch',
'*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stjepancosic',
    maintainer_email='stjepan.cosic9@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'static_turtle_tf2_broadcaster = dz5.static_turtle_tf2_broadcaster:main',
            'turtle_tf2_broadcaster = dz5.turtle_tf2_broadcaster:main',
            'turtle_tf2_listener = dz5.turtle_tf2_listener:main',
            'goal_broadcaster= dz5.goal_broadcaster:main',
            'turtle_controller= dz5.turtle_controller:main',
        ],
    },
)
