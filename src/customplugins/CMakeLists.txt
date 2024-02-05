cmake_minimum_required(VERSION 3.0.2)
project(customplugins)

## Compile as C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)
find_package(gazebo REQUIRED)


find_package(catkin REQUIRED COMPONENTS
  gazebo_plugins
  gazebo_ros
  roscpp
)

catkin_package(DEPENDS
                    roscpp
                    gazebo_ros
                    )


include_directories(
  ${catkin_INCLUDE_DIRS}
)

include_directories(${GAZEBO_INCLUDE_DIRS} ${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
list(APPEND CMAKE_CXX_FLAGS "${GAZEBO_CXX_FLAGS}")

add_library(hello_world SHARED src/hello_world.cc)
target_link_libraries(hello_world ${GAZEBO_LIBRARIES} ${catkin_LIBRARIES})



