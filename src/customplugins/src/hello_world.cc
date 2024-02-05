#include <gazebo/gazebo.hh>

namespace gazebo {

class WorldPLuginTutorial : public WorldPlugin {
    public:
    WorldPLuginTutorial() : WorldPlugin() {
        printf("Hello World!\n");
    }
    public:
    void Load(physics::WorldPtr _world, sdf::ElementPtr _sdf){}

};
GZ_REGISTER_WORLD_PLUGIN(WorldPLuginTutorial)
}